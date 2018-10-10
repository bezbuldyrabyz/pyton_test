d={} # Пустой словарь
d={"spam":2,"eggs":3} # Словарь из двух элементов
print("eggs" in d)
d={"food":{"ham":1,"egg":2}} # Вложение
print(d["food"]["ham"])
d=dict(name="Bob",age=40) # Альтернативные способы создания словарей
#d=dict(zip(keyslist, valslist))
#d=dict.fromkeys(["a","b"])
print(d.keys())
print(d.values())
print(d.items()) # список ключей и значений
d.copy()
#d.get(key,default) # получение значения по умолчанию
print(len(d))
print(list(d.keys()))


# Базовые операции над словарями

d={"spam":2,"ham":1,"eggs":3}
print(len(d))
print(d)
d["ham"]=["grill","bake","fry"]
print(d)
del d["eggs"]
print(d)
d["brunch"]="Bacon"
print(d)

# Дополнительные методы словарей

print(list(d.items()))
print(d.get("spam"))
print(d.get("toast")) # Ключ отсутствует в словаре
print(d.get("toast",88))
print(d)

d2={"toast":4,"muffin":5}
d.update(d2) # Метод update реализует своего рода операцию конкатенации для словарей
print(d)
d.pop("muffin") # метод pop удаляет ключ из словаря и возвращает его значение
print(d)
d.pop("toast")

l=["aa","bb","cc","dd"]
l.pop() #Удаляет и возвращает последний элемент списка
print(l)
l.pop(1) # Удаляет и возвращает элемент из заданной позиции
print(l)


# Таблица языков

table={"Python":"Guido van Rossum","Perl":"Lary Wall","Tcl":"John Ousterhout"}

language="Python"
creator=table[language]
print(creator)
for i in table:
    print(i,"\t",table[i])

# Использование словарей для имитации гибких списков

l=[]
# l[99]="spam" # error
d={}
d[99]="spam" # При использовании целочисленных ключей словари могут имитировать списки, которые увеличиваются при выполнении операции присваивания по смещению:
print(d[99])
print(d)

# Использование словарей для структур разреженных данных

matrix={}
matrix[(2,3,4)]=88
matrix[(7,8,9)]=99
x=2; y=3; z=4 # символ ; отделяет инструкции
print(matrix[(x,y,z)])
print(matrix)

# Как избежать появления ошибок обращения к несуществующему ключу

if(2,3,6) in matrix:
    print(matrix[(2,3,6)])
else:
    print(0)

try:
    print(matrix[(2,3,6)])
except KeyError:
    print(0)

print(matrix.get((2,3,4),0)) # Существует; извлекается и возвращается
print(matrix.get((2,3,6),0)) # Отсутствует; используется аргумент default

# Использование словарей в качестве «записей»

rec={}
rec["name"]="mel"
rec["age"]=45
rec["job"]="trainer/write"
mel={"name":"Mark",
    "jobs":["trainer","writer"],
    "web":"www.rmi.net/lutz",
    "home":{"state":"CO","zip":80513}}
mel["name"]
print(mel["jobs"][1])


# Представления словарей

d = dict(a=1, b=2, c=3)
k=d.keys()
print(k)
v=d.values()
print(v)
print(list(v))
print(list(d.items()))

for i in d.keys(): print(i)
for i in d:print(i) # В итерациях по-прежнему не обязательно вызывать метод keys()

d={"a":1,"b":2,"c":3}
print(d)
del d["b"]
print(d)
print(list(d))
