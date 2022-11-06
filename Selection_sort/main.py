from utils import create_random_list, selection_sort


def main():
    _list = create_random_list(10)
    print("non sorted list = ", _list)
    print("sorted list = ", selection_sort(_list))


if __name__ == "__main__":
    main()
