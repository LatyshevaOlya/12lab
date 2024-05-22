def zadanie1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.r_name = r_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.r_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.r_name} открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, r_name, cuisine_type, flavors):
            super().__init__(r_name, cuisine_type)
            self.flavors = flavors

        def list_flavors(self):
            print("Сорта мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    # Создание экземпляра IceCreamStand
    ice_cream_stand = IceCreamStand("Мороженое-мир", "Мороженое", ["мята с шоколадной крошкой", "Лимон", "Манго", "Клубника"])

    # Вызов методов
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.open_restaurant()
    ice_cream_stand.list_flavors()


def zadanie2():
    class Restaurant:
        def __init__(self, r_name, cuisine_type):
            self.r_name = r_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.r_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.r_name} открыт")

    class IceCreamStand(Restaurant):
        def __init__(self, r_name, cuisine_type, flavors, location, opening_hours):
            super().__init__(r_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.opening_hours = opening_hours

        def open_restaurant(self):
            super().open_restaurant()  # Вызов метода open_restaurant из базового класса
            print(f"Ресторан расположен по адресу: {self.location}")
            print(f"Ресторан работает по расписанию: {self.opening_hours}")

        def add_flavor(self, flavor):
            if flavor not in self.flavors:
                self.flavors.append(flavor)
                print(f"Сорт мороженого {flavor} добавлен.")
            else:
                print(f"Сорт мороженого {flavor} уже есть в списке.")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Сорт мороженого {flavor} удален.")
            else:
                print(f"Сорт мороженого {flavor} не найден.")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Сорт мороженого {flavor} есть в списке.")
            else:
                print(f"Сорт мороженого {flavor} нет в списке.")

        def list_flavors(self):
            print("Сорта мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def serve_ice_cream(self, flavor, type_of_ice_cream):
            if flavor in self.flavors:
                print(f"Сервируем {type_of_ice_cream} мороженое с вкусом {flavor}.")
            else:
                print(f"Сорт мороженого {flavor} нет в наличии.")

    # Создание экземпляра IceCreamStand
    ice_cream_stand = IceCreamStand("Мороженое-Мир", "Мороженое", ["мята с шоколадной крошкой", "Лимон", "Манго", "Клубника"],"Невский, 10", "9:00 - 21:00")

    # Вызов методов
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.open_restaurant()
    ice_cream_stand.list_flavors()
    ice_cream_stand.add_flavor("Вишня")
    ice_cream_stand.remove_flavor("Манго")
    ice_cream_stand.check_flavor("Шоколад")
    ice_cream_stand.serve_ice_cream("Клубника", "на палочке")

while True:
    print('1. IceCreamStand')
    print('2. IceCreamStand dop ')
    print('3. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        break
    else:
        print('Неверное действие')