from os import PathLike
from typing import Union, Generator


def yield_lines(path: Union[PathLike, str]) -> Generator[str, None, None]:
    with open(path) as f:
        for line in f:
            yield line.strip()


class Day1:
    def p1(self):
        current = 0
        max_calories = 0
        for line in yield_lines("d1.txt"):
            if not line:
                max_calories = max(current, max_calories)
                current = 0
                continue
            current += int(line)
        max_calories = max(current, max_calories)
        print(max_calories)
