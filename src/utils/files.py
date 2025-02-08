from typing import TextIO


def skip_byte_order_mark(f: TextIO) -> None:
    if f.read(1).encode("utf-8") != b"\xef\xbb\xbf":
        f.seek(0)
    else:
        f.readline()
