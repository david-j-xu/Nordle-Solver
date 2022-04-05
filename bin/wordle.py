'''
Wordle Emulator, emulates a given wordle game
'''
from typing import List
from utils import *
import random
from enum import Enum
from words import complete_word_set
from math import log2 as lg

'''
Wordle game representation
'''


class GameState(Enum):
    PLAYING = 0
    WON = 1
    LOST = 2


class Board:
    max_guesses: int
    curr_guesses: int
    true_word: str
    __status: GameState
    board_state: List[Label]

    def __init__(self) -> None:
        self.true_word = random.sample(complete_word_set, 1)[0]
        self.curr_guesses = 0
        self.__status = GameState.PLAYING
        self.max_guesses = 6
        self.board_state = []

    def guess(self, guess: str) -> Label:
        guess = guess.lower()
        self.curr_guesses += 1

        if (self.curr_guesses >= self.max_guesses and guess != self.true_word):
            self.__status = GameState.LOST
        elif guess == self.true_word:
            self.__status = GameState.WON
        lbl = get_label(guess_of_str(guess), guess_of_str(self.true_word))
        self.board_state.append(lbl)
        return lbl

    def get_state(self) -> GameState:
        return self.__status


class Agent:
    word_set: Set[str]

    def __init__(self) -> None:
        self.word_set = complete_word_set.copy()

    def get_action(self) -> str:
        return best_action(self.word_set)

    def update_set(self, label: Label):
        self.word_set = thin_word_set(self.word_set, label)


def thin_word_set(word_set: Set[str], label: Label) -> Set[str]:
    return set([x for x in word_set if check_valid_word(guess_of_str(x), label)])


'''
Calculates information -lg(prop_remaining) gained from a given guess.
'''


def get_information(info: Label, word_set: Set[str]) -> float:
    viable = 0
    n = len(word_set)
    for word in word_set:
        if check_valid_word(guess_of_str(word), info):
            viable += 1

    return -lg(viable / n)


'''
Defines a probability distribution on the word set
'''


def get_prob(word: str, word_set: Set[str]) -> float:
    return 1 / len(word_set)


'''
Calculates entropy of a candidate guess

'''


def get_entropy(guess: str, word_set: Set[str]) -> float:
    e_info = 0
    for word in word_set:
        lbl = get_label(guess_of_str(guess), guess_of_str(word))
        e_info += (get_information(lbl, word_set)*get_prob(word, word_set))
    return e_info


'''
Calculates best guess
'''


def best_action(word_set: Set[str]) -> str:
    max_word = ""
    max_e = -1
    for word in word_set:
        e = get_entropy(word, word_set)
        if (e > max_e):
            max_e = e
            max_word = word
    return max_word


if __name__ == "__main__":
    board = Board()
    agent = Agent()

    print("True Word: ", board.true_word)

    while (board.get_state() == GameState.PLAYING):
        next_guess = agent.get_action()
        print("Guess: ", next_guess)
        label = board.guess(next_guess)
        print("Returned Label: ", label)
        agent.update_set(label)
