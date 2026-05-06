class BestiaryEntry:
    def __init__(self, name, species, age, weakness, habitat, loot):
        self.name = name
        self.species = species
        self.age = age
        self.weakness = weakness
        self.habitat = habitat
        self.loot = loot
    
    def is_private(self, field):
        messages = {
            'name': 'Имя чудовища скрыто во мраке!',
            'species': 'Вид существа больше не определить!',
            'age': 'Возраст монстра забыт в веках!',
            'weakness': 'Слабость существа теперь тайна!',
            'habitat': 'Место обитания стерто с карт!',
            'loot': 'Добыча надежно спрятана!'
        }
    
        if hasattr(self, field) and field in messages:
            value = getattr(self, field)
            
            private_name = f'_{self.__class__.__name__}__{field}'
            setattr(self, private_name, value)
            
            delattr(self, field)
            
            print(messages[field])


entry = BestiaryEntry("Фенрир", "Оборотень", 300, "Серебро", "Темный лес", "Волчья шкура")
entry.is_private('weakness')
entry.is_private('loot')
