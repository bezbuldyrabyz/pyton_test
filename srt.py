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
