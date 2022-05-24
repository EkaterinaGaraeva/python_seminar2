# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def swing(N):
    result = []
    for i in range(0, N):
        result.append((-3)**i)
    return(result)

print(swing(5))


# Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

def findtext(element, text):
    count = 0 # счетчик вхождений
    i = 0 # счетчик элементов для цикла
    len_text = len(text) # длина строки текста поиска
    len_element = len(element) # длина искомой строки
    while i < (len_text-len_element-1):
        if element == text[i:i+len_element]:
            count +=1
            i = i + len_element
            print(f"Номер элемента вхождения в искомом тексте - {i}")
        else:
            i += 1
    return count

print(f"Число вхождений - {findtext('11', '4w95793094509234111117656757616717657657611')}")

def numSubString(lSourse, lSubstr):
    ret = 0
    i = 0
    while i != -1:
        i = lSourse.find(lSubstr, i+1)
        ret += 1
    return ret

a = 'Говорил попугай попугаю, я тебя попугай попугаю, отвечает ему попугай — Попугай, попугай, попугай!'
b = 'поп'

print(f'{numSubString(a, b)}')


# Подсчитать сумму цифр в вещественном числе.

def sum_elements(V):
    print(f'Входящее число V = {V}')
    sum_el = 0
    for i in str(V):
        if i.isdigit():
            sum_el += int(i)
    return sum_el

print(f'Сумма всех чисел входящего вещественного числа = {sum_elements(23.141)}')


# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def multirow(N):
    print(f'Входящее число N = {N}')
    array = [0 for i in range(N)]
    for k in range(0, N):
        if k == 0:
            array[k] = 1
        else:
            array[k] = array[k-1]*(k+1)
    return array

print(multirow(4))


