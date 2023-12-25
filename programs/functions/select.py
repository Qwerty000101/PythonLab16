#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(routes, command):
    '''
    Вывести выбранные маршруты
    '''
    parts = command.split(' ', maxsplit=1)
    station = parts[1]
    count = 0

    for route in routes:
        if (station == route["name_start"].lower() or
            station == route["name_end"].lower()):

            count += 1
            print('{:>4}: {}-{}, номер маршрута: {}'.format(count,
                  route["name_start"], route["name_end"], route["number"]))

    if count == 0:
        print("Маршрут не найден.")
