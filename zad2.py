import random
lista1 = [random.randint(0, 120) for x in range(10) ]
print(lista1)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)