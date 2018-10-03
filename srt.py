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


print(line)
print(line.rstrip()) # удаляют пробельные символы в конце текстовой строки
print(line.upper())
print(line.isalpha()) # Вернёт True, если в строке хотя бы один символ и все символы строки являются буквами, иначе — False.
print(line.endswith("Ni!\n")) #Возвращает флаг, указывающий на то, заканчивается ли строка указанным постфиксом.
