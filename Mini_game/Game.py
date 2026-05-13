import random

# ----- 1 ЭТАП -----

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
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print(f'{self.__name}, HP: {self.__hp}')

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp() - self.get_dmg())

# ----- 2 ЭТАП -----

class Zombie(Monster):
    def __init__(self, name='Зомби'):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f'{self.get_name()} теряет конечность! Получено: {damage} урона. HP: {self.get_hp()}')

class Vampire(Monster):
    def __init__(self, name='Вампир'):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        absorbed = damage - 5
        self.set_hp(self.get_hp() - absorbed)
        print(f'{self.get_name()} поглощает 5 единиц урона! Получено: {absorbed} урона. HP: {self.get_hp()}')

class Ghost(Monster):
    def __init__(self, name='Призрак'):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print(f'{self.get_name()} уклонился от удара! Получено: 0 урона. HP: {self.get_hp()}')
        else:
            self.set_hp(self.get_hp() - damage)
            print(f'{self.get_name()} пропускает удар сквозь себя! Получено: {damage} урона. HP: {self.get_hp()}')

class Werewolf(Monster):
    def __init__(self, name='Оборотень'):
        super().__init__(name, 100, 25)
        self._transformed = False

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f'{self.get_name()} получает удар! Получено: {damage} урона. HP: {self.get_hp()}')
        if self.get_hp() < 50 and not self._transformed:
            print(f'{self.get_name} трансформируется!')
            self._transformed = True
