ops = {
    '*': lambda x,y: x * y,
    '/': lambda x,y: x / y,
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '//': lambda x,y: x // y,
    '%': lambda x,y: x % y
}
def calc(line):
    # print(eval(line))
    # print(f'Read line {line}',flush = True)
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation in ops:
        func = ops[operation]
        value = func(operand_1,operand_2)
    else:
        raise ValueError(f'Unknown operand{operation}')
    return value

def get_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            if not line:
                continue
            line = line[:-1]
            yield line
total = 0
for line in get_lines(file_name='python_snippets\calc.txt'):
    try:
        total += calc(line)
    except ValueError as exc:
        if 'unpack' in exc.args[0]:
            print(f'Не хватает операндов {exc} в строке {line}')
        else:
            print(f'Не могу преобразовать к целому {exc}')

print(f' Total = {round(total,2)}')