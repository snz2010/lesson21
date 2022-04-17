from abc import ABC, abstractmethod

class Storage(ABC):
    # `items`(словарь название: количество)
    # `capacity`
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

# СКЛАД
class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        flag_found = False
        # при наличии возможности - добавим товар
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] +count
                    flag_found = True
            if not flag_found:
                self.items[name] = count
            print(f"Товар ={name}({count})= добавлен")
        else: # иначе - сообщим, почему это не удалось
            if self.get_free_space() != 0:
                print(f"Нельзя добавить товар, можно добавить только {self.get_free_space()} товаров")
            else:
                print("Нельзя добавить товар, т.к. место закончилось")

    def remove(self, name, count):
        flag_found = False
        for key in self.items.keys():
            if name == key:
                flag_found = True
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Товара {name} недостаточно на СКЛАДе!")
        if not flag_found:
            print(f"{name} - нет на складе")

        if flag_found and self.items[name] == 0:
            del self.items[name]

    def get_free_space(self):
        return self.capacity - sum( self.items.values() )

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len( self.items.keys() )

class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 50
        self._limit = limit

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_free_space() >= count:
            if self.get_unique_items_count() <= self._limit:
                super().add(name, count)
            else:
                print(f"Товар ={name}({count})= не может быть добавлен (ЛИМИТ магазина = {self.get_item_limit()})")
        else:
            print(f"В магазине нет свободных полок для товара {name}")

class Request:
    def __init__(self, str):
        lst = self.get_info(str)

        self.from_ = lst[4]
        if len(lst) > 6:
            self.to = lst[6]
        else:
            self.to = None
        self.amount = int(lst[1])
        self.product = lst[2]


    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):  #    lst[1]                  lst[2]                lst[4]           lst[6]
        return f'amount= {self.amount} product= {self.product} from= {self.from_} to= {self.to}'


