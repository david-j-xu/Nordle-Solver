from typing import Set, List
from enum import Enum
from xmlrpc.client import Boolean

'''
Enumeration of hint types
'''


class Hint(Enum):
    GREY = 1
    YELLOW = 2
    GREEN = 3


'''
Class encoding a label
'''


class Label:
    guess: List[str]
    colors: List[Hint]

    def __init__(self, guess: List[str]) -> None:
        self.guess = guess
        self.colors = [Hint.GREY for _ in range(5)]

    def update(self, idx: int, color: Hint) -> None:
        if (idx < 0 or idx > 4):
            raise ValueError("Must only give hints for valid indices")

        self.colors[idx] = color

    def __str__(self) -> str:
        return ' '.join([self.guess[i] + ':' + self.colors[i].__str__() for i in range(5)])


'''
Labels a candidate word w1 given true word w2
'''


def label(w1: List[str], w2: List[str]):
    if (not (len(w1) == len(w2) == 5)):
        raise ValueError("Words must be of length 5")

    new_label = Label(w1.copy())

    w1p = w1.copy()
    w2p = w2.copy()

    # label all green elements
    for i in range(5):
        if w1p[i] == w2p[i]:
            new_label.update(i, Hint.GREEN)
            w1p[i] = '$'
            w2p[i] = '$'

    # label all yellow elements
    for i in range(5):
        if w1p[i] != '$':
            for j in range(5):
                if w1p[i] == w2p[j]:
                    new_label.update(i, Hint.YELLOW)
                    w2p[j] = '$'
                    break

    return new_label


'''
Helper function checking consistency of word w with labels l
'''


def check_valid_word(w: List[str], l: Label) -> Boolean:
    if len(w) != 5:
        raise ValueError("Word must be of length 5")
    # word is valid iff it has the same coloring against the guess as the true word
    guess_word = l.guess
    cand_lbl = label(guess_word, w)
    for i in range(5):
        if cand_lbl.colors[i] != l.colors[i]:
            return False
    return True


'''
Helper function to create list of strings from string
'''


def guess_of_str(guess: str) -> List[str]:
    if len(guess) != 5:
        raise ValueError("Incorrect length of string")
    return [guess.lower()[i] for i in range(5)]


if __name__ == "__main__":
    w1 = guess_of_str("wordl")
    w2 = guess_of_str("wordq")
    label(w1, w2)
    print(w1, w2)
