#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from functions.select import select
from functions.add import add
from functions.help import help
from functions.module_list import function_list


def main():
    '''
    Основная функция 
    '''
    routes = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            route = add()
            routes.append(route)

            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            function_list(routes)

        elif command.startswith('select '):
            select(routes, command)

        elif command == 'help':
            help()
            
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
