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


def display_game_name():
    """
    Display the game name
    """
    p("  _____ _   _  ______          ____  __          _   _ ")
    p(" / ____| \ | |/ __ \ \        / |  \/  |   /\   | \ | |")
    p("| (___ |  \| | |  | \ \  /\  / /| \  / |  /  \  |  \| |")
    p(" \___ \|     | |  | |\ \/  \/ / | |\/| | / /\ \ |     |")
    p(" ____) | |\  | |__| | \  /\  /  | |  | |/ ____ \| |\  |")
    p("|_____/|_| \_|\____/   \/  \/   |_|  |_/_/    \_|_| \_|\n")


def clear_header():
    """
    calls to clear screen and display game name
    """
    clear_screen()
    display_game_name()

def print_error_message(text):
    """
    Prints error message in red color
    """
    print(f"{bcolors.FAIL}{text}{bcolors.ENDC}")
    

def print_correct_guess(correct_guess_text):
    """
    Prints text in green color is user guessed the letter or word correctly
    """
    print(f"{bcolors.OKGREEN}{correct_guess_text}{bcolors.ENDC}")
    

def print_incorrect_guess(incorrect_guess_text):
    """
    Prints text in yellow color is user guessed the letter or word incorrectly
    """
    print(f"{bcolors.WARNING}{incorrect_guess_text}{bcolors.ENDC}")
    

def print_hidden_word(hidden_word):
    """
    Prints text in yellow color is user guessed the letter or word incorrectly
    """
    print(f"{bcolors.OKBLUE}{hidden_word}{bcolors.ENDC}")
    