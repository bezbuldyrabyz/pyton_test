# tuple

t= tuple("spam")
print(t)
print(t[0:2])
print(t*3)
print("spam" in t)
print((1,2)+(3,4))
t = (1, 2, 3, 4)
print(t[0],t[1:3])
x=(40)
print(x)

# Преобразования, методы и неизменяемость

t=("cc", "aa", "dd", "bb")
tmp=list(t)
print(tmp)
tmp.sort()
print(tmp)
t=tuple(tmp)
print(t)
sorted(t)
print(t)
t=(1, 2, 3, 4, 5)
l=[x+20 for x in t]
print(l)
t = (1, 2, 3, 2, 4, 2)
print(t)
print(t.index(2)) # Первое вхождение находится в позиции 2
print(t.index(2,2)) # Следующее вхождение за позицией 2
print(t.count(2)) # Определить количество двоек в кортеже
