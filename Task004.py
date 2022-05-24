# 4. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число
# ['geek', 'brains4', '5five', '3friends']

def find_in_list(str_list, number):
    s = "".join(str_list)
    # s = ''
    # for i in range(0, len(str_list)):
        # s += str_list[i]

    if s.find(number) > 0:
        print(f"В списке есть число {number}")
    else:
        print(f"В списке нет числа {number}")

def find_digital(N, list):
    for i in list:
        for k in i:
            if (k.isdigit()) and (int(k) == N):
                return("есть")
    return("отсутствует")


text_list = [ 'geek', 'brains4', '5five', '3friends' ]

symbol = str(5)
find_in_list(text_list, symbol)

num = 5
print(f"Искомое число в массиве {find_digital(num, text_list)}")