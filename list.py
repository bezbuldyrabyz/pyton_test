# Таблица 8.1. Литералы списков и операции. page 255

l=[] # Пустой список
l=[0,1,2,3] # Четыре элемента с индексами 0..3
l=["abc", ["def","ghi"]] # Вложенные списки
l=list("spam") # Создание списка из итерируемого объекта.
l=list(range(-4,4)) # [-4, -3, -2, -1, 0, 1, 2, 3] - Создание списка из непрерывной последовательности целых чисел
len(l) # количество элементов в списке
l*3 # [-4, -3, -2, -1, 0, 1, 2, 3, -4, -3, -2, -1, 0, 1, 2, 3, -4, -3, -2, -1, 0, 1, 2, 3]
for i in l: print(i) # Обход в цикле, проверка вхождения
# l=l.append(4) # Методы: добавление элементов в списо
l.append(4)
l.extend([5,6,7])
# l.insert(8, 9)
l.index(1) # Методы: поиск
#l.count()
#l.sort() # Методы: сортировка, изменение порядка следования элементов на обратный
l.reverse()
#l.pop()
#l.remove(2)
l=[i**2 for i in range(5)] # Генераторы списков и отображение
print(l)
#print(map(ord,"spam"))


# Конкатенация. page 256

[1,2,3]+[4,5,6] # [1, 2, 3, 4, 5, 6]
["Ni!"]*4 # [‘Ni!’, ‘Ni!’, ‘Ni!’, ‘Ni!’]
str([1,2])+"34" # То же, что и “[1, 2]” + “34”
print([1,2]+list("34")) # То же, что и [1, 2] + [“3”, “4”]


# Итерации по спискам и генераторы списков. page 256

3 in [1,2,3] # Проверка на вхождение

for x in [1,2,3]:
    print(x,end=" ")

print()

res=[]
for c in "SPAM":
    res.append(c*4)
print(res)

print(list(map(abs,[-1,-2,0,1,2]))) # Функция map применяется к последовательности

l=["spam","Spam","SPAM!"]
l[1]="eggs"
l[0:2]=["eat","more"]
print(l)

# Методы списков

l.append("please")
l.sort()

l = ["abc", "ABD", "aBe"]
l.sort() # [‘ABD’, ‘aBe’, ‘abc’]
l.sort(key=str.lower) # [‘abc’, ‘ABD’, ‘aBe’]
l.sort(key=str.lower, reverse=True) # [‘aBe’, ‘ABD’, ‘abc’]
print(sorted([x.lower() for x in l], reverse=True))
l=[1,2]
l.extend([3,4,5]) # Добавление нескольких элементов в конец списка
print(l)
print(l.pop()) # Удаляет и возвращает последний элемент списка
print(l)
l.reverse()
print(l)
print(list(reversed(l)))

# стек

l=[]
l.append(1)
l.append(2)
print(l)
print(l.pop())
print(l)

l=["spam","eggs","ham"]
print(l.index("eggs"))
l.insert(1,"toast")
print(l)
l.remove("eggs")
print(l)
l.pop(1) # Удаление элемента в указанной позиции
print(l)

l=["SPAM!", "eat", "more", "please"]
print(l)
del l[0]
print(l)
del l[1:]
print(l)
