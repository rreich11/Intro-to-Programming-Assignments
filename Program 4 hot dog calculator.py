#This program is to calculate how many packages of buns annd hotdogs are needed based on the number of guests and how many hotdogs each one will get

#named constant for hot dog and bun package size
HOT_DOG_PKG = 10
BUN_PKG = 8

#ask how many guests will be at barbeque and how many hot dogs each one will get
guests = int(input('How many guests will you be hosting by your barbeque tonight? '))
hot_dogs_per_guest = int(input('Enter the number of hot dogs that will be given to each of your guests: '))

#find total amount of hot dogs needed
needed_hot_dogs = guests * hot_dogs_per_guest

#calculate number of packages of hot dogs are needed
amnt_dog_pkg = needed_hot_dogs // HOT_DOG_PKG             #divide the total amount of needed hot dogs by how many dogs come in a package(10)
remainder_amnt_dog = needed_hot_dogs % HOT_DOG_PKG        #calculate the remaining amount of hot dogs that are needed, beyond what comes in a package 
if remainder_amnt_dog > 0:                                #if there are remaining hot dogs, 
    final_amnt_dog_pkg = amnt_dog_pkg + 1                 #add 1 more package of hot dogs to total needed amount
    calc_extra_dogs = HOT_DOG_PKG - remainder_amnt_dog    #calculate how many hot dogs will be left in package uneaten, by subtracting remainder from package size(10)
    extra_dogs = calc_extra_dogs                          #make a variable for the extra left over hot dogs
else:
    final_amnt_dog_pkg = amnt_dog_pkg                     #if no extra hot dogs are needed, the set a variable to no extra hot dogs
    extra_dogs = ('no')

#find total amount of buns needed
needed_buns = needed_hot_dogs

#calculate how many packages of buns are needed
amnt_bun_pkg = needed_buns//BUN_PKG                      #divide, getting a qhole number, the total amount of needed buns, by how many buns come in a package
remainder_amnt_bun = needed_buns % BUN_PKG               #calculate the remaining amount of buns that are needed
if remainder_amnt_bun > 0:                               #if there are remaining buns
    final_amnt_bun_pkg = amnt_bun_pkg + 1                #add 1 more package of buns to total needed amount
    calc_extra_buns = BUN_PKG - remainder_amnt_bun       #calculate how many buns will be left in package uneaten, by subtracting remainder from package size(8)
    extra_buns = calc_extra_buns                         #make a variable for the extra left over buns
else:
    final_amnt_bun_pkg = (amnt_bun_pkg)                 #if no extra buns are needed, then set a variable to no extra buns
    extra_buns = ('no')


#display final hot dog packages needed, bun packages needed, how many hot dogs and buns will be left over
print ('In order to have enough hot dogs for your guests, you will need to buy',final_amnt_dog_pkg, 'hot dog packages and',
       final_amnt_bun_pkg, 'packages of buns')
print ('your will have', extra_dogs, 'leftover hot dogs and', extra_buns, 'remaining buns.')
