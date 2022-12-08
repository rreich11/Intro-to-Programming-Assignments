#this program is to calculate the amount of money made in pennies doubled every day

#ask how many days worked
total_days = int(input('How many days did you work? (Days worked must be greater than one) '))

#validate to make sure days worked entered is not less than one
while total_days < 1:
    total_days = int(input('You entered an invalid amount of days worked, please reenter a valid entry. '))

#display table headings
print()
print('Day \tPay Per Day')
print('------------------')

#add the first day to chart by printing it before the loop
print('1','\t','$0.01')                        #I formatted the escape sequence this way,
                                              #in order to match the output in line 26

#initialize an accumalator variable
pay_per_day = 1                               #variable for how much will be paid for each day  
total_pay = 0                                 #variable to keep track of total earned after total_days

#set a for loop to calculate how much will earn each day, by doubling pennies
for number in range (2, total_days + 1):      #the range begins from day 2, since day one is printed above
    pay_per_day = (pay_per_day) * 2
    pay_per_day_dollar = pay_per_day * .01    #multiply pennies by .01 to convert to dollars
    #display days and amount payed on that day
    print(number,'\t', ' $', format(pay_per_day_dollar, ',.2f'), sep='')

    #keep track of the total pay for all the days worked
    total_pay = total_pay + pay_per_day_dollar 
    
     


total_pay = total_pay + .01                   #add the .01 cent from the first day
                                              #that is not included in the loop

#display total earned all together
print()
print()
print( 'Your total earnings from the ', total_days, ' days you worked is, $', format(total_pay, ',.2f'), '!',sep='')
