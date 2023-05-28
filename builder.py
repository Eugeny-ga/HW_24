from typing import Dict, List, Callable, Generator, Optional, Iterable

from functions import filter_query, map_query, unique_query, sort_query, limit_query, regex_query

cmd_to_functions: Dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    "regex": regex_query,
}


def read_file(file_name: str) -> Generator:
    with open(file_name) as file:
        for line in file:
            yield line





def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    function: Callable = cmd_to_functions[cmd]
    return list(function(value=value, data=prepared_data))


