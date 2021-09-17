import random
winning_number =  random.randint(1,100)
guess = 1
guess_number=int(input("Guess any no. between 1 to 100:"))
game_over = False 

while not game_over:
     if guess_number == winning_number:
        print(f"YOU WIN, and You guess this no. in {guess} times")
        game_over = True
     else:
        if guess_number < winning_number:
             print("TOO LOW")
             guess += 1
             guess_number=int(input("Guess any no. between 1 to 100:"))
        else:
            print("TOO HIGH")
            guess += 1
            guess_number=int(input("Guess any no. between 1 to 100:"))
