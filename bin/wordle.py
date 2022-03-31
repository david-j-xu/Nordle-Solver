'''
Wordle Emulator, emulates a given wordle game
'''
from typing import List
from utils import *
from math import log2 as lg

'''
Wordle game representation
'''


class Wordle:
    board_count: int
    max_guesses: int
    curr_guesses: int
    board_states: List[Label]

    def __init__(self) -> None:
        pass


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


def get_entropy(info: Label, word_set: Set[str]) -> float:
    viable = 0
    n = len(word_set)
    for word in word_set:
        if Label.check_valid_word(guess_of_str(word), info):
            viable += 1
    return -lg(viable / n)


'''
Calculates best action
'''


def best_action(game: Wordle) -> Action:
    raise NotImplementedError
