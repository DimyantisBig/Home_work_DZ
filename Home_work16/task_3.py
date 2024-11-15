class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add (self,product,amount):  # Получаем название товара
        product_name = product.name

        if product_name in self.products:  # Проверяем, есть ли уже такой товар
            self.products[product_name] += amount
        else:
            new_price = product.price * 1.3  # Добавляем новый товар с учетом надбавки
            self.products[product_name] = {'quantity': amount, 'price': new_price, 'type': product.type}

    def set_discount (self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            if identifier in self.products:
                self.products[identifier]['price'] *= (1 - percent / 100)
            else:
                print('Product not found.')

    def sell_product (self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]['quantity'] >= amount:
                self.products[product_name]['quantity'] -= amount
                self.income += self.products[product_name]['price'] * amount
            else:
                print(f'Not enough product {product_name} in stock')
        else:
            print(f'Product {product_name} not found')

    def get_income (self):
        return self.income

    def all_product (self):
        return self.products

    def get_product_info (self, product_name):
        if product_name in self.products:
            return self.products[product_name]
        else:
            return f'Product not found'


# Создаем товар и магазин
product = Product(type='electronics', name='laptop', price=1000)
store = ProductStore()

# Добавляем товар в магазин с количеством 10
store.add(product, 10)
print('Products after adding:', store.all_product())  # Проверяем добавление

# Устанавливаем скидку 20% для товара с именем 'laptop'
store.set_discount('laptop', 20)
print('Products after discount:', store.all_product())  # Проверяем цену после скидки

# Продаем 3 единицы товара 'laptop'
store.sell_product('laptop', 3)
print('After Sales Items:', store.all_product())  # Проверяем количество после продажи
print('Current income:', store.get_income())  # Проверяем доход после продажи

# Проверяем информацию о товаре 'laptop'
print('Product information laptop:', store.get_product_info('laptop'))

# Проверяем информацию о несуществующем товаре
print('Product information phone:', store.get_product_info('phone'))





