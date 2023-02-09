zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0
for animal in zoo_pet_mass:
    print(animal, zoo_pet_mass[animal])
    total_mass += zoo_pet_mass[animal]
print('Общая масса животных', total_mass)

total_mass = 0
for animal, mass in zoo_pet_mass.items():
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)

total_mass = 0
for mass in zoo_pet_mass.values():
    print(mass)
    total_mass += mass
print('Общая масса животных', total_mass)