import telebot
import stuff


bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    template = stuff.make_template('start')
    username = message.chat.username
    msg = template.render(username=username)
    pin = bot.send_message(message.chat.id, text=msg, parse_mode='html')
    bot.pin_chat_message(message.chat.id, message_id=pin.id)


@bot.message_handler(commands=['dog'])
def send_dog(message):
    img = stuff.get_dog_img()
    bot.send_photo(message.chat.id, photo=img)



if __name__ == '__main__':
    bot.polling()
