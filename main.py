from num2words import num2words
import re

list_with_en = []
list_with_ru = []

with open('PythonTest.txt', 'r') as file:

    def has_cyrillic(text):
        return bool(re.search('[а-яА-Я]', text))

    for str_with_words in file.readlines():
        str_with_words = tuple(str(str_with_words).replace(";", '').split())
        print(str_with_words)
        str1 = ''
        str2 = ''
        for i in str_with_words:
            if i.isdigit():
                i = num2words(i)
            str_for_list = has_cyrillic(i)
            print(str_for_list)

            if not str_for_list:
                str1 += i + ' '
            else:
                str2 += i + ' '
        list_with_en.append(str1)
        list_with_ru.append(str2)

print(list_with_en)
print(list_with_ru)

with open('en.txt', 'w') as f_en:
    for i in list_with_en:
        f_en.write( i + '\n')

with open('ru.txt', 'w') as f_ru:
    for i in list_with_ru:
        f_ru.write( i + '\n')
