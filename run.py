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

def get_player_name():
    """
    Validates user name before game commence
    """
    global player_name    
    while True:
        player_name = input("Please enter your name:\n".center(width)).strip()
        if player_name == "":
            clear_header()
            print_error_message("The player name cannot "
                                "be blank !!\n".center(width))        
        elif not player_name.isalpha():
            clear_header()
            print_error_message("The player name may only "
                                "contain alphabetic "
                                "characters.\n".center(width))
        elif (len(player_name) > 20):
            clear_header()
            print_error_message("The player name is too long"
                                "- max 20 characters !!\n".center(width))
        else:
            clear_screen()
            break
    return player_name


def menu(player_name):
    """
    Display the welcome message and the menu.
    """
    while True:
        clear_header()
        p(f"Welcome {player_name}\n")
        p("***    Menu    ***\n")
        p("Play game\n")
        p("Instructions how to play\n")
        p("Exit\n")
        p("Press P to play game or I to read"
          " instructions how to play.\n")
        user_input = input("Alternatively press "
                           "E to exit the game.\n".center(width)).upper()
        if user_input == "P":
            clear_header()
            word_category_selection()
        elif user_input == "I":
            clear_screen()
            display_instructions()
        elif user_input == "E":
            clear_screen()
            exit_game()


def word_category_selection():
    """
    Function to select a category from which the word will be guessed
    """
    
    while True:
        clear_screen()
        p("Please select a category from "
          "which you will be guessing the word.\n")
        p("1. Animals\n")
        p("2. Job and occupation\n")
        p("3. Fruit\n")
        p("4. Food\n")
        p("5. Colors\n")
        player_choice = input("Alternatively, press E "
                              "to exit\n".center(width)).upper()
        if player_choice == '1':
            word = str(animal_words[random.randint(0, len(animal_words) - 1)])
            clear_header()
            play_game(word)
        elif player_choice == '2':
            word = str(job_and_occupation_words
                       [random.randint(0, len(job_and_occupation_words) - 1)])
            clear_header()
            play_game(word)
        elif player_choice == '3':
            word = str(fruit_words[random.randint(0, len(fruit_words) - 1)])
            clear_header()
            play_game(word)
        elif player_choice == '4':
            word = str(food_words[random.randint(0, len(food_words) - 1)])
            clear_header()
            play_game(word)
        elif player_choice == '5':
            word = str(color_words[random.randint(0, len(color_words) - 1)])
            clear_header()
            play_game(word)
        elif player_choice == "E":
            menu(player_name)
        else:
            p("Please choose a valid option from the menu!")


def display_instructions():
    """
    Function to display game instructions
    with option to return to main menu
    """
    display_game_name()
    p("Choose a category from which you will be guessing the word.\n")
    p("Try to guess the hidden letters.\n")
    p("As long as you guess correctly, Gerry the Snowman will remain safe.\n")
    p("On the other hand, if you guess incorrectly, Gerry will start melting !!!\n")
    p("You have six attempts to save Gerry's life.\n")
    p("Best of luck!\n")
    while True:
        enter_input = input("Press ENTER to go back\n".center(width)).upper()
        if enter_input == "":
            menu(player_name)
        else:
            clear_header()
            print_error_message("You have typed some text before"
                      " pressing the enter button\n".center(width))


def exit_game():
    """
    Display 'thank you' information
    and exit game
    """
    p(f"Bye bye {player_name}\n")
    p("Thank you for playing the Snowman game.")
    p("See you next time !!")
    sys.exit()

def play_game(word):
    table = list(word)
    used_letters = []
    number_of_tries = 6
    for i in range(len(word)):
        table[i] = "_"
    while number_of_tries > 0:
        p(display_snowman[number_of_tries])
        p(f"You have {number_of_tries} attempts to save Gerry's life.")
        print()
        print(" ".join(table).center(width))
        print()
        p(f"Used letters : {used_letters}")
        letter = input("Please enter a "
                       "letter:\n".center(width)).upper().strip()
        clear_header()
        if len(letter) != 1:
            print_error_message("Please enter only "
                                "one letter at a time".center(width))
        elif letter in used_letters:
            print_error_message(f"[{letter}] letter "
                                "is already used !!".center(width))
        elif not letter.isalpha():
            print_error_message(f"[{letter}] is not a letter".center(width))
        else:
            used_letters.append(letter)
            if letter in word:
                print_correct_guess("YES !!! You have guessed "
                                    "the letter correctly.".center(width))
                for i in range(len(word)):
                    if word[i] == letter:
                        table[i] = letter
            else:
                number_of_tries -= 1
                print_incorrect_guess(f"[{letter}] letter is "
                                      "not in the word".center(width))
        if "".join(map(str, table)) == word:
            clear_header()
            print_correct_guess("Fantastic !! You have guessed "
                                "the word\n".center(width))
            restart_game(player_name)
        elif number_of_tries == 0:
            clear_screen()
            p(display_snowman[0])
            p("Oh my GOD !!! Gerry has melted !!!\n")
            print_hidden_word(f"The word you were trying to guess was {word}\n".center(width))
            restart_game(player_name)

def restart_game(player_name):
    """
    Ask user if they want to start new game
    """
    while True:
        user_input = input(
            "Would you like to play again? [Y]ES/[N]O\n".center(width)).upper()
        if user_input == "Y":
            clear_header()
            word_category_selection()
        elif user_input == "N":
            clear_header()
            menu(player_name)
        else:
            clear_header()
            print_error_message("Invalid choice, please "
                                "try again.\n".center(width))


def melting_gerry_game():
    clear_screen()
    display_game_name()
    player_name = get_player_name()
    menu(player_name)


melting_gerry_game()