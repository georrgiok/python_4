#Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
from decimal import *
import math
n = int(input("Floor round Pi. Input N: "))

def roundDecToMin(i, z):
    return math.floor(i * 10**z) * 10 ** (-z)

print(roundDecToMin(Decimal(22)/Decimal(7), n))
