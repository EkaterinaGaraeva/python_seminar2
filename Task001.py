# 1. Реализовать алгоритм задания случайного числа без генератора случайных чисел

# import time
# seconds = int(time.time()*1000)
# print(seconds % 100)

from datetime import datetime
dt = datetime.now().microsecond
print(int(dt % 10 + 10)) # от 10 до 20

