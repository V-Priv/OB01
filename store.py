class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def info(self):
        print(f"В магазине {self.name} по адресу: {self.address}")
        if self.items:
            print("Список товаров и их цены:")
            for item_name, price in self.items.items():
                print(f"{item_name}: {price}р")
        else:
            print("Товары отсутствуют.")

store = Store("У дома", "ул. Первая, 10")
store1 = Store("Дикси", "ул. Фруктовая, 12")
store2 = Store("Фермер", "ул. Светлая, 17")

store.add_item("Яблоки", 100)
store.add_item("Бананы", 150)
store1.add_item("Картофель", 50)
store1.add_item("Лук", 30)
store2.add_item("Говядина", 500)
store2.add_item("Баранина", 700)

store.info()
store1.info()
store2.info()

store.update_price("Яблоки", 50)
store.update_price("Бананы", 200)
store1.update_price("Картофель", 70)
store1.update_price("Лук", 40)
store2.update_price("Говядина", 700)
store2.update_price("Баранина", 900)

store.remove_item("None")
store.remove_item("None")
store1.remove_item("None")
store1.remove_item("None")
store2.remove_item("None")
store2.remove_item("None")

print(f"После обновления цен и наличия:")

store.info()
store1.info()
store2.info()

