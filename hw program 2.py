#this program is to calculate the total amount of a meal purchased,by asking for the
#charge for the food and then calculating the amount of an 18% tip and 7% sales tax.

#ask for the charge for food
food_cost= float(input('Enter the cost of your food: $'))

#to find tip, multiply food_cost by 18%
tip= (food_cost * .18)

#to find sales tax, multiply food_cost by 7%
salesTax=(food_cost * .07)

#calculate the total cost of meal by adding tip and salestax to food cost
meal_total=(food_cost + tip + salesTax)

#display the tip,salestax and meal total
print ('Tip: $',format(tip, '.2f'), sep='')
print ('Sales tax: $',format( salesTax,'.2f'), sep='')
print ('The total cost of your meal: $', format( meal_total,'.2f'), sep='')
                                    



