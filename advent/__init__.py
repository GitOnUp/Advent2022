import heapq
from os import PathLike
from typing import Union, Generator, List


def yield_lines(path: Union[PathLike, str]) -> Generator[str, None, None]:
    with open(path) as f:
        for line in f:
            yield line.strip()


class Day1:
    import heapq

    @staticmethod
    def top(n: int) -> List[int]:
        current = 0
        top_calories = []

        def keep_top(calories):
            if top_calories and calories < top_calories[0]:
                return
            heapq.heappush(top_calories, calories)
            if len(top_calories) > n:
                heapq.heappop(top_calories)

        for line in yield_lines("d1.txt"):
            if line:
                current += int(line)
                continue
            keep_top(current)
            current = 0
        keep_top(current)
        return top_calories

    @staticmethod
    def p1():
        print(Day1.top(1)[0])

    @staticmethod
    def p2():
        print(sum(Day1.top(3)))