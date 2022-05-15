# **Melting Gerry**

## **Flow Chart**
The Lucid application was used to create a flow chart for the Melting Gerry game. The flowchart shown below helped me to identify all essential steps within the game and simultaneously offer the bigger picture of the project.

Creating a flowchart helped me find less obvious features of the program's algorithm, which were then refined to improve its performance, ie bottlenecks, flaws, and unnecessary steps. 

![Flow chart](docs/screenshots/flow_chart_of_melting_gerry_game.png)

---

## **User Experience (UX)**

### **User Goals**
* The game is easy to navigate and provides appropriate functionality to entertain the user.
* The game should have different categories of words the user can choose from.
* Each category should contain words of varying difficulty to guess.
* Each category should contain enough words to guess to provide the user with the appropriate level of entertainment.
* The game rules are clearly explained.
* The game should allow the user to continue to play after each game.
* The user should know how many attempts are left to guess the word.
* The user should know which letters have already been used.
* The game should appropriately handle the user entries.

### **User Stories**
* As a user, I want the game instructions to be easily accessible and easy to understand.
* As a user, I want the game to be intuitive and easy to navigate.
* As a user, I want the game to be fun and engaging.
* As a user, I want to have the option to choose different word categories.
* As a user, I want to try to guess words of varying difficulty levels.
* As a user, I want to know the word I was trying to guess when the game is over.

### **Site owners Goals**
* To have an easy-to-navigate and entertaining website where users can spend some time enjoying the Melting Gerry game.
* To have different word categories so the user can have an option to try to guess different words.
* To have an algorithm in the code that can handle all the user inputs.
* To have enough words to guess in each category to entertain the user for a long time.

---

## **Design**

### **Colors**
* Coloured Text

    To achieve a better user experience, I decided to implement a simple color scheme to improve the overall user experience.
    * The red color was used to highlight errors due to incorrect user entries.

    ![Error message](docs/screenshots/error_message.PNG)
    * The yellow color was used to inform the user that the letter they have chosen to guess the word is not in the word.

    ![Incorrect letter](docs/screenshots/incorrect_letter_message.PNG)
    * The green color is used to inform the user that the letter they had chosen to guess the word was correct. In addition, this color is used to display a congratulation message if the word is guessed correctly.

    ![Correct letter](docs/screenshots/correct_letter_message.PNG)
    ![Game won](docs/screenshots/game_won_message.PNG)
    * The blue color was used to display information when the game is over and the word is not guessed correctly.

    ![Word not guessed](docs/screenshots/word_not_guessed_message.PNG)
### **Artwork**
* The main “Snowman” logo was created using the [Text to ASCII ART Generator](https://patorjk.com/software/taag/#p=testall&h=3&f=Big&t=SNOWMAN) with some small     modifications from the originally generated artwork.
    ![Main Logo](docs/screenshots/main_logo.PNG)

* The artwork of Gerry the Snowman is a mix of two artworks found on [ASCII Art](https://www.asciiart.eu/holiday-and-events/christmas/snowmen)
    * Art by Hayley Jane Wakenshaw
    * Art by jb

    The final artwork was created by myself from two artworks mentioned above.

    ![Snowman Gerry](docs/screenshots/artwork_of_gerry_the_snowman.PNG)

---

## **Features**

### **User Name**
* Once the program has been executed, the welcome screen is displayed informing the user about the game name.
* The user is asked to enter their name before the game starts.

    ![Enter User Name](docs/screenshots/enter_user_name_screen.PNG)
* Only alphabetical characters are allowed when entering the user name. Special characters, numbers, etc., will not be accepted.
    ![Player Name Not Alphabet Letters](docs/screenshots/player_name_alphabet_characters_only.PNG)
* In addition, the user name cannot be longer than 20 letters.
    ![Player Name Too Long](docs/screenshots/player_name-max_20_characters.PNG)
* If the user name has an incorrect format (blank), an appropriate message will be displayed on the screen.
    ![Player Name Blank](docs/screenshots/player_name-blank.PNG)











