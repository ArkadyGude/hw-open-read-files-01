# Задача №1
with open('recipes.txt') as f:
    data = f.read().split('\n\n')
dish_list = []
ingredients_list_total = []
for dish in data:
    dish = dish.replace('\n', '--')
    dish = dish.split('--')
    dish_name = dish[0]
    dish_list.append(dish_name)
    qty = dish[1]
    ingredients = (dish[2:])
    ingredient_list = []
    ingredients_list_total.append(ingredient_list)
    for item in ingredients:
        ingredient_dict = {}
        ingredient = item.split(' | ')
        ingredient_dict['ingredient_name'] = ingredient[0]
        ingredient_dict['quantity'] = ingredient[1]
        ingredient_dict['measure'] = ingredient[2]
        ingredient_list.append(ingredient_dict)

cook_book = dict(zip(dish_list, ingredients_list_total))
# print(cook_book, '\n')


# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        ingredients_list = cook_book.get(dish)
        for ingredient in ingredients_list:
            if ingredient['ingredient_name'] in shop_list_by_dishes:
                shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] += int(
                    ingredient['quantity']) * person_count

            else:
                shop_list_by_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(
                    ingredient['quantity']) * person_count}

    return shop_list_by_dishes


purchase = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2)
# print(purchase, '\n')


# Задача №3
files_list = ['1.txt', '2.txt', '3.txt']
list_dict = []
for file_name in files_list:
    with open(f'{file_name}',  encoding='utf-8') as file:
        file_dict = {}
        count = 0
        text = file.readlines()
        for line in text:
            count += 1
            file_dict['file'] = [f'{file_name}', count]
        list_dict.append(file_dict)

sorted_files = sorted(list_dict, key=lambda i: i['file'][1])

with open('final_file.txt', 'w', encoding='utf-8') as final_file:
    for i in range(len(sorted_files)):
        k = sorted_files[i]['file'][0]
        with open(f'{k}', encoding='utf-8') as file:
            text = file.read()
        final_file.write(f'{sorted_files[i]['file'][0]}\n{sorted_files[i]['file'][1]}\n{text}\n\n')
