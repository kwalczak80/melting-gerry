"""
This section contains all imports
"""
# External import statements
import os
import sys
import random
# Import statements I created for this game.
from snowman_gerry import display_snowman
from word_categories import (animal_words,
                             job_and_occupation_words,
                             fruit_words,
                             food_words,
                             color_words)


# Used to query the size of a terminal
width = os.get_terminal_size().columns


class TextColor:
    '''
    Class to define text colors
    printed in termianal
    '''
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def print_text_in_the_middle_of_console(text):
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
        # Other operating systems.
        print('\n' * numlines)


def display_game_name():
    """
    Function to display the game name
    """
    print_text_in_the_middle_of_console("  _____ _   _  ______          ____  "
                                        "__          _   _ ")
    print_text_in_the_middle_of_console(" / ____| \ | |/ __ \ \        / |  \/"
                                        "  |   /\   | \ | |")
    print_text_in_the_middle_of_console("| (___ |  \| | |  | \ \  /\  / /| \  "
                                        "/ |  /  \  |  \| |")
    print_text_in_the_middle_of_console(" \___ \|     | |  | |\ \/  \/ / | |\/"
                                        "| | / /\ \ |     |")
    print_text_in_the_middle_of_console(" ____) | |\  | |__| | \  /\  /  | |  "
                                        "| |/ ____ \| |\  |")
    print_text_in_the_middle_of_console("|_____/|_| \_|\____/   \/  \/   |_|  "
                                        "|_/_/    \_|_| \_|\n")


def clear_header():
    """
    Function to clear screen and display game name
    """
    clear_screen()
    display_game_name()


def print_error_message(text):
    """
    Function to print error message in red color
    """
    print(f"{TextColor.FAIL}{text}{TextColor.ENDC}")


def print_correct_guess(correct_guess_text):
    """
    Function to prints text in green color
    is user guessed the letter or word correctly
    """
    print(f"{TextColor.OKGREEN}{correct_guess_text}{TextColor.ENDC}")


def print_incorrect_guess(incorrect_guess_text):
    """
    Function to prints text in yellow color
    is user guessed the letter or word incorrectly
    """
    print(f"{TextColor.WARNING}{incorrect_guess_text}{TextColor.ENDC}")


def print_hidden_word(hidden_word):
    """
    Prints text in blue color is user
    guessed the letter or word incorrectly
    """
    print(f"{TextColor.OKBLUE}{hidden_word}{TextColor.ENDC}")


def get_player_name():
    """
    Function to validate user
    name before game commence
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
    Function to display the welcome
    message and the menu.
    """
    clear_header()
    while True:
        print_text_in_the_middle_of_console(f"Welcome {player_name}\n")
        print_text_in_the_middle_of_console("***    Menu    ***\n")
        print_text_in_the_middle_of_console("Play game\n")
        print_text_in_the_middle_of_console("Instructions how to play\n")
        print_text_in_the_middle_of_console("Exit\n")
        print_text_in_the_middle_of_console("Press P to play game or I to read"
                                            " instructions how to play.\n")
        user_input = input("Alternatively press "
                           "E to exit the game.\n".center(width)).upper()
        if user_input == "P":
            clear_header()
            word_category_selection()
        elif user_input == "I":
            clear_header()
            display_instructions()
        elif user_input == "E":
            clear_screen()
            exit_game()
        else:
            clear_header()
            print_error_message("Please choose a valid option "
                                "from the menu below !\n".center(width))


def word_category_selection():
    """
    Function to select a category
    from which the word will be guessed
    """
    while True:
        print_text_in_the_middle_of_console("Please select a category number "
                                            "from which you will be guessing "
                                            "the word.\n")
        print_text_in_the_middle_of_console("1. Animals\n")
        print_text_in_the_middle_of_console("2. Job and occupation\n")
        print_text_in_the_middle_of_console("3. Fruit\n")
        print_text_in_the_middle_of_console("4. Food\n")
        print_text_in_the_middle_of_console("5. Colors\n")
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
            clear_header()
            print_error_message("Please choose a valid option "
                                "from the menu below !\n".center(width))


def display_instructions():
    """
    Function to display game instructions
    with option to return to main menu
    """
    print_text_in_the_middle_of_console("Select a category from which you "
                                        "will be guessing the word.\n")
    print_text_in_the_middle_of_console("Try to guess the hidden letters.\n")
    print_text_in_the_middle_of_console("If you guess correctly, the letter "
                                        "will appear on the screen and \n")
    print_text_in_the_middle_of_console("Gerry the snowman will be safe.\n")
    print_text_in_the_middle_of_console("However, if you guess incorrectly "
                                        "Gerry will start melting !!!\n")
    print_text_in_the_middle_of_console("You have six attempts to save "
                                        "Gerry's life.\n")
    print_text_in_the_middle_of_console("Best of luck!\n")
    while True:
        enter_input = input("Press P to play the game or E return to "
                            "main menu\n".center(width)).upper()
        if enter_input == "P":
            clear_header()
            word_category_selection()
        elif enter_input == "E":
            menu(player_name)
        else:
            clear_header()
            print_error_message("Please choose a valid option\n".center(width))


def exit_game():
    """
    Function to display 'thank you'
    information and exit game
    """
    print_text_in_the_middle_of_console(f"Bye bye {player_name}\n")
    print_text_in_the_middle_of_console("Thank you for playing the Melting "
                                        "Gerry game.")
    print_text_in_the_middle_of_console("See you next time !!")
    sys.exit()


def play_game(word):
    '''
    Function to start the game
    after category selection
    '''
    table = list(word)
    used_letters = []
    number_of_attempts = 6
    for i in range(len(word)):
        table[i] = "_"
    while number_of_attempts > 0:
        print_text_in_the_middle_of_console(display_snowman
                                            [number_of_attempts])
        print_text_in_the_middle_of_console(f"You have {number_of_attempts} "
                                            "attempts to save Gerry's life.")
        print()
        print(" ".join(table).center(width))
        print()
        print_text_in_the_middle_of_console(f"Used letters : {used_letters}")
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
                number_of_attempts -= 1
                print_incorrect_guess(f"[{letter}] letter is "
                                      "not in the word".center(width))
        if "".join(map(str, table)) == word:
            clear_header()
            print_correct_guess("Fantastic !!! You have guessed "
                                f"the word {word} correctly.\n".center(width))
            print_correct_guess("Gerry the snowman is safe "
                                "thanks to you.\n".center(width))
            restart_game(player_name)
        elif number_of_attempts == 0:
            clear_screen()
            print_text_in_the_middle_of_console(display_snowman[0])
            print_text_in_the_middle_of_console("Oh my GOD !!! Gerry has "
                                                "melted !!!\n")
            print_hidden_word("The word you were trying"
                              f" to guess was {word}\n".center(width))
            restart_game(player_name)


def restart_game(player_name):
    """
    Function to ask user
    if they want to start a new game
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
    '''
    Main function to run the game
    '''
    clear_screen()
    display_game_name()
    player_name = get_player_name()
    menu(player_name)


melting_gerry_game()
