# Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта geekbrains.ru.
# У вас два пути решения:
# * использовать регулярные выражения (библиотеку re),
# * использовать библиотеку BeautifulSoup.

import os
import re
from bs4 import BeautifulSoup as BS

with open('startpage.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print('---------использовать регулярные выражения (библиотеку re)---------')
pattern = re.compile('<span class="total-users">Нас уже ([0-9 ]+) человек</span>')
users = pattern.findall(text)[0]
print(users)
number_of_students = re.sub('\s', '', users)
print(number_of_students)

print('---------использовать библиотеку BeautifulSoup---------')

soup = BS(text, 'html.parser')
span=soup.span.string
print(span)

temp=re.findall('\s[0-9 ]+\s',span)[0]
print(temp)
number_of_students=re.sub('\s','',temp)
print(number_of_students)
