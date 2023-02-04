
class WeirdObject:
    def work(self) -> None:
        print("Работает")


# Функция dependency_func() ожидает на вход объект класса WeirdObject:
def dependency_func(obj: WeirdObject) -> None:
    obj.work()

# Создаём объект класса WeirdObject
strange_item: WeirdObject = WeirdObject()

# А такая запись будет отмечена линтером как ошибка:
dependency_func(11)
# error: Argument 1 to "dependency_func" has incompatible type "int";
# expected "WeirdObject"
# "В функцию передано число, а мы-то ожидали объект класса WeirdObject!"