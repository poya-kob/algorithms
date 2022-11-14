from random import randint as rnd


def create_random_list(length: int):
    return [rnd(0, length) for _ in range(length)]


def main():
    length = int(input("Enter length of list: "))
    _list = create_random_list(length)
    print(_list)
    for i in range(length - 1):
        flag = True
        for j in range(length - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
                flag = False
        if flag:
            break
    print(_list)


if __name__ == "__main__":
    main()
