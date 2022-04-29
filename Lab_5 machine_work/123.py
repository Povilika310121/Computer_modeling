import numpy as np


def get_time_before_next_task():
    return round(np.random.exponential(1.), 2)


def get_time_before_machine_breakdown():
    return round(np.random.normal(20., 2.), 2)


def get_setting_machine():
    return round(np.random.uniform(.2, .5), 2)


def get_task_execution():
    return round(np.random.normal(.5, .1), 2)


def machine_work(kol_det, total_time_machine=0):
    details = kol_det
    kol_det_in_que = 0
    kol_brok = 0                                            # кол-во поломок станка
    time_before_next_task = get_time_before_next_task()     # время до следующего задания
    time_to_broke = get_time_before_machine_breakdown       # время до поломки станка
    while details > 0:
        if time_before_next_task > 0:                       # если есть время до след задания
            total_time_machine += time_before_next_task     # добавляем время ожидания задания
            time_before_next_task = 0

        set_machine = get_setting_machine()                 # настройка станка
        task_execution = get_task_execution()               # время выполненния задания
        time_one_task = set_machine + task_execution        # время отладки + выполнения

        if time_one_task < time_to_broke:                   # время отладки + выполнения меньше чем время до поломки
            time_before_next_task += get_time_before_next_task()
            total_time_machine += time_one_task             # общее время работы станка
            time_to_broke -= time_one_task                  #
            time_before_next_task -= time_one_task          # ???
            details -= 1                                    # задание выполнилось
        else:
            kol_brok += 1
            total_time_machine += time_to_broke             # общее время работы станка
            time_before_next_task -= time_to_broke
            repair_time = np.random.uniform(.1, .5)         # время устранение поломки станка
            total_time_machine += repair_time
            time_before_next_task -= repair_time
            time_to_broke = get_time_before_machine_breakdown()
    while time_before_next_task < 0:
        time_before_next_task += get_time_before_next_task()
        kol_det_in_que += 1
    return kol_brok, total_time_machine, total_time_machine / kol_det, kol_det_in_que


kol_tasks = 500
res = machine_work(kol_tasks)
print("__________________________________")
print(f'Количество заданий: {kol_tasks}\n'
      f'Количество поломок станка: {res[0]}\n'
      f'Время работы: {int(res[1]//1)} часов {int(res[1]%1*60//1)} мин.\n'
      f'Среднее время выполнение одного задания: {f"{int(res[2]%1*60//1)} мин." if (res[2] < 1) else f"{int(res[2]//1)} час {int(res[2]%1*60//1)} мин."}\n'
      f'Деталей в очереди (после выполнения 500 заданий): {res[3]}')
print("__________________________________")
