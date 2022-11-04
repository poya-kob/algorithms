from typing import List


def binary_search(_sored_list: List, value: int):
    if len(_sored_list) == 1:
        return _sored_list[0] == value
    mid = len(_sored_list) // 2
    return binary_search(_sored_list[mid:], value) if value >= _sored_list[mid] else binary_search(_sored_list[:mid],
                                                                                                   value)
