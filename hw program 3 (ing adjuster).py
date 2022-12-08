#This program is meant to convert a cookie recipe, depending on how many cookies
#one wants to make

#create a variable for the original amount of 48 cookies
original_amnt = 48

#find out out how many cookies customer wants, and set it as an integer variable
desired_amnt = int(input('How many cookies would you like to bake? '))

#create an equation for the ratio of how many cookies customer wants, to the original recipe
ratio = (desired_amnt / original_amnt)

#create variables for the sugar, butter and flour
sugar = 1.5
butter = 1
flour = 2.75

#create variables for the adjusted ingrediants, based on the ratio of desired cookies
adj_sugar = format(sugar * ratio, '.2f')
adj_butter = format(butter * ratio, '.2f')
adj_flour = format(flour * ratio, '.2f')

#display the adjusted ingrediants
print('In order to bake ', desired_amnt, 'cookies, use adjusted recipe below: ')
print('Sugar: ', adj_sugar, 'C')
print('Butter:', adj_butter, 'C')
print('Flour: ', adj_flour, 'C')

ex = adj_sugar * adj_butter
print(ex)















                                      
