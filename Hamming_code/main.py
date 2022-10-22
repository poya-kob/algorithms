from utils import FileHandler, data_splinter, binary_char
from sender import Sender
from receiver import Receiver


def main():
    data = input("enter your data:\n")
    sender = Sender()
    sender.encoder(data)
    sender.blocks_creator()

    message = ""
    for block in sender.blocks:
        _list = block.flatten(order="F")
        _list = _list.tolist()
        message += "".join([str(i) for i in _list])

    file_handler = FileHandler()
    file_handler.save("data.txt", message)
    file_data = file_handler.reader("data.txt")
    receiver = Receiver()
    receiver.blocks_creator(data_splinter(file_data))

    receiver.decoder()
    message = "".join(binary_char(block) for block in receiver.blocks)
    print(message)

if __name__ == '__main__':
    main()