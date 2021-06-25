import random
from IPython.display import clear_output

class Word:
    # initialize our word by passing in a word_dict
    def __init__(self, word_dict):
        self.word_dict = word_dict
        
    # accepts a string, which is an option from the word_dict, chosen using an input()
    def choose_word(self, chosen_category):
        return random.choice(self.word_dict[chosen_category])
    
    # take the raw word and convert into an underscored string
    def display_word(self, word_to_guess):
        return ['_' for letter in list(word_to_guess)]
    
class Game:
    # start the game with no incorrect guess (to be incremented upon incorrect guess)
    incorrect_guesses = 0
    # keeps track of all guessed letters
    chosen_letters = set()
    
    words = {
        "fruit": ["watermelon", "kiwi", "apple", "mango", "dragonfruit"],
        "business": ["contract", "building", "desktop", "office", "executive"],
        "travel": ["airplane", "sand", "cruise", "sunscreen", "beach"]
    }
    
    
    @classmethod
    def run(self):
        word = Word(Game.words)
        
        # checking if the category the we choose is valid or not
        valid = False
        while not valid:
            try:
                print(f"Categories => {', '.join([i.title() for i in list(word.word_dict)])}")
                category = input("What category would you like to choose from? ").lower()
                # if whatever we type into the input function is not an alpha character
                if not category.isalpha():
                    clear_output()
                    # rerun the steps
                    print('You must enter a valid category')
                else:
                    # choose a random word frmo the category
                    word_to_guess = word.choose_word(category)
                    # build the display from it ("beach" => _ _ _ _ _)
                    display_word = word.display_word(word_to_guess)
                    # break out of this while loop
                    valid = True
            # if either there was an error in the try block, or if that category is not found
            except:
                clear_output()
                print("You must enter a valid category")
                
        # upon successful category choice, start game login
        done = False
        # determine if game should continue to run if thelist(word_to_guess) => ['b', '_', '_', 'c', 'h'] == display_word => ['b', '_', '_', 'c', 'h']
        while not done and not list(word_to_guess) == display_word:
            # if it is
            if word.display_word(word_to_guess) == list(word_to_guess):
                # end the game
                done = True
            # otherwise, continue the game
            # check for all conditions to end the game FIRST
            else:
                # check if number of incorrect guesses is not 7
                if self.incorrect_guesses > 6:
                    # end the game
                    print(f"You didn't guess the word. Here's word: {word_to_guess}")
                    break
#                 print("=" * 50)
#                 print(f"DEBUGGER: {word_to_guess}")
                print("=" * 50)
                print(f"You have {self.incorrect_guesses}/7 tries remaining. Choose wisely! ")
                print(" ".join([letter for letter in display_word]))
                
                # ask the user to type in a choice
                letter_to_guess = input("Guess a letter. Type 'quit' to exit program").lower()
                clear_output()
                # if the letter choice was an alpha character
                if letter_to_guess.isalpha():
                    # if the user types quit, end the program
                    if letter_to_guess == 'quit':
                        break
                    # if the user does not type quit, continue the program
                    else:
                        # if the letter we choose was not already chosen
                        if letter_to_guess not in self.chosen_letters:
                            # if letter we're looking for can be found in word_to_guess  
                            if letter_to_guess in word_to_guess:
                                # make sure to replace all instances of every letter
                                for idx, letter in enumerate(word_to_guess):
                                    # if the letter has been found at that specific index
                                    if letter == letter_to_guess:
                                        # find that letter at the index of our display_word list and change
                                        # it to the letter we guessed
                                        display_word[idx] = letter_to_guess
                                        # add the letter choice to the chosen_letters set
                                        self.chosen_letters.add(letter_to_guess)
                                continue
                            # if letter we're looking for cannot be found in word_to_guess 
                            else:
                                print("That was an incorrect choice.")
                                # increment the number of incorrect guessed by 1 for each incorrect guess
                                self.incorrect_guesses+=1
                                # add the letter choice to the chosen_letters set
                                self.chosen_letters.add(letter_to_guess)
                                continue
                        # if the letter we choose was already chosen
                        else:
                            input("You have already selected that letter. Press any key to continue and try again")
                            continue
                # if the letter choice was not an alpha character
                else:
                    input("Invalid submission. Press any key to continue and try again.")
                    continue
            # if at any point, we tell our application to set done = True, it breaks the main "game logic" while loop
            done = True
        print("Thanks for playing! You guess the word. See you next time!")
                
Game.run()