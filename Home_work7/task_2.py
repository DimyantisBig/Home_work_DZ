stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_costs = {}
for item in stock:
    total_costs[item] = stock[item] * prices[item]
print(total_costs)

"""
total_cost = {}: Создаем пустой словарь, куда будем записывать общую стоимость каждого товара.

Цикл for item in stock:: Мы проходим по каждому товару в словаре stock 
(или prices, так как товары одинаковы в обоих словарях).

Вычисление стоимости: Для каждого товара находим общую стоимость, 
умножив количество на цену: stock[item] * prices[item].

Добавление в словарь: Результат сохраняется в итоговый словарь total_cost.
"""
