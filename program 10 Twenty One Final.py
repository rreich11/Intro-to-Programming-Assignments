import random

def main():
    #display start up message
    start_up_message()

    #set up loop so player has option to keep playing
    play_again = 'y'
    while play_again.lower() == 'y':

        #choice = 1 so loop for menu forced to execute at least once
        choice = 1

        #accumalator variable to keep track of total score
        total_card_score = 0

        #as long as users choice is one, and score is under
        #21 the loop should continue
        while choice == 1 and total_card_score < 21:

            #draw a card
            player_card = drawing_card()

            #convert card to string and display
            card_string = card_as_string(player_card)
            display_card(card_string)

            #if card is equal to 11,12,13 make it equal to ten
            card_value = actual_card_value(player_card)

            #add card value to total card score, to keep track of score
            total_card_score += card_value

            #only display the menu and card total if the total card score is less than 21
            if total_card_score < 21:
                #display card total with message
                display_card_total(total_card_score)
                
                #display menu, menu returns players choice
                choice = menu()
                
        #if player chooses choice 2 from menu, freeze game
        if choice == 2:
            #display freeze message
            display_freeze_message()

        #if player chooses choice 3 display quit message
        elif choice == 3:
            display_quit_message()

        print('Game is over...')

        #call the computers logic and display it's cards
        final_computer_score = computer_logic()

        #display the results of the game
        results_of_game(total_card_score, final_computer_score)

        #end the loop
        play_again = play_game_again()
            
            
    
def start_up_message():
    #display start up message with game instructions
    print('Welcome to "Twenty One!" The object of this game is to draw as close '
         'to twenty one, withought going over. When prompted, you will draw a '
         'card, you can continue drawing cards, until you choose to stop and  '
         'press freeze. However, be careful that the added value of your '
         'cards does not exceed 21. You will be playing against the computer. '
         'GOOD LUCK!')
    input('Press enter to begin the game: ')
    print()
    
def drawing_card():
    #assign a random card and return to main function
    card = random.randint(1,13)
    return card

def card_as_string(card):
    #if card is 1,11,12, or 13, assign a face card to it as string
    if card == 1:
        face_card = 'Ace'
    elif card == 11:
        face_card = 'Jack'
    elif card == 12:
        face_card = 'Queen'
    elif card == 13:
        face_card = 'King'
    else:
        face_card = str(card)
        
    #assign a suit to card, the function returns the card_suit
    card_suit = suit_of_card()
    
    #make card a string, and return it to main function
    card_string = face_card + card_suit   
    return card_string

def suit_of_card():
    #assign a suit to card
    suit = random.randint(1,4)

    if suit == 1:
        card_suit = ' Of Hearts'
    elif suit == 2:
        card_suit = ' of Diamonds'
    elif suit == 3:
        card_suit = ' of Spades'
    else:
        card_suit = ' of Clubs'
        
    #return the suit to card_as_string function
    return card_suit

def actual_card_value(card):
    #if card is equal to 11,12,13, make value of card equal to ten
    if card == 11:
        card_value = 10
    elif card == 12:
        card_value = 10
    elif card == 13:
        card_value = 10
    else:
        card_value = card
    
    #return the card value to function that called it
    return card_value

def display_card(card_string):
    print()
    print('You drew a', card_string)

def display_card_total(total_card_score):
    print('So far your total card score is ',total_card_score,
                  ', press enter to display the menu. Decide if you\'d like '
                  'to draw again, or freeze ', sep='', end='')
    input()
    print()
    

def computer_logic():
    #this function is computers logic playing game and displaying its cards

    #accumalator variable to keep track of computers total score
    computer_score = 0

    print()
    print('The computers drawn cards:')
    print('---------------------------')

    #computer will continue drawing card until total score is 15
    while computer_score < 15:
        card = drawing_card()
        card_string = card_as_string(card)
        
        #display computers cards
        print(card_string)

        #value of card if card is equal to 11,12,13
        card_value = actual_card_value(card)
        
        #add the card value to total score
        computer_score += card_value
        
    #returns the computer score to main function
    return computer_score

def results_of_game(total_card_score, final_computer_score):
    
    #Calculate difference between final score and 21
    player_score_difference = 21 - total_card_score
    computer_score_difference = 21 - final_computer_score

    print()
    print('Your final score is: ', total_card_score, '\nThe computers final '
          'score is: ', final_computer_score)
    print()

    #if computer and player score 21 = tie
    if total_card_score == 21 and final_computer_score == 21:
        print('Congragulations, you and the computer both scored a perfect '
              'score of 21!!! You tied the computer!')
    #if player total score is 21 = player won
    elif total_card_score == 21:
        print('Congragulation, you have a perfect score of 21!! you just won '
              'the game!!!')
        #if computer score over 21 = comp lost
        if final_computer_score > 21:
            print('The computer scored over 21 and lost the game...')
        #if computer score less than 21= comp also won
        else:
            print('The computer also won the game, with a score less than 21...')
    #if computer score 21 = comp won
    elif final_computer_score == 21:
        print('The computer scored a perfect score of 21, the computer won the game...')
        #if player score over 21 = player lost
        if total_card_score > 21:
            print('You scored over 21 and lost the game... better luck next time!')
        #if player score under 21 = player also won
        else:
            print('You also won the game with a score less than 21!')
    #if computer and player score over 21 = both lost
    elif total_card_score > 21 and final_computer_score > 21:
        print('You and the computer both scored over 21, you both lost the game...')
    #if player score over 21 = player lost, computer score less than 21 = comp won
    elif total_card_score > 21:
        print('You scored over 21, you lost the game...')
        print('The computer scored less than 21, the computer won the game...')
    #if computer score over 21 = comp lost, player score less than 21 = player won
    elif final_computer_score > 21:
        print('You scored less than 21, you won the game against the computer!')
        print('The computer scored over 21, and lost the game...')    
    #if player and computer score less than 21 
    elif total_card_score < 21 and final_computer_score < 21:
        #if player and computer score equal = tie
        if player_score_difference == computer_score_difference:
            print('You and the computer tied with the same score less than 21!!')
        #if player scores closer to 21 than computer = player won
        elif player_score_difference < computer_score_difference:
            print('Congragulations, you won the game against the computer, you '
                  'scored closer to 21 without going over!!')
        #if computer scores closer to 21 than player = comp won
        else: 
            print('The computer won this game. The computer scored closer to 21 '
             'without going over...')
    
def menu():
    #display menu
    print('1. Draw a card')
    print('2. Freeze')
    print('3. Quit the game')
    print()
    
    #accept choice from user 
    player_choice = int(input('Enter your choice from the menu above: '))
    
    #validate players menu choice, validate_menu_choice returned a value
    player_choice = validate_menu_choice(player_choice)

    #return players choice to main function
    return (player_choice)
    
def validate_menu_choice(player_choice):
    #validate choice is 1 2 or 3
    while player_choice != 1 and player_choice != 2 and player_choice != 3:
        player_choice = int(input('You entered an invalid choice, '
                                  'please reenter a choice: '))

    #return users choice to menu function
    return (player_choice)

def display_freeze_message():
     print('You chose to freeze the game, and stop drawing cards.')

def display_quit_message():
    print('You chose to quit this game')

def play_game_again():
    print()
    #Give user option to play game again
    play_again = input('Would you like to play again? Press y '
                         'for yes, or any other key to exit. ')
    #return users choice
    return play_again    

main()
