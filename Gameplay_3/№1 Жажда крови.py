class Vampire:
    def __init__(self, name, bloodlust):
        self.__name = name
        self.__bloodlust = bloodlust
        
    def get_bloodlust(self):
        return self.__bloodlust
        
    def set_bloodlust(self, value):
        if 0 <= value <= 100:
            self.__bloodlust = value
        else:
            print('Ошибка: уровень жажды крови должен быть от 0 до 100!')


vamp = Vampire('Камаэлла', 70)
vamp.set_bloodlust(150)
print(vamp.get_bloodlust())
