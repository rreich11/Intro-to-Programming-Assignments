import random

#this program is a dice game between the computer and the user

#display message to user, about the game
print('The object of this game is to roll the die with the higher value, the most times. ')
print()

#prompt the user to press enter to start the game/roll the die
name = input('What is your name? ')
print(name, 'press enter to begin playing. Press enter each round to roll the die. ', end='')
input()
print()

play_again = 'y'

while play_again.lower() == 'y':

    #set an accumalator cariable to keep track of winning rounds  
    comp_win = 0
    user_win = 0

    #create a loop that repeats for ten rounds of the game
    for spin in range(10):
    
        #display round number
        print('Round', spin + 1)
        print('------------------------',end='')
    

        #generate a random roll for user and display it
        #input('press enter to roll the die')
        input()
        user_roll = random.randint(1,6)
        print(name, 'rolled: ', user_roll)

        #generate random roll for computer and diplay it
        comp_roll = random.randint(1,6)
        print('The computer rolled: ', comp_roll)

        
        
        if comp_roll == user_roll:
            print('This round is a tie, there are no winners of this round.')
        elif comp_roll > user_roll:
            print('The computer wins this round!')
            comp_win += 1
        else:
            print(name, 'wins this round!!')
            user_win +=1
        print()
    
    print('------------------------')
    if comp_win > user_win:
        print('The computer has won the most rounds!')
    elif user_win > comp_win:
        print(name, 'has won the most rounds!!!!')
    else:
        print('This game was tied!')
        
    

    #end game
    print()
    play_again = input("If you'd like to play again, press y ")
    print()

    


