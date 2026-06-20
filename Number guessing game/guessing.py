import random  

class Guessing : 
    print()
    print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")
    print()

    def __init__ (self, low ,high , num,ch,gc) : 
        self.low=  low 
        self.high  = high  
        self.num  = num 
        self.ch  = ch 
        self.gc  =gc 

    def remind(self) : 
        print(f"\nYou have 7 chances to guess the number between {self.low} and {self.high} . Let's Start !")

    def StartGame(self) : 
        while self.gc < self.ch  : 
            self.gc += 1  
            guess   = int (input("Enter  your guess :: ")) 

            if guess  == self.num : 
                print(f"Correct ! the number is {self.num}. You guessed it in {self.gc} attempts")
                break
            elif self.gc >= self.ch and guess !=self.num : 
                print(f"sorry! The number was {self.num} . Better luck next time.")

            elif guess > self.num : 
                print(f"too high ! Try a lower number")

            elif guess < self.num : 
                print(f"Too low! Try a higher number.")
       

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))
num  = random.randint(low,high)
#total allowed chance
ch = 7 
#guess Count
gc   = 0 

g1   = Guessing (low,high,num,ch ,gc)
g1.remind()
g1.StartGame()

