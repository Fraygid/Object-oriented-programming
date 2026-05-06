class Monster():
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0

    def is_alive(self):
        return True if self.__hp > 0 else False

    def show_status(self):
        print(f'{self.__name}, HP: {self.__hp}')

class Zombie(Monster):
    def __init__(self, hp, dmg):
        
