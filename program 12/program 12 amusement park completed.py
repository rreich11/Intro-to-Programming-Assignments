#This program invokes all methods of amusementRide class

import amusementRide

def main():
    
    #initialize variable to hold object after loop                           
    ride1 = 'ride 1'  #amusementPark instance
    ride2 = 'ride 2'  #amusementPark instance
    
    for num in range(2):
        #information for ride1
        print('Enter the information for ride ', num+1, ': ', sep='')
        #get the information to pass to class
        nameRide = input('Enter the name of the ride: ')
    
        minHeight = float(input('Enter the minimum allowed height, in feet, to go on the ride: '))
        #validate
        minHeight = invalid_float(minHeight)
                                              
        minAge = int(input('Enter the minimum age allowed on this ride: '))   
        #validate
        minAge = invalid_int(minAge)                
    
        numTickets = int(input('Enter the number of tickets required to go on the ride: '))    
        #validate
        numTickets = invalid_int(numTickets)
            
        #create instance of AmusementRide Class, pass the parameters
        ride = amusementRide.AmusementRide(nameRide, minHeight, minAge, numTickets)
        
        #if its the first loop, assign object to ride 1, if its second loop, assign object to ride2
        if num == 0:
            ride1 = ride
        else:
            ride2 = ride

        print()
        
    #display information for ride 1
    display_info_ride1(ride1)
    
    #display information for ride 2
    display_info_ride2(ride2)

    #change information for ride 1
    print('Reenter information for ride one')
    new_nameRide = input('Enter a new name: ')
    #change objects attribute
    ride1.set_nameRide(new_nameRide)
    
    new_minHeight = float(input('Enter a new minimum height: '))
    #validate
    new_minHeight = invalid_float(new_minHeight)
    #change the objects attribute
    ride1.set_minHeight(new_minHeight)
    
    new_minAge = int(input('Enter a new minimum age: '))    
    #validate
    new_minAge = invalid_int(new_minAge)
    #change the objects attribute
    ride1.set_minAge(new_minAge)
    
    new_numTickets = int(input('Enter a new number of tickets: '))    
    #validate
    new_numTickets = invalid_int(new_numTickets)
    #change the objects attribute
    ride1.set_numTickets(new_numTickets)

    #display the new information for ride 1
    display_new_info_ride1(ride1)

    #calculate the cost to ride each ride and display formatted
    ticket_price = float(input('Enter the cost per ticket, to figure out how much the ride costs: '))
    #validate ticket price
    ticket_price = invalid_float(ticket_price)
        
    ride_cost_1 = ride1.calc_cost(ticket_price)
    ride_cost_2 = ride2.calc_cost(ticket_price)
    print('To ride the ', ride1.get_nameRide(), ' the total price is, $', format(ride_cost_1, ',.2f'), sep='')   
    print('To ride the ', ride2.get_nameRide(), ' the total price is, $', format(ride_cost_2, ',.2f'), sep='')
    print()

    #see if can ride ride
    print('Enter the height and age of rider to see if can ride.')
    print()
    
    #get height
    height = float(input('Height: '))
    #validate height
    height = invalid_float(height)

    #get age
    age = int(input('Age: '))
    #validate age
    age = invalid_int(age)

    #get the status of rider, if can ride
    status1 = ride1.can_give_ride(height, age)
    status2 = ride2.can_give_ride(height, age)

    #if status is true, can ride and if not, display msg can't ride
    if status1:
        print('Yes, rider can ride the ' , ride1.get_nameRide(),'!', sep='')
    else:
        print('Sorry, rider can\'t ride the ', ride1.get_nameRide(),'...', sep='')

    if status2:
        print('Yes, rider can ride the ', ride2.get_nameRide(),'!', sep='')
    else:
        print('Sorry, rider can\'t ride the ', ride2.get_nameRide(),'...', sep='')
    print()

    #display value of data attributes with __str__ method
    print('Here is the final entered information for the two rides: ')
    print('Ride One:')
    print(ride1)
    print()
    print('Ride two:')
    print(ride2)

def invalid_int(value):
    #validate int input
    while value < 1:
        value = int(input('Invalid, please reenter: '))
    return value
    
def invalid_float(value):
    #validate float input
    while value < 1:
        value = float(input('Invalid, please reenter: '))
    return value
        
def display_info_ride1(ride1):
    #display information for ride 1
    print('Here is the information entered for ride one:')
    print('Name of ride: ', ride1.get_nameRide())
    print('Minimun Height: ', ride1.get_minHeight())
    print('Minimum Age: ', ride1.get_minAge())
    print('Number of Tickets to Ride: ', ride1.get_numTickets())
    print()

def display_info_ride2(ride2):          
    #display information for ride 2 
    print('Here is the information entered for ride two:')
    print('Name of ride: ', ride2.get_nameRide())
    print('Minimun Height: ', ride2.get_minHeight())
    print('Minimum Age: ', ride2.get_minAge())
    print('Number of Tickets to Ride: ', ride2.get_numTickets())
    print()

def display_new_info_ride1(ride1):
    #display the new information for ride 1
    print()
    print('Here is the new information entered for ride one:')
    print('Name of ride: ', ride1.get_nameRide())
    print('Minimun Height: ', ride1.get_minHeight())
    print('Minimum Age: ', ride1.get_minAge())
    print('Number of Tickets to Ride: ', ride1.get_numTickets())
    print()
  
    

    

            
main()
