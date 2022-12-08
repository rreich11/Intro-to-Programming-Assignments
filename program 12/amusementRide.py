#this class represents a ride in an amusement park

class AmusementRide:

    #initialize the data attributes
    def __init__(self, nameRide, minHeight, minAge, numTickets):
        self.__nameRide = nameRide
        self.__minHeight = minHeight
        self.__minAge = minAge
        self.__numTickets = numTickets
        
    #create setters for attributes
    def set_nameRide(self, nameRide):
        self.__nameRide = nameRide

    def set_minHeight(self, minHeight):
        self.__minHeight = minHeight

    def set_minAge(self, minAge):
        self.__minAge = minAge

    def set_numTickets(self, numTickets):
        self.__numTickets = numTickets
        
    #create getters for attributes
    def get_nameRide(self):
        return self.__nameRide 

    def get_minHeight(self,):
        return self.__minHeight 

    def get_minAge(self):
        return self.__minAge 

    def get_numTickets(self):
        return self.__numTickets

    #calculate cost per ride, return cost
    def calc_cost(self, ticketPrice):#get current ticket price from main
        rideCost = self.__numTickets * ticketPrice
        return rideCost  ###QUESTION: can return something thats not atrribute? where does it go???

    #see if can ride, return true or false
    def can_give_ride(self, height, age):
        if height >= self.__minHeight and age >= self.__minAge:
            return True
        else:
            return False

    def __str__(self):
        return 'Ride Name: ' + str(self.__nameRide) + '\nMinimum Height: ' + str(format(self.__minHeight, ',.1f') ) + '\nMinimum Age: ' + str(self.__minAge) + '\nNumber of Tickets: ' + str(self.__numTickets)
    
    
    
