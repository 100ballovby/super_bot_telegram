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


