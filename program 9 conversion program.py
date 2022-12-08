#this program converts distance from meters

def main():

    #get the distance
    distance = float(input('Enter a distance in meters, '
                           'that you would like to convert: '))

    #validate distance is a positive number
    while distance < 0:
        distance = float(input('Error, you cannot enter a negative number, '
                               'please reenter a positive number: '))
    #display menu
    menu()

    option = int(input('Select a number from the option menu above, '
                       'and then press enter: '))

    #validate option entry
    while option != 1 and option != 2 and option != 3 and option != 4:
        option = int(input('You entered an invalid entry, '
                           'please reselect a number from the '
                           'option menu below. '))
        
    #if user chooses to end program right away,
    #without converting any number display bye message
    if option == 4:
        print('bye!')
    
    #display converted meters based on users selection    
    while option != 4:
        if option == 1:
            show_kilometers(distance)
        elif option == 2:
            show_inches(distance)
        elif option == 3:
            show_feet(distance)
        
        #display menu
        menu()

        #user should reenter selection
        option = int(input('Enter your choice: '))

        #validate option entry
        while option != 1 and option != 2 and option != 3 and option != 4:
            option = int(input('You entered an invalid entry, '
                           'please reselect a number from the '
                           'option menu below. '))

        #display bye message if user chooses to end program
        if option == 4:
            print('bye!')

    
#display menu
def menu():
        print()
        print('1. Convert to Kilometers')
        print('2. Convert to inches')
        print('3. Convert to feet')
        print('4. Quit the program')
        print()
        
#convert meters to kilometers and display
def show_kilometers(meters):
    kilometers = meters * 0.001
    print(meters, 'meters is', format(kilometers, ',.2f'), 'kilometers.')

#convert meters to inches and display
def show_inches(meters):
    inches = meters * 39.37
    print(meters, 'meters is', format(inches, ',.2f'), 'inches.')

#convert meters to feet and display
def show_feet(meters):
    feet = meters * 3.281
    print(meters, 'meters is', format(feet, ',.2f'), 'feet.')

#call the main function
main()



                       

    

