class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def show_info(self):
        print(f'- - - - Статистика - - - -')
        print(f'Имя: {self.name}')
        print(f'❤️: {self.hp}')
        print(f'⚔️: {self.dmg}')
        print('- - - - - - - - - - - - - -')


mon1 = Monster('Горгулья', 120, 18)
mon1.show_info()
