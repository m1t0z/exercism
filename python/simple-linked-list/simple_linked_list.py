from __future__ import annotations
from typing import Optional


class Node:
    """Represents a single node inside the LIFO Linked List"""

    def __init__(self, value: int, next: Node = None):
        self._value = value
        self._next = next

    def value(self) -> int:
        return self._value

    def next(self) -> Optional[Node | None]:
        return self._next


class LinkedList:
    """LIFO Linked List"""

    def __init__(self, values=[]):
        self._head = None
        for value in values:
            self.push(value)

    def __iter__(self):
        node = self._head
        while node:
            yield node.value()
            node = node.next()

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def head(self) -> Node:
        if not self._head:
            raise EmptyListException("No head node: list is empty!")
        return self._head

    def push(self, value: int):
        self._head = Node(value, self._head)

    def pop(self) -> int:
        if not self._head:
            raise EmptyListException("Nothing to pop from the list!")
        value = self._head.value()
        self._head = self._head.next()
        return value

    def reversed(self) -> LinkedList:
        return LinkedList(self)


class EmptyListException(Exception):
    pass
