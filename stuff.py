import requests as r
from jinja2 import Template


def get_dog_img():
    url = 'https://random.dog/woof.json'
    resp = r.get(url).json()
    return resp['url']


def make_template(filename):
    with open(f'templates/{filename}.html', 'r', encoding='utf-8') as f:
        text = f.read()
    template = Template(text)
    return template


def parse_horo(sign):
    url = f"https://horoscopes-ai.p.rapidapi.com/get_horoscope_en/{sign}/tomorrow/general"

    headers = {
        "X-RapidAPI-Key": "4b3d784309msh1a54be2ab333712p1f580cjsn967b22d81802",
        "X-RapidAPI-Host": "horoscopes-ai.p.rapidapi.com"
    }

    response = r.get(url, headers=headers)
    res = response.json()
    return res['general'][0]



