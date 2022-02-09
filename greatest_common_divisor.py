# Написать рекурсивную функцию 
# нахождения наибольшего общего делителя двух целых чисел.

def greatest_common_divisor(num_one, num_two):
    '''Функция нвхождения наибольшего общего делителя'''
    if (num_two == 0):
        return num_one
    return greatest_common_divisor(num_two, num_one % num_two)

first_num = int(input("Введите первое число:"))
second_num = int(input("Введите второе число:"))

GCD = greatest_common_divisor(first_num, second_num)

print("НОД:", GCD)