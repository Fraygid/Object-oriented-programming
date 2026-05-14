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


# ----- 3 ЭТАП -----

class Weapon:
    def __init__(self, name):
        self.name = name

    def use(self, monster):
        pass

class SilverSword(Weapon):
    def __init__(self):
        super().__init__("Серебряный меч")
        self.damage = 30

    def use(self, monster):
        print(f"Охотник наносит удар {self.name}! ({self.damage} урона)")
        monster.take_damage(self.damage)

class HolyWater(Weapon):
    def __init__(self):
        super().__init__("Святая вода")
        self.damage = 20

    def use(self, monster):
        print(f"Охотник брызгает {self.name}! ({self.damage} урона)")
        monster.take_damage(self.damage)

class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__("Арбалет с болтом")
        self.damage = 25

    def use(self, monster):
        print(f"Охотник стреляет из {self.name}! ({self.damage} урона)")
        monster.take_damage(self.damage)


# ----- 4 ЭТАП -----

class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []

    def get_name(self):
        return self.__name
        
    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def add_weapon(self, weapon):
        self.__weapons.append(weapon)

    def get_weapon_count(self):
        return len(self.__weapons)

    def show_inventory(self):
        print(f"Инвентарь {self.__name}:")
        for i, w in enumerate(self.__weapons, 1):
            print(f"{i}. {w.name}")

    def attack(self, weapon_index, monster):
        if 0 <= weapon_index < len(self.__weapons):
            self.__weapons[weapon_index].use(monster)
        else:
            print("Неверный индекс оружия!")

    def is_alive(self):
        return self.__hp > 0


# ----- 5 ЭТАП -----

def run_game():
    hunter = Hunter("Ван Хельсинг")
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(CrossbowBolt())
    hunter.show_inventory()
    print("-" * 40)

    monsters = [
        Zombie("Зомби"),
        Vampire("Дракула"),
        Ghost("Призрак"),
        Werewolf("Оборотень")
    ]

    print(f"Начинаем зачистку замка! Впереди {len(monsters)} монстров.")
    print("=" * 40)

    for monster in monsters:
        print(f"Появляется {monster.get_name()}!")
        turn = 0
        
        while monster.is_alive() and hunter.is_alive():
            weapon_idx = turn % hunter.get_weapon_count()
            hunter.attack(weapon_idx, monster)

            if not monster.is_alive():
                print(f"{monster.get_name()} повержен!")
                break

            monster.attack_hunter(hunter)
            print(f"{hunter.get_name()} HP: {hunter.get_hp()}")

            if not hunter.is_alive():
                print(f"{hunter.get_name()} пал в бою!")
                break

            turn += 1
            print("-" * 30)

    print("\n" + "=" * 40)
    if hunter.is_alive():
        print("ПОБЕДА! Замок полностью зачищен от нечисти.")
    else:
        print("ПОРАЖЕНИЕ. Нечисть оказалась сильнее.")

run_game()
