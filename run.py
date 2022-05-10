# Melting Gerry game
import os
import sys
import random
from word_categories import animal_words
from word_categories import job_and_occupation_words
from word_categories import fruit_words
from word_categories import food_words
from word_categories import color_words
from snowman_gerry import display_snowman

width = os.get_terminal_size().columns

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def p(text):
    """
    Function to print text
    in the middle of console.
    """
    print(f"{text}".center(width))


def clear_screen(numlines=100):
    """
    Function to clear the console.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)