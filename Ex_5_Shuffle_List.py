# 5 Реализуйте алгоритм перемешивания списка.


def Shuffle_List(unshuffled_list):
    import random
    for i in range(len(unshuffled_list)):
        unshuffled_list.insert(random.randint(0,len(unshuffled_list)-1), unshuffled_list.pop(i))
    return unshuffled_list

list_length = int(input('Введите длину массива: '))
original_list = list(range(1, list_length + 1))
print(f'Исходный массив: {original_list}')
shuffled_list = Shuffle_List(original_list)
print(f'Перемешанный массив: {shuffled_list}')