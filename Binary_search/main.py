from utils import binary_search


def main():
    number_list = list(map(int, input("Enter the list of numbers: ").split()))
    value = int(input("Enter value to search: "))
    if binary_search(sorted(number_list), value):
        print(f"found at {number_list.index(value)}")
    else:
        print("not found")


if __name__ == "__main__":
    main()
