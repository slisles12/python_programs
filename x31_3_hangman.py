class Hangman:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guessed = []
        self.chances = 7
        self.next_turn()
        
    def next_turn(self):
        print("You have " + str(self.chances) + " guesses remaining.")
        print(self.get_puzzle())
        
        c = self.get_guess()
        
        self.guessed.append(c)
        if c not in self.phrase:
            self.chances -= 1
        
        if self.is_solved():
            print("You completed the puzzle!")
            print("The phrase is: " + self.phrase)
        elif self.chances == 0:
            print("You ran out of chances.")
            print("The phrase is: " + self.phrase)
        else:
            self.next_turn()

                
    def get_puzzle(self):
        puzzle = ""
        for i in range(0,len(self.phrase)):
            if self.phrase[i] == ' ':
                puzzle += ' '
            elif self.phrase[i] in self.guessed:
                puzzle += self.phrase[i]
            else:
                puzzle += '_'
        return puzzle


    def is_solved(self):
        """ Returns True if the puzzle has been solved """
        # TODO: complete this method

        
    def get_guess(self):
        """ Prompts the user to enter a character
            until they enter one they have not previously guessed
        """
        # TODO: complete this method
        

        
                    
                    