from pprint import pprint
cook_book = {}
def cook_book_dict_maker(cook_book_readme):
    with open(cook_book_readme) as file:  # ДЗ 1
        for dish in file:
            list_book = []
            recipe_name = dish.strip()
            num = int(file.readline().strip())
            for item in range(num):
                ingr_list = file.readline().strip().split(' | ')
                test = {'ingredient_name': ingr_list[0], 'quantity': int(ingr_list[1]), 'measure': ingr_list[2]}
                list_book.append(test)
                cook_book.update({recipe_name: list_book})
            file.readline().strip()
    return cook_book
cook_book_dict_maker('Cook_Book.txt')

def dishes_for_person2(dishes, person_count):
    dict_for_shop = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in dict_for_shop:
                dict_for_shop[ingredient['ingredient_name']] = {'quantity': (ingredient['quantity']+ingredient['quantity']) * person_count,
                                                                'measure': ingredient['measure']}
            elif ingredient['ingredient_name'] not in dict_for_shop:
                dict_for_shop[ingredient['ingredient_name']] ={'quantity': ingredient['quantity'] * person_count,
                                                                 'measure': ingredient['measure']}
    return dict_for_shop
pprint(dishes_for_person2(['Фахитос','Омлет'],2))


# Мы его может сделать след образом
# def dishes_for_person(dishes, person_count):
#     dict_for_shop = {}
#     for dish in dishes:
#         # Здесь должна быть проверка на наличие блюда в книге рецептов. Если есть то проваливаемся в условие
#             for ingredient in ...: # здесь в цикле проходим по блюду в книге, получая при каждой итерации его ингредиент
#                 # Тут должен быть условный оператор в котором вы проверяете есть ли ингредиент в списке покупок.
#                 Если есть то увеличиваем его значение, если нету то создаем новый ключ с необходимым значением
#     return dict_for_shop
# pprint(get_shop_list_by_dishes(['Фахитос','Омлет'],1))
# Цикл здесь лишь для того чтобы пройтись по списку ингредиентов блюда, а увеличение происходит у ключа в словаре. Т.е.
# new_dict= {"a": 3}
# new_dict["a"] += 5 * 2
# # У вас получается {"a": 13}
