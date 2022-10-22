import numpy as np

_places = [[0, 3], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]


class FileHandler:

    def save(self, file_name: str, string_to_save: str) -> bool:
        try:
            with open(file_name, "w") as f:
                f.write(string_to_save)
            return True
        except Exception:
            return False

    def reader(self, file_name: str) -> str | bool:
        try:
            with open(file_name, "r") as f:
                return f.read()
        except Exception:
            return False


def binary_convertor(char: str):
    binary = bin(ord(char))[2:]
    return '0' * (11 - len(binary)) + binary


def parity_bits_filler(block):
    if (np.count_nonzero(block[:, 1]) + np.count_nonzero(block[:, 3])) % 2:
        block[0][1] = 1
    else:
        block[0][1] = 0
        # Q2
    if (np.count_nonzero(block[:, 2]) + np.count_nonzero(block[:, 3])) % 2:
        block[0][2] = 1
    else:
        block[0][2] = 0
        # Q3
    if (np.count_nonzero(block[1]) + np.count_nonzero(block[3])) % 2:
        block[1][0] = 1
    else:
        block[1][0] = 0
        # Q4
    if (np.count_nonzero(block[2]) + np.count_nonzero(block[3])) % 2:
        block[2][0] = 1
    else:
        block[2][0] = 0
    if np.count_nonzero(block) % 2:
        block[0][0] = 1
    return block


def block_creator(binary_string: str):
    block = np.zeros((4, 4), np.int8)
    for indx, val in enumerate(binary_string):
        row, col = _places[indx]
        block[row][col] = val
    # block = parity_bits_filler(block)
    return block


def data_splinter(data):
    return [data[_:_ + 16] for _ in range(0, len(data), 16)]


class ErrorHandler:
    _errors = [False, False, False, False]
    _row_error = None
    _col_error = None

    def q_error_finder(self, block):

        if (np.count_nonzero(block[1:, 1]) + np.count_nonzero(block[:, 3])) % 2 != block[0][1]:
            self._errors[0] = True
        if (np.count_nonzero(block[1:, 2]) + np.count_nonzero(block[:, 3])) % 2 != block[0][2]:
            self._errors[1] = True
        if (np.count_nonzero(block[1][1:]) + np.count_nonzero(block[3])) % 2 != block[1][0]:
            self._errors[2] = True
        if (np.count_nonzero(block[2][1:]) + np.count_nonzero(block[3])) % 2 != block[2][0]:
            self._errors[3] = True

    def _col_errors(self):
        if self._errors[0] and self._errors[1]:
            self._col_error = 3
        elif self._errors[0] and not self._errors[1]:
            self._col_error = 1
        elif not self._errors[0] and self._errors[1]:
            self._col_error = 2
        elif not self._errors[0] and not self._errors[1]:
            self._col_error = 0

    def _row_errors(self):
        if self._errors[2] and self._errors[3]:
            self._row_error = 3
        elif self._errors[2] and not self._errors[3]:
            self._row_error = 1
        elif not self._errors[2] and self._errors[3]:
            self._row_error = 2
        if not self._errors[2] and not self._errors[3]:
            self._row_error = 0

    def row_col_error_finder(self, block):
        if any(self._errors):
            print("error")
            self._row_errors()
            self._col_errors()
            block[self._col_error][self._row_error] = int(not block[self._col_error][self._row_error])
        return block


def binary_char(block):
    _str = ''.join(str(block[col][row]) for row, col in _places)
    _str = f'0b{_str}'
    _str = int(_str, 2)
    return chr(_str)
