#!usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    a1, a2 = map(int, input("Укажите координаты точки A (a1, a2): ").split())
    b1, b2 = map(int, input("Укажите координаты точки B (b1, b2): ").split())

    OA_distance = math.sqrt(math.pow(a1 - 0, 2) + math.pow(a2 - 0, 2))
    OB_distance = math.sqrt(math.pow(b1 - 0, 2) + math.pow(b2 - 0, 2))

    if OA_distance > OB_distance:
        print("Точка A находится дальше от начала координат")
    elif OA_distance == OB_distance:
        print("Точки A и B находятся на одинаковом удалении от начала координат")
    else:
        print("Точка B находится дальше от начала координат")
