class worker:
    def __init__(self,name,pay): # Инициализация при создании
        self.name=name # self – это сам объект
        self.pay=pay
    def last_name(self):
        return self.name.split()[-1] # Разбить строку по символам пробела
    def give_raise(self,percent):
        self.pay*=(1.0+percent) # Обновить сумму выплат

bob=worker("Bob Smith",50000) # Создаются два экземпляра и для каждого
sue = worker("Sue Jones",60000) # определяется имя и сумма выплат
print(bob.last_name())
sue.give_raise(.1)
print(sue.pay)
