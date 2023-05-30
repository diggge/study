animal = 'зайка'
def stutter(text):
    return text[:2] + '-' + text


def stutter_factory(n):
    def stutter(text):
        return (text[:2] + '-')*n + text
    return stutter


stutter_2=stutter_factory(2)

# print(stutter_2(animal))
# print(stutter_factory(100)(animal))
# Создать массив функций и применить все функции поочередно к аргументу
stutters = [stutter_factory(n=n) for n  in range(1,10)]
print(stutters)
animals = ['зайка', 'мишка', 'бегемотик']
for saakh in stutters:
    print(saakh(animal))
result = [saakh(animal) for saakh in stutters]
print(result)
animals = ['зайка', 'мишка', 'бегемотик']
mesh = [saakh(animal) for animal in animals for saakh in stutters]
print(mesh)

# //КОНЕЦ первой части
