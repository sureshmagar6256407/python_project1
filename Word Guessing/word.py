import random
class WordGuess: 
    def __init__ (self,words) :
        self.words = words
        self.word  = random.choice(words)
        self.guesess= ""
        self.turns = 12

    def GetUserName(self,name) : 
        print(f"Good luck! ,{name}")

    def start(self) : 
        print("\n guess the characters")   
        while self.turns >0 : 
            failed  = 0  

            for char in self.word : 
                if char in self.guesess : 
                    print(char,end=" ")
                else : 
                    print("-",end=" ")
                    failed += 1
            print()

            if failed == 0 : 
                print("you win")
                print("the word is : " ,self.word)
                break  

            guess  = input("Guess a characer : ").lower()

            if len(guess) != 1  : 
                print("please enter a single character.")
                continue  

            if guess in self.guesess : 
                print("you already guesed that character.")
                continue  

            self.guesess += guess 

            if guess not in self.word : 
                self.turns -= 1  
                print("wrong")
                print("you have" , self.turns , "more guesses")

                if self.turns == 0 : 
                    print("you lose")
                    print("the word was : " ,self.word)



words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
name = input("Enter your name :  " ) 
w1 = WordGuess(words)
w1.GetUserName(name)
w1.start()