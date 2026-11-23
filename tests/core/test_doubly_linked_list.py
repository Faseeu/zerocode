import random

import pytest

from zerocode.core.doubly_linked_list import DoublyLinkedList


def test_empty():
    d = DoublyLinkedList()
    assert len(d) == 0
    assert list(d) == []
    assert list(reversed(d)) == []


def test_push_order():
    d = DoublyLinkedList()
    d.push_back(2)
    d.push_back(3)
    d.push_front(1)
    assert list(d) == [1, 2, 3]
    assert list(reversed(d)) == [3, 2, 1]
    assert len(d) == 3


def test_remove_middle_head_tail_until_empty():
    d = DoublyLinkedList()
    a, b, c = d.push_back("a"), d.push_back("b"), d.push_back("c")
    d.remove(b)
    assert list(d) == ["a", "c"]
    d.remove(a)
    assert list(d) == ["c"]
    d.remove(c)
    assert list(d) == [] and len(d) == 0


def test_remove_twice_raises():
    d = DoublyLinkedList()
    n = d.push_back(1)
    d.remove(n)
    with pytest.raises(ValueError):
        d.remove(n)


def test_pop_front_back_and_empty():
    d = DoublyLinkedList()
    d.push_back(1)
    d.push_back(2)
    assert d.pop_back() == 2
    assert d.pop_front() == 1
    with pytest.raises(IndexError):
        d.pop_back()
    with pytest.raises(IndexError):
        d.pop_front()


def test_move_to_front():
    d = DoublyLinkedList()
    a, b, c = d.push_back("a"), d.push_back("b"), d.push_back("c")
    d.move_to_front(c)
    assert list(d) == ["c", "a", "b"]
    d.move_to_front(c)  # already at front: no change
    assert list(d) == ["c", "a", "b"]
    d.move_to_front(b)
    assert list(d) == ["b", "c", "a"]
    assert len(d) == 3


def test_random_ops_match_plain_list():
    rng = random.Random(0)
    d = DoublyLinkedList()
    ref = []  # plain Python list of nodes, same order
    for i in range(2000):
        op = rng.choice(["pf", "pb", "rm", "mtf", "pop"])
        if op == "pf":
            ref.insert(0, d.push_front(i))
        elif op == "pb":
            ref.append(d.push_back(i))
        elif ref and op == "rm":
            n = rng.choice(ref)
            d.remove(n)
            ref.remove(n)
        elif ref and op == "mtf":
            n = rng.choice(ref)
            d.move_to_front(n)
            ref.remove(n)
            ref.insert(0, n)
        elif ref and op == "pop":
            assert d.pop_back() == ref.pop().value
        values = [n.value for n in ref]
        assert list(d) == values
        assert list(reversed(d)) == values[::-1]
        assert len(d) == len(ref)
