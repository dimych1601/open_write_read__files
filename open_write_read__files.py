from pprint import pprint

with open('recipes.txt', encoding='UTF-8') as file:
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