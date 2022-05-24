# 2. Реализуйте алгоритм перемешивания списка

import random

list_of_numbers = [1, 2, 3, 4]
random.shuffle(list_of_numbers)
print(list_of_numbers)


# Вариант 2

import time
def new_random(min, max):
    rnd = time.time()
    rnd = rnd - int(rnd)
    rnd = int(rnd * (max - min)) + min
    return rnd

spisok = [ 1, 4, 98, 'sddsd', True, 'rrr', False]
size = len(spisok)
print(size)
new_spisok = []
print(spisok)
while size > 0:
    index = new_random(0, size)
    new_spisok.append(spisok[index])
    spisok.pop(index)
    size -= 1
print(new_spisok)
