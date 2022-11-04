from typing import List
from random import randint as rnd
import numpy as np
import cv2


def draw_cities(img, cities_locations):
    for x, y in cities_locations:
        img = cv2.circle(img, (x, y), 6, (0, 0, 255), -1)
    return img


def draw_path(img, path, color):
    for i in range(len(path) - 1):
        img = cv2.line(img, path[i], path[i + 1], color, 2)
    return img


def city_randomizer(total_city_number: int, area_height: int, area_width: int):
    offset = 20
    city = set()
    while len(city) < total_city_number:
        city_location = (rnd(offset, area_width - offset), rnd(offset, area_height - offset))
        city.add(city_location)
    return city


def cities_converter(path, cities_locations: List):
    return [cities_locations[i] for i in path]


def distance_calculator(path):
    return sum(
        np.sqrt((path[i][0] - path[i + 1][0]) ** 2 + (path[i][1] - path[i + 1][1]) ** 2) for i in range(len(path) - 1))


def lexico_graphic(number_of_city: int):
    def swap(_list: List, index1: int, index2: int):
        _list[index1], _list[index2] = _list[index2], _list[index1]
        return _list

    items = list(range(number_of_city))
    cpy = items.copy()
    yield items
    while True:
        # step 1
        largest_i = None
        for i in range(len(items) - 1):
            if items[i] < items[i + 1]:
                largest_i = i
        if largest_i is None:
            break

        # step 2
        largest_j = 0
        for j in range(len(items)):
            if items[largest_i] < items[j]:
                largest_j = j

        # step 3
        items = swap(items, largest_i, largest_j)

        # step 4
        items = items[:largest_i + 1] + items[:largest_i:-1]
        yield items
    yield cpy


if __name__ == "__main__":
    # print(lexico_graphic([0, 1, 2]))
    print(city_randomizer(5, 500, 500))
