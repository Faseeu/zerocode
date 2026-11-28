from zerocode.core.doubly_linked_list import DoublyLinkedList


class LRUMap:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity should be >= 1")
        self._cap = capacity
        self._nodes = {}
        self._order = DoublyLinkedList()

    def __len__(self):
        return len(self._nodes)

    def __contains__(self, key):
        return key in self._nodes

    def get(self, key, default=None): ...

    def put(self, key, value) -> None: ...
