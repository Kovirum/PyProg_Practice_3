#!usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    c = int(input("Введите число C такое, что |C| < 9: "))

    if not abs(c) < 9:
        print("Число C должно соответствовать условию: |C| < 9", file=sys.stderr)
        exit(1)

    result_str = ""

    if c < 0:
        result_str += "минус "
    match abs(c):
        case 0:
            result_str += "ноль"
        case 1:
            result_str += "один"
        case 2:
            result_str += "два"
        case 3:
            result_str += "три"
        case 4:
            result_str += "четыре"
        case 5:
            result_str += "пять"
        case 6:
            result_str += "шесть"
        case 7:
            result_str += "семь"
        case 8:
            result_str += "восемь"
        case 9:
            result_str += "девять"

    print(result_str)
