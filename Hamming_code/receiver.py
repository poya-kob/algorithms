from typing import List
from dataclasses import dataclass
import numpy as np

from utils import ErrorHandler


@dataclass
class Receiver:
    blocks: List

    def __init__(self):
        self.blocks = []

    def blocks_creator(self, binary_list: List):
        for binary in binary_list:
            _list = [int(_) for _ in binary]
            _list = np.array(_list)
            self.blocks.append(_list.reshape((4, 4)))

        # for _ in range(len(_list)):
        #     self.blocks.append(np.array(_list[_]))
        #     self.blocks[_] = self.blocks[_].reshape((4, 4))

    def decoder(self):
        error_handler = ErrorHandler()
        for _ in range(len(self.blocks)):
            error_handler.q_error_finder(self.blocks[_])
            self.blocks[_] = error_handler.row_col_error_finder(self.blocks[_])
