zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    letters_count += len(animal)
    pass
print('Всего букв', letters_count)
