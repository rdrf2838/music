from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


def map_if(
    xs: Iterable[T], cond: Callable[[T], bool], f: Callable[[T], T]
) -> Iterable[T]:
    return (f(x) if cond(x) else x for x in xs)
