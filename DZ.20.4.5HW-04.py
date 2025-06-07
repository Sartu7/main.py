import json

with open("orders_july_2023.json", "r") as f:
    orders = json.load(f)

#1Какой номер самого дорого заказа за июль?
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
#2Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством товаров: {max_order}, количество товаров: {max_quantity}')
#3 В какой день в июле было сделано больше всего заказов?
date_counts = {}
for order_num, orders_data in orders.items():
    date = orders_data["date"]
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
most_popular_date = max(date_counts, key=date_counts.get)
print(f'Дата с наибольшим количеством заказов: {most_popular_date}, количество заказов: {date_counts[most_popular_date]}')
#4Какой пользователь сделал самое большое количество заказов за июль?
user_count = {}
for order in orders.values():
    user_id = order["user_id"]
    user_count[user_id] = user_count.get(user_id, 0) + 1
most_active_user = max(user_count, key=user_count.get)
print(f"Самое большое количество заказов у пользователя с ID {most_active_user}, количество заказов: {user_count[most_active_user]} штук")
#5У какого пользователя самая большая суммарная стоимость заказов за июль?
max_price = 0
user_total_price = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    user_id = orders_data["user_id"]
    if price > max_price:
        max_price = price
    user_total_price[user_id] = user_total_price.get(user_id, 0) + price
    max_user_price = max(user_total_price, key=user_total_price.get)
print(f"Пользователь с ID {max_user_price} имеет самую большую суммарную стоимость заказов {max_price}")
#6Какая средняя стоимость заказа была в июле?
prices = []
for order in orders.values():
    prices.append(order['price'])
    average_price = sum(prices) // len(prices)
print(f"Средняя стоимость заказа в июле: {average_price}")
#7Какая средняя стоимость товаров в июле?
total_price = sum(order["price"] for order_num, orders_data in orders.items())
# Подсчитываем количество заказов за июль
num_orders = len(orders)
# Вычисляем среднюю стоимость
average_price = total_price / num_orders
# Выводим результат
print(f"Средняя стоимость товаров в июле: {average_price} руб.")


