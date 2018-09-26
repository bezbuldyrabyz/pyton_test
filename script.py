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

print(s.find("pa"))
