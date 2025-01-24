from pprint import pprint
import os
# Задание №1

def create_cook_book_dict(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        cook_book_dict = {}
        for line in file:
            recipe_name = line.strip()
            ingredients_count = file.readline()
            ingredients = []
            for p in range(int(ingredients_count)):
                recipe = file.readline().strip().split(' | ')
                product, quantity, word = recipe
                ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': word})
            file.readline()
            cook_book_dict[recipe_name] = ingredients
    return cook_book_dict

cook_book = create_cook_book_dict('recipes.txt')
pprint(cook_book)

# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish not in cook_book:
            print('Такого блюда нет в книге')
            continue
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += \
                    (int(ingredient['quantity']) * person_count)
                else:
                    result[ingredient['ingredient_name']] = ({'measure': ingredient['measure'],
                    'quantity': (int(ingredient['quantity']) * person_count)})
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание №3

def file_read(path, filename):
    if os.path.exists(f'{path}/{filename}'):
        with open(f'{path}/{filename}', 'r', encoding='utf-8') as file:
            file_lines_count = 0
            file_content = ''
            for line in file:
                file_content += line
                file_lines_count += 1
        return {'file_content': file_content, 'file_lines_count': file_lines_count}
    else:
        print('Нет такого файла')
        return False

print(file_read(f'{os.getcwd()}/sorted', '1.txt'))
print(file_read(f'{os.getcwd()}/sorted', '2.txt'))

def file_write(path_write_file , file_writing_name, file1_name, file2_name):
    file1 = file_read(f'{os.getcwd()}/sorted/', file1_name)
    file2 = file_read(f'{os.getcwd()}/sorted/', file2_name)
    if not file1 or not file2:
        print('Операция записи в файл невозможна!!!')
        return False
    with open(f'{path_write_file}/{file_writing_name}', 'w', encoding='utf-8') as file:
        if file1['file_lines_count'] < file2['file_lines_count']:
            file.write(f'{file1_name}\n{file1['file_lines_count']}\n{file1['file_content']}\n')
            file.write(f'{file2_name}\n{file2['file_lines_count']}\n{file2['file_content']}')
        else:
            file.write(f'{file2_name}\n{file2['file_lines_count']}\n{file2['file_content']}\n')
            file.write(f'{file1_name}\n{file1['file_lines_count']}\n{file1['file_content']}')

file_write(f'{os.getcwd()}/sorted/', '3.txt','1.txt', '2.txt')