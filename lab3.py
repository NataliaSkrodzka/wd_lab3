# try:
# a = int(input())
# b = int(input())
# result = a/b
# print(result)
# except ZeroDivisionError:
# print("Error")
# except ValueError:
# print("Error")
# except Exception:
# print
# cos tam dalej
from math import *


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# for i in list1:
#     l2.append(pow(i, 2))
# print(l2)
# l3 = [3**y for y in range(0, 6)]
# print(l3)
# l4 = [x for x in l2 if x % 2 == 1]
# print(l4)
# l5 = [(x, y) for x in l3 for y in l4]
# print(l5)
# l6 = []
# for x in l3:
#     for y in l4:
#         l6.append((x, y))
# print(l6)
# s1 = {1: 2, 2: 3, 3: 4, 4: 5}
# s2 = {}
# for key, value in s1.items():
#     s2[value] = key
# print(s1)
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)
#
# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         print('jeden pierwiastek')
#         x = (-b + sqrt(delta)) / (2 * a)
#         return x
#     elif delta > 0:
#         print('dwa pierwiastki')
#         x1 = (-b - sqrt(delta)) / (2 * a)
#         x2 = (-b + sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 4, 2))
#
# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print(dlugosc_odcinka(4, 2, 6, 3))
# print(dlugosc_odcinka(y2=5, y1=5, x2=2, x1=8))
# print(dlugosc_odcinka(3, 5, y2=4, y1=3))
# plik = open('tekst.txt', 'r', encoding='utf-8')
# znaki = plik.read(10)
#
# linia = plik.readline()
# linie = plik.readlines(10)
# print(znaki)
# print(linia)
# # print(linie)
# for l in linie:
#     print(l)
# plik = open('tekst.txt', 'a+')
# plik.write('aaaaaaa')
# plik.seek(15)
# znaki = plik.read(10)
# print(znaki)
# plik.close()

with open('tekst.txt', 'r') as f:
    lines = f.readlines()

print(lines)

