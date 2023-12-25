#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add():
    '''
    Добавить маршрут
    '''
    name_start = input("Начальный пункт маршрута? ")
    name_end = input("Конечный пункт маршрута? ")
    number = int(input("Номер маршрута? "))

    route = {
            'name_start': name_start,
            'name_end': name_end,
            'number': number,
            }
    
    return route