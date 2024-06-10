# separate chaining
class Hash:
    def __init__(self) -> None:
        self.size = 53  # using prime will improve collision
        self.PRIME = 37
        self.table = [None] * self.size

    def __hash__(self, key: str) -> int:
        hash_code = 0
        for i in key:
            j = ord(i) - 96
            hash_code = (hash_code * self.PRIME + j) % self.size
        return hash_code

    # O(1)
    def set(self, key: str, value: any) -> None:
        hash_code = self.__hash__(key)
        if self.table[hash_code] is None:
            self.table[hash_code] = []
        for i, kv in enumerate(self.table[hash_code]):
            if kv[0] is key:
                del self.table[hash_code][i]
        self.table[hash_code].append((key, value))

    # O(1)
    def get(self, key: str) -> any:
        hash_code = self.__hash__(key)
        if self.table[hash_code] is None:
            return -1
        for k, v in self.table[hash_code]:
            if k is key:
                return v
        return -1

    def helper_list(self, is_keys: bool) -> list:
        values = []
        for i in self.table:
            if i is not None:
                for k, v in i:
                    if is_keys:
                        # if k not in values:  #mostly key won't be duplicate if so it'll overwrite the value in it
                        values.append(k)  # keys
                    else:
                        if v not in values:  # check for duplicates
                            values.append(v)  # values
        return values

    def values(self) -> list:
        return self.helper_list(False)

    def keys(self) -> list:
        return self.helper_list(True)

    def print(self) -> None:
        print(self.table)


table = Hash()
table.set("yellow", "1")
table.set("blue", "2")
table.set("black", "3")
table.set("orange", "4")
table.set("purple", "5")
table.set("green", "6")
table.set("red", "7")
table.set("red", "8")

print("orange: ", table.get("orange"))

print("values: ", table.values())
print("keys: ", table.keys())
# table.print()
