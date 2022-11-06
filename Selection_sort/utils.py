from random import randint as rnd
from typing import List


def create_random_list(length: int):
    return [rnd(0, length) for _ in range(length)]


def selection_sort(numbers: List):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
