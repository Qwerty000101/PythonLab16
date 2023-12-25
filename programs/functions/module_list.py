#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def function_list(routes):
    '''
    Вывести список маршрутов
    '''
    if routes:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 30,
                '-' * 8
                )
        print(line)

        print('| {:^4} | {:^30} | {:^30} | {:^8} |'.format(
                "№",
                "Начальный пункт",
                "Конечный пункт",
                "Номер"
                )
              )
        print(line)

        for idx, route in enumerate(routes, 1):
            print('| {:>4} | {:<30} | {:<30} | {:>8} |'.format(
                    idx,
                    route.get('name_start', ''),
                    route.get('name_end', ''),
                    route.get('number', 0)
                    )
                    )
            print(line)
    else:
        print("Список работников пуст.")
