import pandas as pd
import math
import numpy
import matplotlib.pyplot as plt

x = [1., 2., 3., 4., 5., 6.]
y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]

# поэлементно умножает 2 списка x_i*y_i+x_(i+1)*y_(i+1)+...
def sum_mult_list(l1, l2):
    return sum(list(map(lambda el_l1, el_l2: el_l1 * el_l2, l1, l2)))

def sum2_mult_list(l1, l2):
    return sum(l1)*sum(l2)

def method_Kramer_2(x, y):
    # Определитель а
    det_a = len(x) * sum_mult_list(x, y) - sum2_mult_list(x, y)
    # Определитель матрицы
    det = len(x) * sum_mult_list(x, x) - pow(sum(x), 2)
    a = det_a / det
    b = (sum(y) - a * sum(x)) / len(x)
    exp = round(sum(list(map(lambda el_x, el_y: pow((a * el_x + b - el_y), 2), x, y))), 6)
    return a, b, exp

def power_fun(x, y):
    ln_x = list(map(math.log, x))
    ln_y = list(map(math.log, y))
    a_ln_b = list(method_Kramer_2(ln_x, ln_y))
    a = a_ln_b[0]
    b = math.exp(a_ln_b[1])
    exp = round(sum(list(map(lambda el_x, el_y:
                       pow((b * pow(el_x, a) - el_y), 2), x, y))), 6)
    return a, b, exp

def exp_func(x, y):
    ln_y = list(map(math.log, y))
    a_lh_b = method_Kramer_2(x, ln_y)
    a = a_lh_b[0]
    b = math.exp(a_lh_b[1])
    exp = round(sum(list(map(lambda el_x, el_y: pow((b * math.exp(a * el_x) - el_y), 2), x, y))), 6)
    return a, b, exp

# функция проходит по всему массиву и каждый элемент возводит в указанную степень
def x_in_pow(x, degree):
    return list(map(lambda x: pow(x, degree), x))

def square_func(x, y):
    # матрица (левая часть системы)
    matr = numpy.array([
        [sum(x_in_pow(x, 4)), sum(x_in_pow(x, 3)), sum(x_in_pow(x, 2))],
        [sum(x_in_pow(x, 3)), sum(x_in_pow(x, 2)), sum(x)],
        [sum(x_in_pow(x, 2)), sum(x), len(x)]
    ])
    # вектор результатов (прававя часть системы)
    vect = numpy.array([
        sum_mult_list(x_in_pow(x, 2), y),
        sum_mult_list(x, y),
        sum(y)
    ])
    # numpy.linalg.solve решает матричное уравнение.
    koef = numpy.linalg.solve(matr, vect)
    a = koef[0]
    b = koef[1]
    c = koef[2]
    exp = round(sum(list(map(lambda el_x, el_y: pow((a * pow(el_x, 2) + b * el_x + c - el_y), 2), x, y))), 6)
    return a, b, c, exp

ar_x = numpy.arange(x[0], x[-1] + 0.1, 0.1)

def grafic_Kramer2(a, b):
    list_y = []
    for i in ar_x:
        list_y.append(a * i + b)
    return list_y

def grafic_power_fun(a, b):
    list_y = []
    for i in ar_x:
        list_y.append(b * pow(i, a))
    return list_y

def grafic_exponetional_func(a, b):
    list_y = []
    for i in ar_x:
        list_y.append(b * math.exp(a * i))
    return list_y

def grafic_square_func(a, b, c):
    list_y = []
    for i in ar_x:
        list_y.append(a * i * i + b * i + c)
    return list_y

lin_f = method_Kramer_2(x, y)
power_f = power_fun(x, y)
exp_f = exp_func(x, y)
sq_f = square_func(x, y)

print(f"Линейная: y = {round(lin_f[0], 2)} * x + {round(lin_f[1], 2)}")
print(f"Cтепенная: y = {round(power_f[1], 2)} * x^{round(power_f[0], 2)}")
print(f"Показательная: y = {round(exp_f[1], 2)} * e^({round(power_f[0], 2)} * x)")
print(f"Квадратичная: y = {round(sq_f[0], 4)} * x^2 + {round(sq_f[1], 2)} * x + {round(sq_f[2], 2)}")
print("*****Соответствующие суммарные погрешности*****")
print(f'Линейной: {lin_f[2]}')
print(f'Cтепенной: {power_f[2]}')
print(f'Показательной: {exp_f[2]}')
print(f'Квадратичной: {sq_f[3]}')

gr_lin_f = f'y = {round(lin_f[0], 2)} * x + {round(lin_f[1], 2)}'
gr_power_f = f'y = {round(power_f[1], 2)} * x^{round(power_f[0], 2)}'
gr_exp_f = f'y = {round(exp_f[1], 2)} * e^({round(power_f[0], 2)} * x))'
gr_sq_f = f'y = {round(sq_f[0], 4)} * x^2 + {round(sq_f[1], 2)} * x + {round(sq_f[2], 2)}'

# оси
axis = {
    'x': x,
    'y': y
}
func = { # numpy.arange (от, до,  шаг)
    'x': numpy.arange(x[0], x[-1] + 0.1, 0.1),
    gr_lin_f: grafic_Kramer2(lin_f[0], lin_f[1]),
    gr_power_f: grafic_power_fun(power_f[0], power_f[1]),
    gr_exp_f: grafic_exponetional_func(exp_f[0], exp_f[1]),
    gr_sq_f: grafic_square_func(sq_f[0], sq_f[1], sq_f[2]),
}
df1 = pd.DataFrame(data=axis)
df2 = pd.DataFrame(data=func)
# pd=pandas вывести 2 графика на одном
pd.concat([df1, df2])
# экспер. точки на графике
ax = df1.plot.scatter(x="x", y="y")
df2.plot.line(x="x", y=[gr_lin_f, gr_power_f, gr_exp_f, gr_sq_f], ax=ax)
plt.show()




