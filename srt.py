# Неформатированные строки подавляют экранирование

path=r"C:\new\text.dat"
print(path)

# Тройные кавычки, многострочные блоки текста

mantra="""Always look
    on the bright
    side of life."""
print(mantra)


# временного отключения строк программного кода

x=1
"""
import os
print(os.getcwd())
"""
y=2
print(x)


# базовые операции над строками

print(len("abc"))
print("abc" + "def") # Конкатенация: новая строка
print("-"*80)

myjob="hacker"
for i in myjob: print(i, end=" ") # Обход элементов строки в цикле

print("k" in myjob)
print("z" in myjob)
print("spam" in "abcspamdef")


# Расширенная операция извлечения подстроки: третий предел
s="abcdefghijklmnop"
s[1:10:2]
print(s[::2]) # вернет каждый второй элемент от начала и до конца последовательности
s="hello"
print(s[::-1]) #-1, указывает, что срез должен быть выбран в обратном порядке – справа налево, а не слева направо

# Изменение строк

s="spam"
s=s+"SPAM!"
s=s[:4]+"Burger"+s[-1]
print(s)
s="splot"
print(s.replace("pl","pamal"))


# cтроковые методы
s="help"
print(s.capitalize())
print(s.isalpha())
s="xxxxSPAMxxxxSPAMxxxx"
where =s.find("SPAM") # Подстрока найдена со смещением 4
print(where)
s=s[:where]+"EGGS"+s[(where+4):]
print(s)
s="spammy"
l=list(s)
print(l)
l[3]="x"
l[4]="x"
print(l)
s="".join(l)
print(s)
print("SPAM".join(["eggs","sausage","ham","toast"]))


# строки и базовые методы http://pythonz.net/references/named/str/

line="     the knights who sy Ni!\n"
line.capitalize() # Возвращает копию строки, делая первую букву заглавной

'ß'.lower()  # 'ß'
print('ß'.casefold())  # 'ss' - Возвращает копию строки в сложенном регистре.

print("".center(3,"w")) # Позиционирует по центру указанную строку, дополняя её справа и слева до указанной длины указанным символом.
print("1".center(2,"w"))
print("1".center(4,"w")) # ... Символ добавляется к строке циклично сначала справа, затем слева.
print("1".center(0,"w"))
print("1".center(4))

my_str = "podstroka is strok"
print(my_str.count("stroka")) # 1 - Для строки возвращает количество непересекающихся вхождений в неё указанной подстроки.
my_str.count("str")  # 2
my_str.count('str', 0, -1)  # 2

# print(getdefaultencoding())  # utf-8
my_string = 'кот cat'
print(type(my_string))  # str
print(my_string.encode())
print(my_string.encode('ascii', errors='ignore')) # b' cat'
my_string.encode('ascii', errors='replace') # b'??? cat'
print(my_string.encode('ascii', errors='xmlcharrefreplace')) # b'&#1082;&#1086;&#1090; cat'
print(my_string.encode('ascii', errors="backslashreplace")) # b'\\u043a\\u043e\\u0442 cat'
print(my_string.encode("ascii", errors="namereplace")) # b'\\N{CYRILLIC SMALL LETTER KA}\\N{CYRILLIC SMALL LETTER O}\\N{CYRILLIC SMALL LETTER TE} cat'
surrogated = '\udcd0\udcba\udcd0\udcbe\udcd1\udc82 cat'
print(surrogated.encode(errors="surrogateescape")) # b'\xd0\xba\xd0\xbe\xd1\x82 cat'
print(surrogated.encode(errors="surrogatepass")) # b'\xed\xb3\x90\xed\xb2\xba\xed\xb3\x90\xed\xb2\xbe\xed\xb3\x91\xed\xb2\x82 cat'

#print(line.endswith("Ni!\n")) #Возвращает флаг, указывающий на то, заканчивается ли строка указанным постфиксом.
#my_str = 'Discworld'
#print(my_str.endwith("jockey")) # False

my_str = '\t1\t10\t100\t1000\t10000'
my_str.expandtabs() # Возвращает копию строки, в которой символы табуляций заменены пробелами.
my_str.expandtabs(4) # tabsize=8 : Максимальное количество пробелов на которое может быть заменена табуляция.

my_str = 'barbarian'
my_str.find("bar") # Возвращает наименьший индекс, по которому обнаруживается начало указанной подстроки в исходной.
my_str.find("bar", 1) # start=0 : Индекс начала среза в исходной строке, в котором требуется отыскать подстроку.
my_str.find('bar', 1, 2)  # -1, end=None : Индекс конца среза в исходной строке, в котором требуется отыскать подстроку.

print('{}-{}-{}'.format(1, 2, 3))  # '1-2-3'
'{}-{}-{}'.format(*[1, 2, 3])  # '1-2-3'
print("{one}-{two}-{three}".format(two=2,one=1,three=3))
print("{one}-{two}-{three}".format(**{"two":2,"one":1,"three":3}))  # '1-2-3'

class my_dict(dict):
    missing_default="space"
    def __missing__(self,key):
        return self.missing_default

my_str = 'kosmonavt fly to {where}'
print(my_str.format_map(my_dict()))
print(my_str.format_map(my_dict(where="tatarstan")))

my_str = 'barbarian'
my_str.index('bar')  # 0 Возвращает наименьший индекс, по которому обнаруживается начало указанной подстроки в исходной.

print("!@#".isalnum()) # Возвращает флаг, указывающий на то, содержит ли строка только цифры и/или буквы.
'abc123'.isalpha()  # False. Возвращает флаг, указывающий на то, содержит ли строка только буквы.
'1000'.isdecimal()  # True. Возвращает флаг, указывающий на то, содержит ли строка число в десятичной системе исчисления.

print(line)
print(line.rstrip()) # удаляют пробельные символы в конце текстовой строки
print(line.upper())
