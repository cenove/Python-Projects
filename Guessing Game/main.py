import random

def number_picker():
    hearts = 3
    random_number = random.randrange(1,10) #idk why but the last property 'step' is so odd for me


    print("Guess the number between 1 to 10: ")
    number_guessed = int(input())
    
    while random_number != number_guessed and hearts > 0:


        #the meme I'm talking about is this one: https://www.youtube.com/shorts/_AHpRNJLamc
        if number_guessed == 21:
            print("-------------------------")
            print("You stupid")
            print("No, I'm not")
            print("What is 9 + 10? ")
            print("21")
            print("You stupid")
            print("-------------------------")
            print("You got your meme, now try again: ")
            number_guessed = int(input())
        
        elif number_guessed >= 11 and number_guessed != 21:
           print("Only use numbers between 1 to 10 and no letters")
           number_guessed = int(input())
        
        else:
            print("Incorrect try again: ")
            hearts -= 1
            print(f"You still have {hearts} heart(s)")
            number_guessed = int(input())
    
    if hearts == 0:
        print("Game Over!")
    
    else:
        print("You won! Congratulations :D ")

number_picker()