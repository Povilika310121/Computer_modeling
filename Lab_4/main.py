import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# производные из 1 задачи
# x'=-2x+4y, x(0)=3
def fun_x1(t, x, y):  # x(t)
    return -2 * x + 4 * y


# y'=-x+3y, y(0)=0
def fun_y1(t, x, y):  # y(t)
    return -x + 3 * y


# производные из 2 задачи
# x'=y, x(0)=2
def fun_x2(t, x, y):
    return y


# y'=2y, y(0)=2
def fun_y2(t, x, y):
    return 2 * y


# считает коэффициенты для двух функций (со страницы 11)
def delta(fun_x, fun_y, t, x, y, h):
    k1 = h * fun_x(t, x, y)
    l1 = h * fun_y(t, x, y)

    k2 = h * fun_x(t + h / 2, x + k1 / 2., y + l1 / 2.)
    l2 = h * fun_y(t + h / 2, x + k1 / 2., y + l1 / 2.)

    k3 = h * fun_x(t + h / 2, x + k2 / 2., y + l2 / 2.)
    l3 = h * fun_y(t + h / 2, x + k2 / 2., y + l2 / 2.)

    k4 = h * fun_x(t + h, x + k3, y + l3)
    l4 = h * fun_y(t + h, x + k3, y + l3)

    d_x = (k1 + 2. * k2 + 2. * k3 + k4) / 6.
    d_y = (l1 + 2. * l2 + 2. * l3 + l4) / 6.
    return d_x, d_y


def run_kut(fun_x, fun_y, x0, y0, h, t0):  # сам метод
    # начальные значения
    x = [x0]
    y = [y0]
    t = [t0]

    # заполнение массивов координат
    for i in range(20):
        d_x, d_y = delta(fun_x, fun_y, t0, x0, y0, h)
        x0 = x0 + d_x
        y0 = y0 + d_y
        t0 = t0 + h
        x.append(x0)
        y.append(y0)
        t.append(t0)

    return x, y, t


# точные значения 1 задания
def exactly_x1(t):
    return 4 * np.exp(-t) - np.exp(2 * t)


def exactly_y1(t):
    return np.exp(-t) - np.exp(2 * t)


# 2 задания
def exactly_x2(t):
    return np.exp(2 * t) + 1


def exactly_y2(t):
    return 2 * np.exp(2 * t)


# вычисление точных значений x(t), y(t)
def exactly_solution(exactly_x, exactly_y, t0):
    N = 100
    x, y = [], []
    t = np.linspace(t0, 2, N)
    for i in t:
        x.append(exactly_x(i))
        y.append(exactly_y(i))
    return x, y, t


# построение графиков
def make_graph(fun_x, fun_y, exactly_x, exactly_y, x0, y0, t0, title, lim1, lim2):
    x, y, t = run_kut(fun_x, fun_y, x0, y0, 0.1, t0)
    x1, y1, t1 = exactly_solution(exactly_x, exactly_y, t0)

    fig, ax = plt.subplots()
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.plot(t1, x1, label='Точное решение, x(t)', color="purple")
    ax.plot(t1, y1, label='Точное решение, y(t)', color="black")
    ax.plot(t, x, label='Метод Рунге-Кутта 4го порядка, x(t)', color="orange")
    ax.plot(t, y, label='Метод Рунге-Кутта 4го порядка, y(t)', color="green")

    plt.ylim(lim1, lim2)
    ax.legend(fontsize=12, ncol=2, facecolor='white', edgecolor='r', title_fontsize='14')

    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.title(title)
    plt.show()


make_graph(fun_x1, fun_y1, exactly_x1, exactly_y1, 3, 0, 0, "Задание 1", -10, 5)
make_graph(fun_x2, fun_y2, exactly_x2, exactly_y2, 2, 2, 0, "Задание 2", -2, 20)
