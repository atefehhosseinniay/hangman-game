import random
import re
from typing import List


class Hangman():
    """
    here we define des atributes of object.
    These atributes are:

    possible_words: attribute that contains a list of words.
    Out of these words, one will be selected as the word to find.

    word_to_find: attribute that contains a list of strings.
    Each element will be a letter of the word.

    lives: attribute that contains the number of lives that the player still has left.

    well_guessed_letters: attribute that contains a list of strings where each element will be a letter guessed by the user.

    wrongly_guessed_letters: attribute that contains a list of strings where each element will be a letter guessed by the
                             user that is not in the word_to_find.

   turn_count: attribute that contain the number of turns played by the player.

   error_count: attribute that contains the number of errors made by the player.

    """

    possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find: List[str] = []
    lives: int = 5
    well_guessed_letters: List[str] = []
    wrongly_guessed_letters: list = []
    turn_count: int = 0
    error_count: int = 0

    def play(self):

        """
        The play() method ask player to enter a letter. If player enter a charachter that is not a alphabet letter
        it will ask again a new Try. If player enter more than one letter, it will ask to enter only one letter.
        If player enter a letter that has been guessed before it ask to Try a new one.
        If the player guessed a letter well, it set it in the well_guessed_letters list. If not, it add it to the
        self.wrongly_guessed_letters list and add 1 to self.error_count and decrease self.lives by one .
        each time the player enter a letter, self.turn_count is increased by one.
        """
        path: chr = r"\b[a-z]\b"

        guess: chr = input("Please enter a letter: ")
        guess = guess.lower()

        self.turn_count += 1

        if len(guess) != 1:
            print('please enter only one letter.Try again: ')
        elif re.search(path, guess) is None:
            print(f'{guess} is not a letter.Try again:')
        elif (guess in self.wrongly_guessed_letters):
            print(f'{guess} has been guessed before.Try a new one:')

        if guess in self.word_to_find:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == guess:
                    self.well_guessed_letters[i] = guess
        else:
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count += 1

        print(" ".join(self.well_guessed_letters))

    def start_game(self):
        """
        this method will choose a word among possible_words list at random and
        will create a list of single letters of this word.It will create a list "self.well_guessed_letters"
        with a length equal to the length of the word_to_find with '_' as element.
        Then it will call play() until the game is over. if lives is equal to 0 it will call game_over().
        If the player guessed well all the letters of word_to_find, it will call well_played().
        """

        self.word_to_find: List[str] = list(random.choice(self.possible_words))

        print(f"let's go.The word is of {len(self.word_to_find)} letters.")

        self.well_guessed_letters = list("_") * len(self.word_to_find)

        while True:
            # keep asking the player untill all letters are guessed.

            if self.well_guessed_letters != self.word_to_find:
                self.play()
                if self.lives == 0:
                    self.game_over()
                    break

            else:
                self.well_played()
                print(*([i for i in self.well_guessed_letters]))
                break

            print(f"well guessed letters: {' '.join(self.well_guessed_letters)}\n"
                  f'wrongly gessed letters: {self.wrongly_guessed_letters}\n'
                  f'lives: {self.lives}\n'
                  f'count errors: {self.error_count}\n'
                  f'count turns: {self.turn_count}\n'
                  )

    def game_over(self):

        """
        method that will stop the game and print "game over..."
        """

        print("game over...!!!")

    def well_played(self):
        """
        This method will print you found the word and count of turns and count of errors
        if the player guesses well the word to fin.
        """

        print(
            f' You found the word: {" ".join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!')



