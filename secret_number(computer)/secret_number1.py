import random

def guess(x):
    random_no = random.randint(1,x)
    guess = 0
    while (guess != random_no):
        guess = int(input(f'Guess my Number,it is between 1 and {x} '))
        if(guess< random_no):
            print('Sorry, Guess Again.Your guess is low.')
        elif(guess> random_no):
            print('Sorry, guess Again.Your guess is higher.')
    
    print(f'You guessed it Wohooo!!😨. it was {random_no}')
guess(10)