# # 13_1
# n = [int(i) for i in input().split()]
# def f(ls):
#     a = []
#     summ_n = 0
#     for i in ls:
#         while i > 0:
#             l_n = i % 10
#             summ_n += l_n
#             i = i // 10
#         a.append(summ_n)
#         summ_n = 0
#     a.sort()
#     return a
# print(f(n))

# # 13_2
a = float(input())
def f(x):
    if a <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < a <= 2:
        return -(x / 2)
    elif a > 2:
        return (x - 2) ** 2 + 1
print(f(a))
# a = float(input())
# if a <= -2:
#     def f(x):
#         return 1-(x + 2)**2
#     print(f(a))
# elif -2 < a <= 2:
#     def f(x):
#         return -(x/2)
#     print(f(a))
# elif a > 2:
#     def f(x):
#         return (x - 2)**2 + 1
#     print(f(a))

# # HT_13_3
# a = [int(i) for i in input().split()]
# print(a)
# def f(x):
#     t = tuple(x)
#     for i in range(len(t)):
#         if t[i] % 2 == 0:
#             x[x.index(t[i])] = t[i] // 2
#         else:
#             x.remove(t[i])
#     return x
# print(f(a))













