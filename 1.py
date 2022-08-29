import re


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


a = has_cyrillic('да')
if a == True:
    print(2)