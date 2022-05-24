# 1. Реализовать алгоритм задания случайного числа без генератора случайных чисел

# import time
# seconds = int(time.time()*1000)
# print(seconds % 100)

# Вариант 1
from datetime import datetime
def randomize(min, max):
    rand = int(datetime.now().microsecond) % 100
    rand = rand * (max - min)//100 + min
    return rand

print(randomize(10, 20))

# Вариант 2
import time
def new_random(min, max):
    rnd = time.time()
    rnd = rnd - int(rnd)
    rnd = int(rnd * (max - min)) + min
    return rnd

print(new_random(50, 60))
