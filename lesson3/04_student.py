# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
# TODO здесь ваш код
i=1
summa_money_parents=0
while i<=10:
    money_parents=expenses-educational_grant
    next_expenses=round(1.03*expenses,2)
    summa_money_parents=money_parents+summa_money_parents
    expenses = next_expenses
    i+=1
print('Студент должен попросить ', summa_money_parents, 'рублей')

