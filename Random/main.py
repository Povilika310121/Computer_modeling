import math
import random
import matplotlib.pyplot as plt
import numpy as np


# Метод квадратов
def method_square(num, n):
    random_number = np.array([])
    razr = len(str(num))
    for i in range(n):
        num_2 = str(pow(num, 2))
        while len(num_2) != razr * 2:
            num_2 = "0" + num_2
        if razr % 2 == 0:
            new_num = num_2[int(razr - razr / 2):int(razr + razr / 2)]
        else:
            new_num = num_2[int(razr - razr / 2):int(razr + razr / 2)]
        random_number = np.append(random_number, int(new_num) * pow(10, -razr))
        num = int(new_num)

    return random_number


# Метод произведений
def method_compasion(num, core, n):
    random_number = np.array([])
    razr = len(num)
    for i in range(n):
        num_2 = str(int(num) * core)
        while len(num_2) != razr * 2:
            num_2 = "0" + num_2
        if razr % 2 == 0:
            new_num = num_2[int(razr - razr / 2):int(razr + razr / 2)]                                   # Если четное число разрядов
        else:
            new_num = num_2[int(razr - razr / 2):int(razr + razr / 2)]
        random_number = np.append(random_number, int(new_num) * pow(10, -razr))
        num = num_2[-razr:]

    return random_number


# Kонгруэнтный метод
def congruent_method(num, multiplier, delit, n):
    random_number = np.array([])  # Массив полученных чисел
    razr = len(str(num))  # Разрядность числа
    for i in range(n):
        new_num = num * multiplier % delit  # Число на множитель и получаем остаток
        random_number = np.append(random_number, new_num * pow(10, -razr))
        num = new_num

    return random_number

def mix_congruent_method(num, multiplier, delit, a, n):
    random_number = np.array([])
    razr = len(str(num))
    for i in range(n):
        new_num = (num * multiplier + a) % delit
        random_number = np.append(random_number, new_num * pow(10, -razr))
        num = new_num

    return random_number

def create_hist(data):
    n, bin, patches = plt.hist(data, color='orange')
    return n, patches


# n = 8  # Количество повторений
# num = 1357  # Исходное число
# core = 5167  # Ядро
# multiplier = 1357  # Множитель
# delit = 5689  # Делитель
m = mix_congruent_method(1357, 1357, 9689, 1, 500)
m_1 = method_square(7153, 200)
m_2 = method_compasion(str(3729), 5167, 500)
m_3 = congruent_method(1357, 1357, 9689, 500)
# print(f"Метод квадратов:\n {m_1}")
# print(f"Метод умножения:\n {m_2}")
# print(f"Метод vультипликативный конгруэнтный:\n {m_3}")

create_hist(m)
plt.title('Смешанный конгруэнтный')
plt.show()
create_hist(m_2)
plt.title('Произведений')
plt.show()
create_hist(m_1)
plt.title('Квадратов')
plt.show()
create_hist(m_3)
plt.title('Конгруэнтный')
plt.show()
