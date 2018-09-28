# методы строковых типов

line = 'aaa,bbb,ccccc,dd'
print(line.split(",")) # Разбивает строку по разделителю и создает список строк
print(line.upper())
print(line.isalpha()) # Проверка содержимого: isalpha, isdigit и так далее
print("absd".isalpha())
line='aaa,bbb,ccccc,dd\n'
print(line)
line=line.rstrip() # Удаляет завершающие пробельные символы
print(line)
print("%s, eggs, and %s" % ("spam", "SPAM!"))
print("{0}, eggs, and {1}".format("spam", "SPAM!"))
print(dir(line))
print(help(line.replace))
print("A\nB\tC")
print(ord("\n")) # В ASCII \n – это байт с числовым значением 10
s="a\0B\0C" # \0 – это двоичный ноль, не является завершителем строки
print(len(s))
msg = """ aaaaaaaaaa
bbb'''bbbbbbbbb""bbbbbb'bbbbbb
cccccccccccccccccccc"""
print(msg)

#поиск по шаблону

import re
match = re.match("Hello[ \t]*(.*)world", "Hello    Python world")
print(match.group(1))
match = re.match("/(.*)/(.*)/(.*)", "/usr/home/lumberjack")
print(match.groups())

# операции над последовательностями

l=[123, "spam", 1.23]
print(len(l))
print(l[:-1]) # Операция получения среза возвращает новый список
print(l+[4,5,6]) # Операция конкатенации также возвращает новый список
print(l) # Наши действия не привели к изменению оригинального списка
