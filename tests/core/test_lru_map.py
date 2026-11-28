from zerocode.core.lru_map import LRUMap


def test_evicts_least_recently_used():
    c = LRUMap(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")            # "a" becomes newest, "b" is now oldest
    c.put("c", 3)         # evicts "b"
    assert "b" not in c
    assert c.get("a") == 1 and c.get("c") == 3
    assert len(c) == 2


def test_update_existing_key():
    c = LRUMap(2)
    c.put("a", 1)
    c.put("a", 99)
    assert len(c) == 1
    assert c.get("a") == 99
