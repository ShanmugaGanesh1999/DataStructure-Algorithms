class Heap:
    def __init__(self, what) -> None:
        self.array = []
        self.what = 1 if what == "max" else 0

    # O(log n)
    def insert(self, val) -> None:
        self.array.append(val)
        self.heapify()

    def heapify(self) -> None:
        i = len(self.array) - 1
        while i > 0:
            p = int((i - 1) / 2)  # binary
            if self.operation(self.array[i], self.array[p]):
                self.swap(i, p)
            i = p

    # O(log n)
    def remove(self) -> int:
        r = -1
        if len(self.array) > 0:
            r = self.array.pop(0)
            last = self.array.pop()
            self.array.insert(0, last)
            self.sink()
        return r

    def sink(self) -> None:
        i, l = 0, len(self.array)
        while True:
            c1, c2 = (i * 2) + 1, (i * 2) + 2
            swap = None
            if c1 < l:
                if self.operation(self.array[c1], self.array[i]):
                    swap = c1
            if c2 < l:
                if (swap == None and self.operation(self.array[c2], self.array[i])) or (
                    swap != None and self.operation(self.array[c2], self.array[c1])
                ):
                    swap = c2
            if swap == None:
                break
            self.swap(i, swap)
            i = swap

    # min heap is the priority queue
    def operation(self, i, j) -> bool:
        return i > j if self.what == 1 else i < j  # max or min comparison

    def swap(self, i, j) -> None:
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def print(self) -> None:
        print(self.array)


heap = Heap("max")
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.print()
heap.insert(55)
heap.print()
print("removing", heap.remove())
heap.print()
print("removing", heap.remove())
heap.print()
print("removing", heap.remove())
heap.print()

"""
max

[41, 39, 33, 18, 27, 12]
[55, 39, 41, 18, 27, 12, 33]
removing 55
[41, 39, 33, 18, 27, 12]
removing 41
[39, 27, 33, 18, 12]
removing 39
[33, 27, 12, 18]

------------------------------

min

[12, 27, 18, 41, 33, 39]
[12, 27, 18, 41, 33, 39, 55]
removing 12
[18, 27, 39, 41, 33, 55]
removing 18
[27, 33, 39, 41, 55]
removing 27
[33, 41, 39, 55]
"""
