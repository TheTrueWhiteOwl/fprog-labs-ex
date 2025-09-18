#! /usr/bin/env python

from math import sqrt

QUANTIDADE_NUMS = 5

print(f"Por favor insira {QUANTIDADE_NUMS} números reais")
nums = list()
for i in range(QUANTIDADE_NUMS):
    nums.append(int(input("> ")))

media = sum(nums) / QUANTIDADE_NUMS
standard_dev = sqrt(1/(QUANTIDADE_NUMS-1) * sum([(num - media)**2 for num in nums]))

print(f"media: {media}; standard deviation: {standard_dev}")
