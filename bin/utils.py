from wordle import Wordle
from typing import Set

from main import logger

'''
Labels a word w1 given true word w2
'''


def label(w1: str, w2: str):
    raise NotImplementedError


'''
Class encoding a candidate action
'''


class Action:
    guess: str
    entropy: float
    word_set: Set[str]


'''
Calculates entropy (\E[-\lg(x)], where x denotes the proportion of remaining words
'''


def get_entropy(guess: str, word_set: Set[str]) -> float:
    raise NotImplementedError


'''
Calculates best action
'''


def best_action(game: Wordle) -> Action:
    raise NotImplementedError
