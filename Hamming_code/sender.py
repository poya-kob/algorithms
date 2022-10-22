from typing import List
from dataclasses import dataclass

from utils import binary_convertor, block_creator, parity_bits_filler


@dataclass
class Sender:
    _binary_list: List
    blocks: List

    def __init__(self):
        self._binary_list = []
        self.blocks = []

    def encoder(self, string: str) -> None:
        self._binary_list = [binary_convertor(_) for _ in string]

    def blocks_creator(self) -> None:
        self.blocks = [block_creator(binary_code) for binary_code in self._binary_list]
        for _ in range(len(self.blocks)):
            self.blocks[_] = parity_bits_filler(self.blocks[_])
        # print(self.blocks)


if __name__ == '__main__':
    sender = Sender()
    sender.encoder('h')
    sender.blocks_creator()
