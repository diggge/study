y=4577
spisok_2=[y // 1000, y // 100 % 10, y // 10 % 10, y % 10]
if len(spisok_2)==len(set(spisok_2)):
    print('Список уникальный')
else:
    print('список не уникальный')
