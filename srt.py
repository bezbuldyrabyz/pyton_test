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
