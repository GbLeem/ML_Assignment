from random import random as rand



X = [rand() * i * 0.5 - 20 for i in range(0, 100)]
y = [x ** 3 * 0.002 - x ** 2 * 0.005 + x * 0.003 + rand() * 5 for x in X]

print(y)
print(max(y))

for i in range(10):
    print(i)

x = 2
print(x**0)