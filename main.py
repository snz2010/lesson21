from my_class import Shop, Store, Request

if __name__ == '__main__':
# МАГАЗИН
    shop = Shop()
    shop.add("печеньки", 5)
    shop.add("вафли", 5)
    shop.add("помидоры", 5)
    shop.add("сок", 5)
# СКЛАД
    store = Store()
    store.add("печеньки_5", 5)
# ВВОД ПОЛЬЗОВАТЕЛЯ
    user_str = input("Введите запрос вида 'Доставить 5 печеньки_5 из склад в магазин':")
    user_str_list = user_str.split(" ")
    flag_error = False
# ----------------- БЛОК ПРОСТЕЙШИХ ПРОВЕРОК ---------------------
# ЧТО СДЕЛАТЬ
    if ("забрать" and "доставить") not in user_str_list[0].lower():
        print("введите 'забрать/доставить'")
        flag_error = True
# СКОЛЬКО
    try:
        user_str_list[1] = int(user_str_list[1])
    except:
        print("введите число товара")
        flag_error = True
# ОТКУДА
    if ("магазин" and "склад") not in user_str_list[4].lower():
        print("введите место забора товара (магазин ИЛИ склад)")
        flag_error = True
# КУДА
#     if "магазин" not in user_str_list[6].lower():
#         print("введите место доставки товара (магазин ИЛИ склад)")
#         flag_error = True
# ----------------- логика программы ---------------------
    if not flag_error:
        req = Request(user_str)
        print(req)
        if "магазин" in req.from_:
            print("Доставка возможна только со склада")
        elif "склад" in req.from_:
            if req.product in store.get_items():
                if req.amount <= store.get_items()[req.product]:
                    print("Нужное количество есть на складе")
                    print(f"Курьер забрал {user_str_list[1]} {user_str_list[2]} со склада")
                    if sum(shop.get_items().values()) + int(req.amount) <= shop.capacity:
                        print(f"Курьер везет {req.amount} {req.product} со склад в магазин")
                        store.remove(req.product, req.amount)
                        shop.add(req.product, req.amount)
                        print(f"Курьер доставил {req.amount} {req.product} в магазин")
                    else:
                        print(f"В магазине недостаточно места")
                else:
                    print(f"На складе недостаточно товара, попробуйте заказать меньше")
            else:
                print("Такого товара нет наскладе")

        print("В магазине хранится:")
        if shop.get_unique_items_count():
            for key, value in shop.items.items():
                print(key, value)
        else:
            print("магазин пуст")

        print("На складе хранится:")
        if store.get_unique_items_count():
            for key, value in store.items.items():
                print(key, value)
        else:
            print("склад пуст")
