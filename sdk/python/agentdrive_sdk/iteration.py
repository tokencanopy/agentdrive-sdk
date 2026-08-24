"""Opaque-cursor page and item iterators."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class Page(Generic[T]):
    """A page plus the opaque cursor needed to request the next page."""

    items: tuple[T, ...]
    next_cursor: str | None
    has_more: bool | None = None
    raw: object | None = None


class CursorPages(Generic[T]):
    """Lazy page iterator that never interprets or mutates cursor strings."""

    def __init__(
        self,
        loader: Callable[[str | None], Page[T]],
        *,
        initial_cursor: str | None = None,
        max_pages: int | None = None,
    ) -> None:
        self._loader = loader
        self._cursor = initial_cursor
        self._max_pages = max_pages

    def __iter__(self) -> Iterator[Page[T]]:
        cursor = self._cursor
        pages = 0
        while True:
            if self._max_pages is not None and pages >= self._max_pages:
                return
            page = self._loader(cursor)
            pages += 1
            yield page
            if not page.next_cursor or page.has_more is False:
                return
            cursor = page.next_cursor


class CursorItems(Generic[T]):
    """Lazy item iterator over :class:`CursorPages`."""

    def __init__(self, pages: CursorPages[T]) -> None:
        self._pages = pages

    def __iter__(self) -> Iterator[T]:
        for page in self._pages:
            yield from page.items
