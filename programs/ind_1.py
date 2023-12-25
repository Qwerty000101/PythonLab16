#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from module_outer import outer


if __name__ == "__main__":
    print(outer("max")([1,2,3,5,7,10]))
    print(outer("min")([1,2,3,5,7,10]))
    print(outer()([1,2,3,5,7,10]))