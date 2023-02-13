# a = 5
# b = 3
#
# nums = (a, b)
#
# character = {
#     'name': 'Mickey',
#     'class': 'cartoon character',
#     'age': 132
# }
#
# character['sex'] = 'male'
# character.pop('class')
#
# for (key, item) in character.items():
#     print(item)
#
# print(character)

# names1 = {'Pavel', 'Dmitry', 'Mihail', 'Dmitry'}
# names2 = {'Olga', 'Nataly', 'Dmitry'}
#
# n1 = names1.union(names2)
# n2 = names1.intersection(names2)
#
# print(names1)
# print(n2)

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3 or len(name) > 8 :
            print('Некорректная длина для атрибута!')
        else:
            self.__name = name
            print('Обновление атрибута name успешно завершено!')

    def __str__(self):
        return f'Всем привет! Меня зовут {self.__name} и мне {self.age} лет.'


class Worker(Human):
    def __init__(self, name, age, specialty = 'Unknown', xp = 0):
        super().__init__(name, age)
        self.specialty = specialty
        self.xp = xp

    def __str__(self):
        return super().__str__() + f'\nЯ работаю по специальности {self.specialty} уже {self.xp} лет. '


dima = Worker('Dmitry', 18, 'Programmer', 30)
pavel = Human('Pavel', 19)

print(dima)




