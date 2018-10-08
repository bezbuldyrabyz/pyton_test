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
