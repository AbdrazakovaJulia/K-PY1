money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

spends = spend
month = 0  # количество месяцев, которое можно прожить
while money_capital >= spends:
    money_capital = money_capital + salary - spends
    month += 1
    spends = spend * (increase + 1) ** month
# TODO Оформить решение

print(month)
