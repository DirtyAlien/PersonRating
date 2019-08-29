from typing import Sequence, Iterable, TypeVar

T = TypeVar('T')


def chunked(l: Sequence[T], n: int) -> Iterable[Sequence[T]]:
    for i in range(0, len(l), n):
        yield l[i:i + n]
