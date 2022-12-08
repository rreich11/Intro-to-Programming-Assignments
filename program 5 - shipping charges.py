#this program is to calculate the charge of shipping

#get a package weight from customer
pkg_weight = float(input('How much does your package weigh, in pounds?'))

#determine and print the shipping cost
if pkg_weight <= 2:
    print('Your package will cost $1.50 to ship.')
elif pkg_weight <=6:
    print('Your package will cost $3.00 to ship.')
elif pkg_weight <=10:
    print('Your pakage will cost $4.00 to ship.')
else:
    print('Your package will cost $4.75 to ship.')
