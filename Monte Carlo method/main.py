import random
import matplotlib.pyplot as plt
import numpy as np
import math

#Task 1

# function 1 (n = 1)
def f_1(cur_x):
    return round(10 * cur_x, 3)

# function 2 (n = 1)
def f_2(cur_x):
    return round(10 * (cur_x - 20) / -19, 3)

def inside_triangle(cur_x, cur_y):
    if cur_y < f_1(cur_x) and cur_y < f_2(cur_x):
        return True
    else:
        return False

def square_MK(M_points, N_points, a_rect, b_rect):
    return round(M_points * a_rect * b_rect / N_points, 3)

def print_graphics(x_points, y_points, a_rect, b_rect):
    # рисуем графики
    x = np.linspace(0, a_rect, num=100)  # Точки по которым строятся графики
    y_rect = np.linspace(0, b_rect, num=100)
    fig, ax = plt.subplots()

    plt.ylim(0, 12)

    my_f_1 = 10 * x
    my_f_2 = 10 * (x - 20) / - 19
    rect_x = [a_rect] * 100
    rect_y = [b_rect] * 100

    ax.plot(x, my_f_1, label=f"f(x) = 10 * x ", linewidth = 3)
    ax.plot(x, my_f_2, label=f"f(x) = 10 * (x - 20) / -19 ",  linewidth = 3)
    ax.plot(x, rect_y, linewidth = 3)
    ax.plot(rect_x, y_rect, linewidth = 3)

    ax.legend(fontsize=14,
              ncol=1,  # Количество столбцов
              facecolor='white',  # Цвет области
              edgecolor='black',  # Цвет грани
              title='Функции',  # Заголовок
              title_fontsize='18',  # Размер шрифта заголовка
              loc="upper right" # местонахождение
              )

    fig.set_figwidth(10)
    fig.set_figheight(10)

    for i in range(len(x_points)):
        if inside_triangle(x_points[i], y_points[i]):
            plt.scatter(x_points[i], y_points[i], s=20, color='blue')  # scatter - метод для нанесения маркера в точке
        else:
            plt.scatter(x_points[i], y_points[i], s=20, color='red')

    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.show()

# Task 2

def integral(cur_x):
    return np.sqrt(11 - np.power((np.sin(cur_x)), 2))

def under_int(cur_x, cur_y, ):
    if cur_y < integral(cur_x) and cur_y < integral(cur_x):
        return True
    else:
        return False

# Task 3

def is_in_circle(cur_x, cur_y):
    if 0 <= cur_x <= 2 and 0 <= cur_y <= 2:
        if math.pow(cur_x - 1, 2) + math.pow(cur_y - 1, 2) < 1:
            return True
        else:
            return False
    else:
        return False

def square_5(N_points, a_rect, intersect = [1, 10]):
    sum = 0
    step = a_rect / N_points
    print(f"\nStep: {step}")
    cur_x = 0
    for i in range(N_points):
        if cur_x <= intersect[0]:
            sum += f_1(cur_x)
            cur_x += step
        else:
            sum += f_2(cur_x)
            cur_x += step
    return round(a_rect / N_points * sum, 3)

def fun_task_2(cur_x):
    return round(math.sqrt(29 - 11 * math.pow((math.cos(cur_x)), 2)), 3)


def print_graphics_2(x_points, y_points, a_rect, b_rect):
    # рисуем графики
    x = np.linspace(0, a_rect, num=100)  # Точки по которым строятся графики
    y_rect = np.linspace(0, b_rect, num=100)
    fig, ax = plt.subplots()

    my_f_1 = np.sqrt(11 - np.power((np.sin(x)), 2))
    rect_x = [a_rect] * 100
    rect_y = [b_rect] * 100

    ax.plot(x, my_f_1, label=f"f(x) = sqrt(11 - sin^2(x))", linewidth = 3)
    ax.plot(x, rect_y, linewidth = 3)
    ax.plot(rect_x, y_rect, linewidth = 3)

    fig.legend(fontsize=13,
              ncol=1,  # Количество столбцов
              facecolor='white',  # Цвет области
              edgecolor='green',  # Цвет грани
              title='Функции',  # Заголовок
              title_fontsize='18',  # Размер шрифта заголовка
              loc="upper right" # местонахождение
              )

    fig.set_figwidth(12)
    fig.set_figheight(12)

    for i in range(len(x_points)):
        if under_int(x_points[i], y_points[i]):
            plt.scatter(x_points[i], y_points[i], s=20, color='blue')  # scatter - метод для нанесения маркера в точке
        else:
            plt.scatter(x_points[i], y_points[i], s=20, color='red')

    plt.axhline(y = 0, color = 'k')
    plt.axvline(x = 0, color = 'k')
    plt.show()


def print_graphics_3(x_points, y_points, a_rect, b_rect):
    # рисуем график
    x = np.linspace(0, 2 * np.pi, num=150)  # Точки по которым строится график
    y_rect = np.linspace(0, b_rect, num=150)
    fig, ax = plt.subplots()

    my_circle_x = 1 + np.cos(x)
    my_circle_y = 1 + np.sin(x)
    rect_x = [a_rect] * 150
    rect_y = [b_rect] * 150

    ax.plot(my_circle_x, my_circle_y, label=f"x = 1+cos(phi); y = 1+sin(phi)", linewidth = 3)
    ax.plot(y_rect, rect_y, linewidth = 3)
    ax.plot(rect_x, y_rect, linewidth = 3)

    fig.legend(fontsize=13,
              ncol=1,  # Количество столбцов
              facecolor='white',  # Цвет области
              edgecolor='green',  # Цвет грани
              title='Функции',  # Заголовок
              title_fontsize='18',  # Размер шрифта заголовка
              loc="upper right" # местонахождение
              )

    fig.set_figwidth(9)
    fig.set_figheight(9)

    for i in range(len(x_points)):
        if is_in_circle(x_points[i], y_points[i]):
            plt.scatter(x_points[i], y_points[i], s=20, color='blue')
        else:
            plt.scatter(x_points[i], y_points[i], s=20, color='red')  # scatter - метод для нанесения маркера в точке

    plt.axhline(y = 0, color = 'k')
    plt.axvline(x = 0, color = 'k')
    plt.show()


def ro_fun(cur_phi, A, B):
    return np.sqrt(A * np.power(np.cos(cur_phi), 2) + B * np.power(np.sin(cur_phi), 2))


def r_i(cur_x, cur_y):
    return np.sqrt(np.power(cur_x, 2) + np.power(cur_y, 2))


def phi_i(cur_x, cur_y):
    if cur_x > 0:
        return np.arctan(cur_y/cur_x)
    elif cur_x < 0:
        return np.pi + np.arctan(cur_y / cur_x)
    elif cur_x == 0 and cur_y > 0:
        return np.pi / 2
    elif cur_x == 0 and cur_y < 0:
        return - np.pi / 2
    elif cur_x == 0 and cur_y == 0:
        return 0
    else:
        return "Ошибка"


def is_in_polar(cur_x, cur_y, A, B):
    if r_i(cur_x, cur_y) < ro_fun(phi_i(cur_x, cur_y), A, B):
        return True
    else:
        return False


# Площадь фигуры #
print("* * * * Площадь фигуры * * * *\n")
n = 1

# пересечение f1 и f2 [x, y]
point_of_f1f2 = [1, 10]

# точка пересечения f1 и x, f2 и x
f1_x = 0
f2_x = 20

# прямоугольник (a - по x, b - по y)
a, b = f2_x, point_of_f1f2[1]
print(f"Длины сторон прямоугольника: {a}, {b}")


print("Введите N - количество точек: ")
N = int(input())

# создаем рандомные точки в пределах прямоугольника
rand_x = []
rand_y = []

for i in range(N):
    rand_x.append(round(random.uniform(0, a), 3))
    rand_y.append(round(random.uniform(0, b), 3))

# считаем кол-во точек рандомных, лежащих в треугольнике
M = 0
for i in range(N):
    M += 1 if inside_triangle(rand_x[i], rand_y[i]) else 0
print(f"M = {M}\n")

# вычисляем площадь
sq_MK = square_MK(M, N, a, b)
print(f"Площадь по 7 формуле: {sq_MK}")
print(f"Точная площадь: 100")

# рисуем график
print_graphics(rand_x, rand_y, a, b)

print("Продолжить?")
input()

# Task 2 #
print("* * * * Интеграл * * * *")

# прямоугольник - по х и у
# max по y - 3,3166 => можно взять прямоугольник 3.35
a_2, b_2 = 5, 3.35
print(f"Размер прямоугольника: {a_2}, {b_2}")

print("Введите количество точек N: ")
N = int(input())

# создаем рандомные точки в пределах прямоугольника
rand_x = []
rand_y = []

for i in range(N):
    rand_x.append(round(random.uniform(0, a_2), 3))
    rand_y.append(round(random.uniform(0, b_2), 3))

# считаем кол-во точек рандомных, лежащих под графиком
M = 0
for i in range(N):
    M += 1 if under_int(rand_x[i], rand_y[i]) else 0
print(f"M = {M}")

# вычисляем площадь
sq_MK = square_MK(M, N, a_2, b_2)
print(f"Площадь по 7 формуле: {sq_MK}")
print("Точная площадь: 16.168")


print_graphics_2(rand_x, rand_y, a_2, b_2)

print("Продолжить?")
input()
#_______________________________________________________
#Task 3
print("* * * * Pi * * * *")

# R = n = 1 прямоугольник - 2*R - 2
a_3, b_3 = 2, 2
print(f"Размер прямоугольника: {a_3}, {b_3}")

print("Введите количство точек N: ")
N = int(input())

# создаем точки в пределах прямоугольника
rand_x = []
rand_y = []

for i in range(N):
    rand_x.append(round(random.uniform(0, a_3), 3))
    rand_y.append(round(random.uniform(0, b_3), 3))

# считаем кол-во точек, лежащих под графиком
M = 0
for i in range(N):
    M += 1 if is_in_circle(rand_x[i], rand_y[i]) else 0
print(f"M = {M}")

my_pi = 4 * M / N
print(f"My PI = {my_pi}")
print("PI: 3,1415926535")

print_graphics_3(rand_x, rand_y, a_3, b_3)

print("Продолжить?")
input()
#________________________________________________________
# Task 4 #
print("* * * * Полярные координаты * * * * ")

# т.к. n = 11 >= 11:
n=1
A = 3
    # n + 11
B = 7
    # 11 - n

# [0; 2pi] - составили значения фи
phi = np.linspace(0, 2 * np.pi, num=150)

# определяем x и y
x_4 = []
y_4 = []
for i in range(len(phi)):
   x_4.append(ro_fun(phi[i], A, B) * np.cos(phi[i]))
   y_4.append(ro_fun(phi[i], A, B) * np.sin(phi[i]))

x_4_min = round(min(x_4), 3)
x_4_max = round(max(x_4), 3)
y_4_min = round(min(y_4), 3)
y_4_max = round(max(y_4), 3)

print(f"X min: {x_4_min}; X max: {x_4_max}\nY min: {y_4_min};  Y max: {y_4_max}")

print("Введите количество точек N: ")
N = int(input())

# создаем рандомные точки в пределах прямоугольника
rand_x = []
rand_y = []

for i in range(N):
    rand_x.append(round(random.uniform(x_4_min, x_4_max), 3))
    rand_y.append(round(random.uniform(y_4_min, y_4_max), 3))

M = 0
for i in range(N):
    M += 1 if is_in_polar(rand_x[i], rand_y[i], A, B) else 0
print(f"M = {M}")

sq_MK = square_MK(M, N, x_4_max - x_4_min, y_4_max - y_4_min)
print(f"Площадь по формуле: {sq_MK}")
print("Точная площадь: 15.708")


fig, ax = plt.subplots()

# график рисуем
ax.plot(x_4, y_4, label=f"ro^2 = {A}cos^2(phi) + {B}sin^2(phi)", linewidth = 3)

fig.legend(fontsize=13,
              ncol=1,  # Количество столбцов
              facecolor='white',  # Цвет области
              edgecolor='black',  # Цвет грани
              title='Функции',  # Заголовок
              title_fontsize='18',  # Размер шрифта заголовка
              loc="upper right" # местонахождение
              )

fig.set_figwidth(9)
fig.set_figheight(9)

# точки рисуем
for i in range(len(rand_x)):
    if is_in_polar(rand_x[i], rand_y[i], A, B):
        plt.scatter(rand_x[i], rand_y[i], s=20, color='blue')
    else:
        plt.scatter(rand_x[i], rand_y[i], s=20, color='red')

# прямоугольник рисуем
ax.plot([x_4_min, x_4_max, x_4_max, x_4_min, x_4_min], [y_4_max, y_4_max, y_4_min, y_4_min, y_4_max],  linewidth = 3)

plt.axhline(y = 0, color = 'k')
plt.axvline(x = 0, color = 'k')
plt.show()

