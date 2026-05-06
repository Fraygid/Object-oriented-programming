class Monster:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp

    def mutate(self):
        self.power += 5
        print(f'{self.name} мутирует! Сила увеличена!')
        print(f'⚔️: {self.power}')

    def rest(self):
        self.hp += 10
        print(f'{self.name} отдыхает в склепе! Здоровье увеличено!')
        print(f'❤️: {self.hp}')


lycan = Monster('Lycan', 15, 90)
lycan.mutate()
lycan.rest()
