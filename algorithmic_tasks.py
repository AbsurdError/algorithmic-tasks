#///////////_1_Задача_////////////

# n = int(input('Введите число: '))
# i = 2
# res = 0
# while i <= n // 2:
#     if n % i == 0:
#         res += 1
#     i += 1
# if res <= 0:
#     print(True)
# else:
#     print(False)

#///////////_2_Задача_////////////

# n = [int(y) for y in input('Введите числа: ').split()]
# for i in range(0, len(n)):
#     for x in range(0, len(n) - (i + 1)):
#         if n[x] > n[x + 1]:
#             n[x], n[x + 1] = n[x + 1], n[x]
# print(f'Ответ:  {n}')

#///////////_2.2_Задача_////////////

# n = [int(y) for y in input('Введите числа: ').split()]
# i = 0
# while i < len(n):
#     x = 0
#     while x < len(n) - (i + 1):
#         if n[x] > n[x + 1]:
#             n[x], n[x + 1] = n[x + 1], n[x]
#         x += 1
#     i += 1
# print(f'Ответ:  {n}')

#///////////_3_Задача_////////////

# n = [int(i) for i in input('Введите числа:  ').split()]
# x = n[0]
# i = 1
# while i < len(n):
#     if n[i] > x:
#         x = n[i]
#     i += 1
# print(f'Максимальное число:  {x}')

#///////////_4_Задача_////////////

# n = int(input('Номер числа Фибоначчи: '))
# if n == 0:
#     print(0)
# else:
#     a = 0
#     b = 1
#     i = 2
#     while i <= n:
#         sum_ab = a + b
#         a = b
#         b = sum_ab
#         i += 1
#     print(f'Число Фибоначчи: {b}')

#///////////_5_Задача_////////////

# from collections import Counter
# hash_table = input('Введите строку:  ').split()
# take = Counter(hash_table)
# max_repetitions = take.most_common(1)[0][0]
# print(f"Наиболее часто встречающаяся строка: {max_repetitions}")

#///////////_5.2_Задача_////////////

# hash_table = input('Введите строку:  ').split()
# period = {}
# period_storage = 0
# max_period = 0
# for string in hash_table:
#     if string in period:
#         period[string] += 1
#     else:
#         period[string] = 1
#     if period_storage < period[string]:
#         period_storage = period[string]
#         max_period = string
# print(f"Наиболее часто встречающаяся строка: {max_period}")
