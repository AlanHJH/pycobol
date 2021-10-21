class WorkingStorage:
    def __init__(self, size : int) -> None:
        self.bytes : bytearray = bytearray(size)
        self.size : int = size

    def setValue(self, index : int, value : bytearray) -> None:
        for bit in value:
            self.bytes.insert(index, bit)
            index += 1

    def getValue(self, start : int, end : int) -> bytearray:
        return self.bytes[start:end]

    def copy(self, indexFrom : int, indexTo : int, size):   
        while size > 0:
            self.bytes[indexTo] = self.bytes[indexFrom]
            size -= 1
            indexFrom += 1
            indexTo += 1

    def print(self) -> None:
        print(self.bytes)    

    def clear(self) -> None:
        self.bytes.clear()    