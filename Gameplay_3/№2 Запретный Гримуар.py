class DarkEntity:
    def __init__(self, name, species, danger_level):
        self.__name = name
        self.__species = species
        self.__danger_level = danger_level


grimoire = DarkEntity('Балор', 'Высший вампир', 99)

print(f'Данные из гримуара:({grimoire._DarkEntity__name}, {grimoire._DarkEntity__species}, {grimoire._DarkEntity__danger_level})')
