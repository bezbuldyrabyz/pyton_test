# Первый сценарий на языке Python

import sys
import myfile
from myfile import title # еще один вариант импорта
from myfile import a, b, c

print(sys.platform)
print(myfile.title)
print(a)
print(title)
print(2**100)
x="Spam!"
print(x*8)

#-- for example
for  x in "spam":
    print(x)

input()
