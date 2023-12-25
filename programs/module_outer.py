#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outer(type = "max"):
    '''
    Внешняя функция
    '''
    def inner(lst):
        '''
        Внутренняя функция
        '''
        if type == "max":
            return max(lst)
        
        else:
            return min(lst)
        
    return inner