class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f'Монстр:{self.name}')
        print(f'HP:{self.hp}')
        print(f'DMG:{self.dmg}')
        print()


dracula = Monster("Дракула", 120, 35)
lycan = Monster("Люкан", 100, 40)
