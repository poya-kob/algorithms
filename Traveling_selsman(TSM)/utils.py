from typing import List


def swap(_list: List, index1: int, index2: int):
    _list[index1], _list[index2] = _list[index2], _list[index1]
    return _list


def lexico_graphic(items: List):
    paths = [items]
    while True:
        # step 1
        largest_i = None
        for i in range(len(items) - 1):
            if items[i] < items[i + 1]:
                largest_i = i
        if largest_i is None:
            return paths

        # step 2
        largest_j = 0
        for j in range(len(items)):
            if items[largest_i] < items[j]:
                largest_j = j

        # step 3
        items = swap(items, largest_i, largest_j)

        # step 4
        items = items[:largest_i + 1] + items[:largest_i:-1]
        paths.append(items)


if __name__ == "__main__":
    print(lexico_graphic([0, 1, 2]))
