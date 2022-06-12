# # Напишите декоратор text_decor, который оборачивает вызов декорированной функции
# # фразами «Hello» и «Goodbye!»: фраза
# # «Hello» печатается до вызова, фраза «Goodbye!» - после
#
# def text_decor(func):
#     def inner(*args, **kwargs):
#         print("Hello")
#         func(*args, **kwargs)
#         print('Goodbye!')
#     return inner
#
# @text_decor
# def simple_func():
#     print('I just simple python func')
# simple_func()
# print('-----')
# @text_decor
# def multiply(num1, num2):
#     print(num1 * num2)
# print(multiply(3,5))
#
# # Напишите декоратор repeater, который дважды вызывает декорированную функцию
#
# def repeater(func):
#     def inner (*args, **kwargs):
#         func(*args, **kwargs)
#     return inner
#
# @repeater
# def multiply(n1, n2):
#     print(n1 * n2)
# print('-----')
# multiply(2,7)
# multiply(5,3)
#
# # Напишите декоратор double_it, который возвращает удвоенный
# # результат вызова декорированной функции
#
# def double_it(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs) * 2
#     return inner
# print('----')
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
# print(multiply(9, 4))
#
# @double_it
# def get_sum(*args):
#     return sum(args)
# print(get_sum(1, 2, 3, 4, 5))

# # HT_13_4
# import random
#
#
# n,a,b = map(int,input().split())
#
# def rand_nums(n1,a1,b1):
#     l = []
#     for i in range(n):
#         r1 = random.randint(a, b)
#         l.append(r1)
#     return l
# print(rand_nums(n,a,b))




# # HT_13_5
#
# cafe = {'наполеон':[("масло, мука, сахар"),5,900],
#         'медовик':[("крем, мука, мед"),7,800],
#         'киевский':[("масло, корж, сгущенка"),9,700]}
# cake = input('Какой торт Вы хотели бы приобрести: ').lower()
# clarification = input('Что Вы хотели бы уточнить: ').lower()
# if clarification == 'описание':
#     how_much_cake: int = int(input('Сколько торта Вам положить: '))
#
# def f1(func):
#         def inner(*args, **kwargs):
#             if clarification == 'описание':
#                 print(f'Торт {cake} состоит из {cafe[cake][0]}')
#                 func(*args, **kwargs)
#                 print(f'К оплате {cafe[cake][1] * func(*args, **kwargs) / 100}')
#                 print(f'Торта {cake} осталось {cafe[cake][-1] - func(*args, **kwargs)}')
#                 cafe[cake][-1] -= how_much_cake
#             elif clarification == 'цена':
#                 func(*args, **kwargs)
#                 print(f'Торт {cake} стоит {cafe[cake][1]} руб')
#             elif clarification == 'количество':
#                 func(*args, **kwargs)
#                 print(f'Торт {cake} осталос {cafe[cake][2]} грамм')
#             elif clarification == 'купить':
#                 func(*args, **kwargs)
#                 print(f'Торт {cake} стоит {cafe[cake][1]} руб остаток {cafe[cake][2]} грамм')
#         return inner
# if clarification == 'описание':
#     def g(how_much_cake1):
#         return how_much_cake1
#     g = f1(g)
#     g(how_much_cake)
# else:
#     def g():
#         pass
#     g = f1(g)
#     g()

# # Hometask_13_6
# a = int(input())
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return factorial(n-1)*n
# print(factorial(a))











