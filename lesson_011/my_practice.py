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
def calc(line):
    # print(f'Read line {line}',flush = True)
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        print(f'Unknown operand{operation}')
    return value


total = 0
with open('python_snippets\calc.txt','r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc} в строке {line}')
            else:
                print(f'Не могу преобразовать к целому {exc}')



print(f' Total = {round(total,2)}')