from zerocode.core.fnv_hash import fnv1a_32


def test_known_vectors():
    # Published FNV-1a 32-bit reference values
    assert fnv1a_32("") == 0x811C9DC5
    assert fnv1a_32("a") == 0xE40C292C
    assert fnv1a_32("foobar") == 0xBF9CF968


def test_deterministic_and_in_range():
    for s in ["abc", "def foo(x):", "ممتاز", "🙂"]:
        h = fnv1a_32(s)
        assert h == fnv1a_32(s)
        assert 0 <= h <= 0xFFFFFFFF


def test_unicode_is_hashed_as_utf8_bytes():
    assert fnv1a_32("é") != fnv1a_32("e")


def test_reasonable_spread_over_buckets():
    m = 61                                   # prime bucket count
    counts = [0] * m
    n = 10_000
    for i in range(n):
        counts[fnv1a_32(f"key{i}") % m] += 1
    assert max(counts) < 3 * (n / m)         # loose bound: no bucket hoards keys
