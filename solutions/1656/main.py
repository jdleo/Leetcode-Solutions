class OrderedStream:
    def __init__(self, n: int):
        # empty slots at beginning, and also initial ptr at 0
        self.data = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        # 0 indexed
        id -= 1
        # set this slot
        self.data[id] = value
        # check if ptr doesnt reach new item
        if self.ptr < id: return []

        # increment ptr to next empty slot
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1

        # return slice from id to last non null object
        return self.data[id:self.ptr]