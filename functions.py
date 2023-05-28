import re
from typing import Iterable, Iterator


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)

def map_query(value: str, data: Iterable[str])-> Iterator[str]:
    column_num = int(value)
    return map(lambda x: x.split()[column_num], data)

def unique_query(data: Iterable[str]) -> set:
    return set(data)


def sort_query(value: str, data: Iterable[str]) -> list:
    reverse = value == "desc"
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> list:
    limit=int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    regex = re.compile(value)
    return filter(lambda x: re.search(regex, x), data)

