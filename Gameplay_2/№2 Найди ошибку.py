class Monster:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Я {self.name}, и я хочу кушать!')


m = Monster('Упырь')
m.introduce()
