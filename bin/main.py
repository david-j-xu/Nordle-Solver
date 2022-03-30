import sys
import argparse
import logging
from dotenv import dotenv_values
from words import word_list

# create logger for debugging purposes using name denoted in .env
logger = logging.getLogger(name=dotenv_values('.env')['LOGGER_NAME'])

'''
Terminal input to n-ordle solver

Usage: main.py [-h] [-n <num>] [--ter] [--sim <numgames>] [--debug <filename>]

options:
    -h, --help              Help
    -n, --number            Number of wordles (default 1)
    -t, --ter               If added, takes user input to help solve a wordle game
    -s, --sim               Simulates <numgames> games, prints summary statistics
    -v, --debug             Turns on debugging log writing to <filename>, defaults to stderr.
'''


def main(argv):
    # parse arguments
    parser = argparse.ArgumentParser()
    # TODO: Add arguments parsing as documented above


if __name__ == "__main__":
    main(sys.argv[1:])
