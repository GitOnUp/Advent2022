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


class Day2:
    @staticmethod
    def generate_result_map():
        result_scores = {
            "A": {
                "X": 3,
                "Y": 6,
                "Z": 0,
            },
            "B": {
                "X": 0,
                "Y": 3,
                "Z": 6,
            },
            "C": {
                "X": 6,
                "Y": 0,
                "Z": 3,
            },
        }
        choice_scores = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }
        score_map = {}
        for opponent_play in result_scores:
            for my_play, my_result_score in result_scores[opponent_play].items():
                key = f"{opponent_play} {my_play}"
                score = my_result_score + choice_scores[my_play]
                score_map[key] = score

        return score_map

    @staticmethod
    def p1():
        score = 0
        result_map = Day2.generate_result_map()
        for line in yield_lines("d2.txt"):
            score += result_map[line]
        print(score)