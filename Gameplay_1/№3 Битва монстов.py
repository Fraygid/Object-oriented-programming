class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f'Монстр:{self.name}')
        print(f'HP:{self.hp}')
        print(f'DMG:{self.dmg}')
        print()


line1 = input('Введите через пробел имя, здоровье, и урон монстра 1: ').split()
line2 = input('Введите через пробел имя, здоровье, и урон монстра 2: ').split()

monster1 = Monster(line1[0], int(line1[1]), int(line1[2]))
monster2 = Monster(line2[0], int(line2[1]), int(line2[2]))

while True:
    # Первая атака монстра1
    monster2.hp -= monster1.dmg
    if monster2.hp <= 0:
        monster2.hp = 0

    print(f'{monster1.name} наносит удар!')
    print(f'У {monster2.name} осталось {monster2.hp} HP')
    print()

    if monster2.hp == 0:
        print(f'Победил {monster1.name}')
        break

    # атака монстра2
    monster1.hp -= monster2.dmg
    if monster1.hp <= 0:
        monster1.hp = 0

    print(f'{monster2.name} наносит удар!')
    print(f'У {monster1.name} осталось {monster1.hp} HP')
    print()

    if monster1.hp == 0:
        print(f'Победил {monster2.name}!')
        break
