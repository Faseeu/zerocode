FNV_OFFSET_32 = 0x811C9DC5
FNV_PRIME_32 = 0x01000193
MASK_32 = 0xFFFFFFFF


def fnv1a_32(text: str) -> int:
    """Stable 32-bit FNV-1a hash of text (UTF-8). Same input -> same output, every run."""
    h = FNV_OFFSET_32
    for byte in text.encode("utf"):
        h ^= byte
        h = (h * FNV_PRIME_32) & MASK_32

    return h
