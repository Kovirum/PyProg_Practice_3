#!usr/bin/env python3
# -*- coding: utf-8 -*-

TOTAL_PAWS = 64

if __name__ == '__main__':
    for c, i in enumerate(range(0, TOTAL_PAWS + 1, 4), 1):
        goose_count = (TOTAL_PAWS - i) // 2
        rabbit_count = (TOTAL_PAWS - goose_count * 2) // 4

        print(f"[#{c}] Гусей - {goose_count}, Кроликов - {rabbit_count}. "
              f"Лап: {goose_count * 2} + {rabbit_count * 4} = {goose_count * 2 + rabbit_count * 4}")
