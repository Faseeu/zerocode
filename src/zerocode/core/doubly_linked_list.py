class Node:
    __slots__ = ("next", "prev", "value")

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._head = Node()  # sentinel
        self._tail = Node()  # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def _insert_between(self, prev: Node, nxt: Node, value) -> Node:
        """Create a node holding value between prev and nxt. Return it. _size += 1."""
        n = Node(value)
        n.prev = prev
        n.next = nxt
        prev.next = n
        nxt.prev = n
        self._size += 1
        return n

    def push_front(self, value) -> Node:  # returns the node so callers can keep it

        return self._insert_between(self._head, self._head.next, value)

    def push_back(self, value) -> Node:

        return self._insert_between(self._tail.prev, self._tail, value)

    def remove(self, node: Node) -> None:
        """Unlink node in O(1). _size -= 1.
        Afterwards set node.prev = node.next = None.
        If node.prev is None (already removed), raise ValueError."""

        if node.prev is None or node.next is None:
            raise ValueError
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = node.next = None
        self._size -= 1

    def pop_front(self):

        if self._size == 0:
            raise IndexError("Pop from empty list")
        n = self._head.next
        self.remove(n)

        return n.value

        # remove and return the value. Empty -> IndexError

    def pop_back(self):

        if self._size == 0:
            raise IndexError("Pop from empty list")
        n = self._tail.prev
        self.remove(n)

        return n.value

    def move_to_front(self, node: Node) -> None:
        """Move an existing node to the front without creating a new one."""
        if node.prev is None or node.next is None:
            raise ValueError("node is not in the list")
        if node.prev is self._head:  # already at the front
            return
        # unlink
        node.prev.next = node.next
        node.next.prev = node.prev

        first = self._head.next
        node.next = first
        node.prev = self._head
        first.prev = node
        self._head.next = node

    def __iter__(self):
        n = self._head.next
        while n is not self._tail:
            yield n.value

            n = n.next

        # yield values front -> back

    def __reversed__(
        self,
    ):  # yield values back -> front (this tests your prev pointers)
        n = self._tail.prev
        while n is not self._head:
            yield n.value

            n = n.prev
