# 3. Задайте список из n чисел последовательности (1+1/n)**n 
# и выведите на экран их сумму.

def sequence_of_numbers(number):
    result = []
    sum = 0
    for i in range(1, number):
        result.append((1 + 1 / i)**i)
        print(result[i-1])
        sum += result[i-1]
    print(f"Сумма чисел = {sum}")

sequence_of_numbers(188)
