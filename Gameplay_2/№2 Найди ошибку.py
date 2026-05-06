class Monster:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Я {self.name}, и я хочу кушать!')


mon = Monster('Упырь')
mon.introduce()
