class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp

zomb1 = Zombie('Мясник', 100)

dmg = int(input('Введите силу укуса: '))
remaining_hp = zomb1.bite(dmg)

print(f'Остаток здоровья: {remaining_hp}')
