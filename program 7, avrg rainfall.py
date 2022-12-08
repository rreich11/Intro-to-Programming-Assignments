#this program is to calculate the average rainfall over a period of years

#get the number of years
num_years = int(input('Enter the number of years you would like to calculate the average rainful for,'
                      ' you must enter at least one year: '))

#validate input is at least one year
while num_years < 1:
    num_years = int(input('You entered an invalid number of years, please reenter a number: '))

#set accumalator for total rainfall
total_rain = 0

#loop for number of years
for year in range(num_years):
    print('Year', year + 1, end='')
    print(':')
    
    #loop for each month
    for month in['January', 'February', 'March', 'April', 'May',
                 'June', 'July', 'August', 'September', 'October', 'November', 'December']:

        #ask user to enter rainful per month
        print('Enter the amount of rainful, in inches, for ', month, ': ', sep='',  end='')
        amnt = float(input())

        #calculate total amount of raifall
        total_rain = total_rain + amnt
        
#calculate how many months entered rainfall for
total_months = num_years * 12

#calculate average rainfall per month
avrg_rain_per_month = total_rain / total_months

#display total number of months calculated for, and how much rain fell all together
print('In the past', total_months, 'months,', format(total_rain, ',.2f'), 'inches of rain fell.')
print('The average monthly rainful during these', num_years, 'years entered is,', format(avrg_rain_per_month, ',.2f'), 'inches per month.')
        
    
