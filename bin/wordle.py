'''
Wordle Emulator, emulates a given wordle game
'''
from typing import List
from main import logger
from enum import Enum

'''
Enumeration of hint types
'''


class Hint(Enum):
    GREY = 1
    YELLOW = 2
    GREEN = 3


'''
Wordle game representation
'''


class Wordle:
    board_count: int
    max_guesses: int
    curr_guesses: int
    board_states: List[Hint]

    def __init__(self) -> None:
        pass
