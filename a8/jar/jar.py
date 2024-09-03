class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be negative :(")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._capacity < n + self._size:
            raise ValueError("Not enough space in the jar :(")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Not enough cookies in the jar :(")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self): #getter
        return self._size
