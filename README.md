# Melting Gerry

The Melting Gerry game is a word game where the goal is to guess the word by selecting different letters until the word is completely guessed.
The main character of this game is a snowman named Gerry.

To save Gerry's life, the user has to find all of the letters in the word randomly selected by the computer from one of the five available categories. Each wrong guess will cause Gerry to start melting. The user has six attempts to guess the word before Gerry gets melted.

The game is quite challenging as the length of words to guess ranges from three to even fifteen letters. Additionally, in order to keep the user entertained for a long time, I have made sure that the number of words available for guessing is adequate - there are over 500 words at the moment.

[View the live project here](https://melting-gerry.herokuapp.com/)

---

## Table of contents

- [Flow Chart](#flow-chart)
- [User Experience (UX)](#user-experience-ux)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site owners Goals](#site-owners-goals)
- [Design](#design)
  - [Colors](#colors)
  - [Artwork](#artwork)
- [Features](#features)
  - [User Name](#user-name)
  - [Menu](#menu)
  - [Instructions how to play](#instructions-how-to-play)
  - [Play game](#play-game)
  - [Exit game](#exit-game)
- [Features to be implemented](#features-to-be-implemented)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools](#tools)
- [Testing](#testing)
  - [PEP8](#pep8)
- [Testing User Stories from the User Experience (UX) Section](#testing-user-stories-from-the-user-experience-ux-section)
- [Bugs](#bugs)
  - [Sovled bugs](#solved-bugs)
  - [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Content](#content)
- [Acknowledgments](#acknowledgments)

---

## Flow Chart

The Lucid application was used to create a flow chart for the Melting Gerry game. The flowchart shown below helped me to identify all the essential steps within the game and simultaneously offer a bigger picture of the project.

Creating a flowchart helped me find less obvious features of the program's algorithm, which were then refined to improve its performance, i.e., bottlenecks, flaws, and unnecessary steps.

![Flow chart](docs/screenshots/flow_chart_of_melting_gerry_game.png)

[Back to Top](#table-of-contents)

---

## User Experience (UX)

### User Goals

- The game is easy to navigate and provides appropriate functionality to entertain the user.
- The game should have different categories of words that the user can choose from.
- Each category should contain words of varying difficulty to guess.
- Each category should have a sufficient number of words to guess to keep the user entertained.
- The game rules are clearly explained.
- The game should allow the user to continue to play after each game.
- The user should know how many attempts are left to guess the word.
- The user should know which letters have already been used.
- The game should appropriately handle the user entries.

[Back to Top](#table-of-contents)

### User Stories

- As a user, I want the game instructions to be easily accessible and easy to understand.
- As a user, I want the game to be intuitive and easy to navigate.
- As a user, I want to have the option to choose different word categories.
- As a user, I want to try to guess words of varying difficulty levels.
- As a user, I want to know the word I was trying to guess when the game is over.

[Back to Top](#table-of-contents)

### Site owners Goals

- To have an easy-to-navigate and entertaining website where users can spend some time enjoying the Melting Gerry game.
- To have different word categories so the user can have an option to try to guess different words.
- To have an algorithm in the code that can handle all the user inputs.
- To have enough words to guess in each category to entertain the user for a long time.

[Back to Top](#table-of-contents)

---

## Design

### Colors

- Coloured Text

    To achieve a better user experience, I decided to implement a simple color scheme to improve the overall user experience.
  - The red color is used to highlight errors due to incorrect user entries.

  ![Error message](docs/screenshots/error_message.png)
  - The yellow color is used to inform the user that the letter they have chosen to guess the word is not in the word.

  ![Incorrect letter](docs/screenshots/incorrect_letter_message.png)
  - The green color is used to inform the user that the letter they had chosen to guess the word was correct. In addition, this color is used to display a congratulation message if the word is guessed correctly.

  ![Correct letter](docs/screenshots/correct_letter_message.png)
  ![Game won](docs/screenshots/game_won_message.png)
  - The blue color is used to display information when the game is over and the word is not guessed correctly.

  ![Word not guessed](docs/screenshots/word_not_guessed_message.png)

[Back to Top](#table-of-contents)

### Artwork

- The main ???Snowman??? logo was created using the [Text to ASCII ART Generator](https://patorjk.com/software/taag/#p=testall&h=3&f=Big&t=SNOWMAN) with some small     modifications from the originally generated artwork.
  ![Main Logo](docs/screenshots/main_logo.png)

- The artwork of Gerry the Snowman is a mix of two artworks found on [ASCII Art](https://www.asciiart.eu/holiday-and-events/christmas/snowmen)
  - Art by Hayley Jane Wakenshaw
  - Art by jb

    The final artwork was created by myself using the two artworks mentioned above.

  ![Snowman Gerry](docs/screenshots/artwork_of_gerry_the_snowman.png)

[Back to Top](#table-of-contents)

---

## Features

### User Name

- Once the program has been executed, the welcome screen is displayed, informing the user about the game name.
- The user is asked to enter their name before the game starts.

  ![Enter User Name](docs/screenshots/enter_user_name_screen.png)

- Only alphabetical characters are allowed when entering the user name. Special characters, numbers, etc., will not be accepted.

  ![Player Name Not Alphabet Letters](docs/screenshots/player_name_alphabet_characters_only.png)

- In addition, the user name can not be longer than 20 letters.

  ![Player Name Too Long](docs/screenshots/player_name_max_20_characters.png)

- If the user name has an incorrect format (blank), an appropriate message will be displayed on the screen.

  ![Player Name Blank](docs/screenshots/player_name_blank.png)

[Back to Top](#table-of-contents)

### Menu

- Once the player's name is entered, the game menu is displayed on the screen. To achieve a better user experience, I decided to have all the text information displayed in the middle of the console, which in my opinion, looks very nice.

  ![Menu](docs/screenshots/menu.png)

- At this stage, the user has three options:
  - Play game
  - Read instructions on how to play
  - Exit game

    Short text information is displayed below the menu, informing which key needs to be pressed to select each option.
    If the user presses other keys than **P**, **I** or **E**, then a message will be displayed to correctly enter one of the available options.

  ![Menu Not Valid Option Selected](docs/screenshots/menu_not_valid_option_selected.png)

[Back to Top](#table-of-contents)

### Instructions how to play

- Once the user selects to read the game instructions, the following screen will be displayed in the console window. The game instructions are very simple and easy to follow.

  ![Game Instructions](docs/screenshots/game_instructions.png)
- When the user is familiar with game instructions, they have two options:
  - Play the game by pressing the **P** key.
  - Return to the main menu by pressing the **E** key.
- If the user chooses a different option, a message will be displayed on the screen asking them to select a valid option.

  ![Game Instructions Choose Valid Option](docs/screenshots/game_instructions_choose_valid_option.png)

[Back to Top](#table-of-contents)

### Play game

- Before the game starts, the user will be asked to choose a category number from which the random word will be selected. The game is challenging; therefore, the difficulty of guessing the word will vary for each game. Some words can only contain three letters to guess, while others can even have fifteen letters (random selection).
- Currently, in the game, there are five-word categories to choose from:
  - Animals
  - Job and occupation
  - Fruit
  - Food
  - Colors

  ![Category Selection](docs/screenshots/category_selection.png)

- If the user selects a different option than is available, the following message will be shown in the console.

  ![Category Selection Invalid Choice](docs/screenshots/category_selection_invalid_choice.png)
- If the user decides to press the **E** key, the main menu will be displayed again in the console.
- If the correct category number is selected by the user, the main game screen will be displayed.

  ![Main Game Screen](docs/screenshots/main_game_screen.png)
- During the game the following information is displayed on the screen:
  - The number of attempts left to guess the word.
  - A hidden word that is represented by underscores '_' The number of underscores is equal to the number of letters in the word to be guessed.
  - Which letters have been already used to guess the word
- Once the letter is entered by the user, the program checks if the letter is listed in the word. If not, information in yellow color is displayed on the screen to inform the user that the letter they selected is not listed in the word. The used letters table will be updated automatically with the chosen letter. The number of attempts to finish the game will decrease.
- Snowman Gerry will start melting!!!

  ![Letter not in word message](docs/screenshots/letter_not_in_word.png)
- If the letter entered by the user is correct, information in green color is displayed on the screen to inform the user that the letter they selected is correct. The used letters table will be updated automatically. The number of attempts to finish the game remains the same.

  ![Letter in word message](docs/screenshots/letter_in_word_message.png)
- Snowman Gerry is safe!!!
- If the same letter is entered by the user again, the following message is displayed on the screen. The used letters table is not updated as the letter is already being used. The number of attempts to finish the game is not changed either.

  ![Letter already used message](docs/screenshots/letter_already_used_message.png)
- If the user enters a character other than the letter, the appropriate information will be displayed in the console.
- The number of attempts left to finish the game remains the same.

  ![Incorrect character entered message](docs/screenshots/incorrect_character_entered_message.png)
- If more than one letter is entered by the user, the following error message will be displayed to inform the user to enter only one letter at a time.

  ![More than one character entered message](docs/screenshots/more_that_one_character_entered_message.png)
- When the number of attempts to save Gerry???s life is equal to zero, a new screen will be displayed informing the user that snowman Gerry has melted. At this stage, the user has the option to start the game again by pressing the **Y** key or exit the main menu by pressing the **N** key.

  ![Game over word not guessed](docs/screenshots/game_over_word_not_guessed_message.png)
- If any other option than **Y** or **N** is selected by the user, the following screen will be displayed to inform the user to choose the correct option.

  ![Game over invalid choice](docs/screenshots/game_over_invalid_choice.png)
- If the word is guessed correctly, a congratulations message is displayed on the screen. The user has the option to play the game again or exit to the main menu.

  ![Game over word guessed correctly](docs/screenshots/game_over_word_guessed_message.png)
- If any other option than **Y** or **N** is selected by the user, the following screen will be displayed to inform the user to choose the correct option.

  ![Game over invalid choice](docs/screenshots/game_over_invalid_choice.png)

[Back to Top](#table-of-contents)

### Exit game

- If the user hits the **E** key while in the main menu, the game will be terminated and the game exit screen will be displayed.

  ![Exit game](docs/screenshots/exit_game_message.png)

[Back to Top](#table-of-contents)

---

## Features to be implemented

- To have a record of users??? scores.

    I plan to implement this idea by using a Google spreadsheet to store the number of words guessed by each player. After finishing the game and saving the results in a spreadsheet the user would receive information on which position, they are on the score list. There should also be an option in the game menu to display the high score list on the screen with limitations to the top 10 highest scores.

[Back to Top](#table-of-contents)

---

## Technologies Used

### Languages

- [Python](https://www.python.org/)

### Tools

- [Github](https://github.com/)
  - Used to store all the project files written in Gitpod.

- [GitPod](https://www.gitpod.io/)
  - Used for writing the code, committing, and pushing to GitHub. Gitpod terminal was also used to deploy the project to Heroku.
- [PEP8 validator](http://pep8online.com/)
  - Used to validate the python code.
- [VS Code](https://code.visualstudio.com/)
  - To test the code in case of any problems
- [Heroku](https://www.heroku.com)
  - To deploy the project into the live environment.
- [Lucid](https://lucid.app/users/login)
  - To create a project diagram.

[Back to Top](#table-of-contents)

---

## Testing

### PEP8

The code has been tested using [PEP8 Online](http://pep8online.com/)

- Initial run.py validator testing - six warnings and one error were presented.

  ![Initial run.py validator testing](docs/screenshots/initial_validator_testing.png)

- Final run.py validator testing - all issues fixed.

  ![Final run.py validator testing](docs/screenshots/final_validator_testing_errors_fixed.png)

- Initial artwork.py validator testing - 7 warnings were presented.

  ![Initial artwork.py validator testing](docs/screenshots/initial_artwork_validator_testing.png)

- Final artwork.py validator testing - all issues fixed.

  ![Final artwork.py validator testing](docs/screenshots/final_artwork_validator_testing.png)

- Initial categories.py validator testing - 1 warninig was presented.

  ![Initial categories.py validator testing](docs/screenshots/initial_categories_validator_testing.png)

- Final categories.py validator testing - all issues fixed.

  ![Final categories.py validator testing](docs/screenshots/final_categories_validator_testing.png)

[Back to Top](#table-of-contents)

---

## Testing User Stories from the User Experience (UX) Section

### As a user, I want the game instructions to be easily accessible and easy to understand

- **Plan**

    Describe the game rules in a very simple way and ensure the user has easy access to read them.

- **Implementation**

    When the user selects to read the game instructions by pressing the **I** key in the main menu, a new screen in the console will be displayed with the rules of the game.

- **Testing**

    Tests have been conducted numerous times to ensure that the game rules are displayed correctly after pressing the **I** key from the main menu. In addition, many of my friends who were testing this game confirmed that the game rules are explained very well in a clear and very understandable form.

- **Result**

    The game instructions are explained very well and they are easily accessible.
- **Verdict**

    The user has easy access to the easily understandable game rules.

### **As a user, I want the game to be intuitive and easy to navigate.**

- **Plan**

    Create a very simple game control system that is easy to navigate and very intuitive to use.

- **Implementation**

  - _Main menu section_

    The following letters are being used to ensure easy navigation in the main menu:
    - **P** key will start the game.
    - **I** key will display the game instructions.
    - **E** key will exit the game.

  - _Instructions how to play section_

    The following letters are being used to ensure easy navigation in the section where the game instructions are displayed:
    - **P** key will start the game.
    - **E** key will return to the main menu.

  - _Category selection section_

    Only numbers from **1 - 5** will be accepted when choosing a word category
    - **E** key will return to the main menu

  - _Handling other user entries_

    If the user presses a key other than the required key, a message prompting the user to press the appropriate key will appear on the screen.

- **Testing**

    Testing was carried out in each section of the game to ensure that only appropriate keys pressed by the user would be accepted to navigate properly through the game. If the user presses a key other than the required one, a message will be displayed on the screen asking the user to press the correct key.

- **Result**

    All tests passed. No issues noted. The game navigation system is working as expected.
- **Verdict**

    A simple navigation system has been implemented successfully.

### As a user, I want to have the option to choose different word categories

- **Plan**

    Provide the user with the ability to choose a category from which they will be guessing the word.

- **Implementation**

    Five different categories are available for the user to choose from. See the list below:
  - Animals
  - Job and occupation
  - Fruit
  - Food
  - Colors

- **Testing**

    Tests have been conducted numerous times to ensure that the words are loaded correctly from each category selected.

- **Result**

    Tests confirmed that the words were being loaded from each category.

- **Verdict**

    The user can choose from five different categories. Each category has a corresponding set of words to minimize the chance that the same word is loaded twice in a row during the game.

### As a user, I want to try to guess words of varying difficulty levels

- **Plan**

    Each category should contain words of varying lengths.

- **Implementation**

    The following websites were visited to build word banks for each category.
  - [Enchanted Learning](https://www.enchantedlearning.com/wordlist/)
  - [The Game Gal](https://www.thegamegal.com/printables/)

 The word banks available in the game are as follows:

- The animal category contains 88 words, with word lengths ranging from three to twelve letters.
- The job and occupation category contains 204 words, with word lengths ranging from three to fifteen letters.
- The fruit category contains 53 words, with word lengths ranging from three to eleven letters.
- The food category contains 58 words, with word lengths ranging from three to ten letters.
- The colors category contains 105 words, with word lengths ranging from three to thirteen letters.  

- **Testing**

    Tests were carried out multiple times to ensure that the words displayed on the screen were of varying lengths, meaning that they had varying difficulty levels to guess.

- **Result**

    Each category provides words of varying difficulty levels to guess, which are correctly displayed on the screen.

- **Verdict**

    The game provides words to be guessed of varying difficulty levels for each category.

### As a user, I want to know the word I was trying to guess when the game is over

- **Plan**

    Display the word the user was trying to guess.

- **Implementation**

  - _The user did not guess the word_

    - When the game is over, and the word is not guessed by the user, the word will be revealed and displayed on a new screen.

  - _The user did guess the word_

    - When the game is over and the word is guessed by the user, the word will be displayed on a new screen with a congratulations message.

- **Testing**

    Tests have been conducted numerous times to ensure that the words are displayed correctly when the game is over.

- **Result**

    The user has the opportunity to find out what the word was they were trying to guess during the game.

- **Verdict**

    The word that the user was trying to guess is displayed on the screen when the game is over.

All tests from the Testing User Stories section were performed on both the Gitpod terminal and the Heroku terminal.
Additional tests were also performed on each screen of the game by entering data outside of the acceptable range. No issues noted - all user entries are handled correctly.

[Back to Top](#table-of-contents)

---

## Bugs

### Solved bugs

- Issue
  - The following message was displayed in the console during the manual testing process : **NameError: name 'player_name' is not defined**.
      This issue was related to the local scope of the `player_name` variable in the `get_player_name` function.

- Solution
  - Fixed by setting up `player_name` variable as global.

### Unfixed bugs

- None currently known

[Back to Top](#table-of-contents)

---

## Deployment

The project was deployed to Heroku following the steps below:

- Commit changes and push them to GitHub.
- Go to [Heroku's](https://www.heroku.com) website.
- Create an account or select login.
- From the Heroku dashboard, click on **Create new app**.
- Enter the **App name** and **Choose a region** before clicking on **Create app**.
- Select **Config Vars** under the **Settings** tab.
- Click on **Reveals Config Vars**.
- Add in the Config Var, **KEY: PORT**, and **VALUE: 8000**.
- Click on the **Buildpacks** section and click **Add buildpack**.
- Select **python** and click **Save changes**.
- Add **nodejs** buildpack using the same process.

Due to the current security breach in Heroku, the following steps were taken to deploy the game code to Heroku as automated deployments from GitHub have been disabled:

- In the Gitpod console application enter **heroku login -i**. Note: For this project, the GitPod environment was created using a template provided by the Code Institute.Installation of [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) may be required if you are using any other programming environment.
- Log in with the email address used while creating the Heroku account.
- Enter the password.
- Enter **heroku git: remote -a** followed by the project's name on Heroku (in this case, **heroku git:remote -a melting-gerry**).
- Once the code is ready to be deployed enter **git push heroku main** in the console to deploy to Heroku.

[Back to Top](#table-of-contents)

---

## Content

- The artwork used in this project was copied from the following websites:
  - [ASCII ART Generator](https://patorjk.com/software/taag/#p=testall&h=3&f=Big&t=SNOWMAN)
  - [ASCII Art](https://www.asciiart.eu/holiday-and-events/christmas/snowmen)

- The following websites were visited to build word banks for each category:
  - [Enchanted Learning](https://www.enchantedlearning.com/wordlist/)
  - [The Game Gal](https://www.thegamegal.com/printables/)

- The following website was visited to learn how to output colored text to the terminal in Python.
  - [Stack Overflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)

[Back to Top](#table-of-contents)

---

## Acknowledgments

- My Mentor Simen [Eventyret_mentor](https://github.com/Eventyret) for continuous helpful feedback.

- Code Institute's [Slack](https://app.slack.com/client/) community for their support.
- [W3Schools](https://www.w3schools.com/python/) as an additional source of knowledge.
- All family members and friends who helped test this game.

[Back to Top](#table-of-contents)
