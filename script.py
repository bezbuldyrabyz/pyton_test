# Первый сценарий на языке Python

import sys
import myfile
from myfile import title # еще один вариант импорта
from myfile import a, b, c
import math
import random

print(sys.platform)
print(myfile.title)
print(a)

print(2**100)
s="Spam!"
print(s*8)

#-- for example
for  x in s:
    print(x)

print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1,2,3,4]))

# строки
print(title)
print(len(title))
print(title[0])
print(title[1])
print(title[-1])
print(title[len(title)-1])
print(title[1:3]) # cрез строки title начиная со смещения 1 и до 2 (не 3)
print(title[1:]) # Все, кроме первого элемента (1:len(title))
print(title[0:3])
print(title[:3])
print(title[:-1]) # все, кроме последнего элемента
print(title[:]) # Все содержимое title, как обычная копия (0:len(title))
print(title + " xyz") # Конкатенация

print(s.find("pa")) # Поиск смещения подстроки

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
l.append("NI") # Увеличение: в конец списка добавляется новый объект
print(l)
l.pop(2) # Уменьшение: удаляется элемент из середины списка
print(l)

# списки

m=["bb","aa","cc"]
m.sort()
print(m)
m.reverse()
print(m) # сортировка в обратном направлении

m= [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(m)
print(m[1])
print(m[1][2])
col2=[row[1] for row in m] # Выбирает элементы второго столбца
print(col2)
print(m)
print([row[1]+1 for row in m])
print([row[1] for row in m if row[1]%2==0]) # отфильтровать нечетные значения

diag=[m[i][i] for i in [0,1,2]]
print(diag)
doubles=[c*2 for c in "spam"]
print(doubles)

g=(sum(row) for row in m) # Генератор, возвращающий суммы элементов строк
print(next(g)) # Вызов в соответствии с протоколом итераций
print(next(g))
print(list(map(sum,m))) # Отобразить sum на элементы в M
print({sum(row) for row in m}) # Создаст множество сумм строк
print({i:sum(m[i]) for i in range(3)}) # Таблица пар ключ/значение сумм строк
print([ord(x) for x in "spaam"]) # Список кодов символов
print({x:ord(x) for x in "spaam"})


# отображения (словари)

d={"food":"Spam", "quantity": 4, "color": "pink"}
print(d["food"])
d["quantity"]+=1 # Прибавить 1 к значению ключа ‘quantity’
print(d)

d={}
print(d)
d["name"]="Bob"
d["job"]="dev"
d["age"]=40
print(d)
print(d["name"])

rec = {"name":{"first":"Bob","last":"Smith"},
        "job":["dev","mgr"],
        "age":40.5}
print(rec)
print(rec["name"]["last"])
print(rec["job"][-1])
rec["job"].append("janitor")
print(rec)
rec=0
print(rec)

d={"a":1,"c":2,"b":3}
ks=list(d.keys())
ks.sort() # Сортировка списка ключей
print(ks)
for i in ks:
    print(i, "=>", d[i]) # Здесь дважды нажмите клавишу Enter

for i in sorted(d):
    print(i, "=>", d[i])

x=4
while x>0:
    print("spam!"*x)
    x-=1


# итерационная оптимизация

squares=[x**2 for x in [1,2,3,4,5]]
print(squares)

squares=[]
for x in [1,2,3,4,5]:
    squares.append(x**2)
print(squares)

if not "f" in d:
    print('missing')

value=d.get("x", 0)
print(value)
print(d)
value=d["x"] if "x" in d else 0
print(value)


# кортежи

t=(1,2,3,4)
print(len(t))
print(t+(5,6))
print(t.index(4))
print(t.count(4))
print(t[2])


# другие базовые типы

x=set("spam")
y={"h","a","m"}
print(x,y)
print(x&y) # Пересечение
print(x|y) # Объединение
print(x-y) # Разность
print({x**2 for x in [1,2,3,4]})

print(1/3) # Вещественное число
print((2/3)+(1/2))

import decimal # Вещественные числа с фиксированной точностью
d=decimal.Decimal("3.141")
print(d+1)
decimal.getcontext().prec=2
print(decimal.Decimal("1.00")/decimal.Decimal("3.00"))
from fractions import Fraction
f=Fraction(2,3)
print(f+1)
print(f+Fraction(1,2))
print(1>2,1<2)
print(bool("spam"))
x=None # Специальный объект None
print(x)
l=[None]*100
print(l)
print(type(l))
print(type(type(l)))

if type(l)==type([]):
    print ('yes')

if(isinstance(l,list)):
    print("yes")

# типы данных
print("100: ", hex(100), ", ", oct(100), ", ", bin(100))


# числовые операции

print(int(3.1415)) # Усекает дробную часть вещественного числа
print(float(3)) # Преобразует целое число в вещественное

num=1/3

print(repr(num)) # Используется для автоматического вывода: в форме как есть
print(str(num)) # Используется функцией print: дружественная форма
print(4//3) # деление с округлением вниз

print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

print(5//2, 5//-2)
print(5//2.0, 5//-2.0)
print(99999999999999999999999999999999999999999999999999999999999999999+1)
print(2**200)
print(eval("64"),eval("0o100"))
print("{0:o}, {1:x}, {2:b}".format(64,64,64))
print("%o, %x, %X" % (64,255,255))

x=1
print(x<<2) # Сдвиг влево на 2 бита: 0100
print(x|2) # Побитовое ИЛИ: 0011
print(x&1) # Побитовое И: 0001
print(round(2.567,2))
print("%.2f" % (1/3))
print(random.random())
print(random.randint(1,10))
print(random.choice(["Life of Brian","Holy Grail","Meaning of Life"]))

print(decimal.Decimal("0.1")+decimal.Decimal("0.1")+decimal.Decimal("0.1")-decimal.Decimal("0.3"))
print(decimal.Decimal("0.1")+decimal.Decimal("0.10")+decimal.Decimal("0.10")-decimal.Decimal("0.3"))
decimal.getcontext().prec=4
print(decimal.Decimal(1)/decimal.Decimal(7))
decimal.getcontext().prec=2
pay=decimal.Decimal(str(1999+1.33))
print(pay)
print(decimal.Decimal("1.00")/decimal.Decimal("3.00"))
with decimal.localcontext() as ctx:
    ctx.prec=4
    print(decimal.Decimal("1.00")/decimal.Decimal("3.00"))

x=Fraction(1,3)
y=Fraction(4,6)
print(x)
print(Fraction(".25"))
print(Fraction(".25")+Fraction("1.25"))
