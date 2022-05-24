# 3. Задайте список из n чисел последовательности (1+1.n)**n 
# и выведите на экран их сумму.

def sequence_of_numbers(number):
    result = 0
    sum = 0
    for i in range(1, number):
        result = (1 + 1 / i)**i
        print(round(result, 3))
        sum = sum + result
    print(round(sum, 3))

sequence_of_numbers(5)
