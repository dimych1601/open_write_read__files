from pprint import pprint

# Задание №1

with open('recipes.txt', 'r', encoding='UTF-8') as file:
    cook_book = {}
    for line in file:
        recepie_name = line.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients

pprint(cook_book)

# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],'quantity': (int(ingredient['quantity']) * person_count)}
        else:
            print('Такого блюда нет в книге')
    pprint(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
