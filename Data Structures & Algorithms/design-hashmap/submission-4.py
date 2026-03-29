class MyHashMap:

    def __init__(self):
        self.table = {}

    def put(self, key: int, value: int) -> None:
        self.table[key]=value

    def get(self, key: int) -> int:
        return self.table[key] if key in self.table else -1

    def remove(self, key: int) -> None:
        if self.table.get(key):
            self.table.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)