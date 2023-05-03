# This script will calculate inflation adjusted salary/price etc.
# Please edit the start data below and run this script
# Only works for Swedish [SEK] Inflation.
from datetime import datetime
from statistics import mean

### Edit these values ###
#----------------------------------------------------------------------#
# "start" of either employment or latest salary raise etc. [int]
# cannot be set to current month/year
# month is defined in [1-12]
start_month = 8
start_year = 2019
start_salary = 40000
current_salary = 44600
### Current Date ###
# Can only be set to latest valid inflation data point in inflation_by_month below.
current_month = 3
current_year = 2023
#current_month = int(datetime.today().strftime('%m'))
#current_year = int(datetime.today().strftime('%Y'))
#----------------------------------------------------------------------#

### Swedish Inflation data ###
# https://www.riksbank.se/sv/penningpolitik/inflationsmalet/inflationen-just-nu/
# TODO: Add new data entries when available, or add older data if needed.
inflation_by_month = {
    '2016':	[1.6, 1.1, 1.5, 1.4, 1.1, 1.5, 1.4, 1.4, 1.2, 1.4, 1.6, 1.9],
    '2017':	[1.6, 2.0, 1.5, 2.0, 1.9, 1.9, 2.4, 2.3, 2.3, 1.8, 2.0, 1.9],
    '2018':	[1.7, 1.7, 2.0, 1.9, 2.1, 2.2, 2.2, 2.2, 2.5, 2.4, 2.1, 2.2],
    '2019':	[2.0, 1.9, 1.8, 2.0, 2.1, 1.7, 1.5, 1.3, 1.3, 1.5, 1.7, 1.7],
    '2020':	[1.2, 1.0, 0.6, -0.4, 0.0, 0.7, 0.5, 0.7, 0.3, 0.3, 0.2, 0.5],
    '2021':	[1.7, 1.5, 1.9,	2.5, 2.1, 1.6, 1.7,	2.4, 2.8, 3.1, 3.6, 4.1],
    '2022':	[3.9, 4.5, 6.1,	6.4, 7.2, 8.5, 8.0,	9.0, 9.7, 9.3, 9.5,	10.2],
    '2023':	[9.3, 9.4, 8.0],   # TODO Update me later
}

### Prepare the loop ###
month_counter = start_month
year_counter = start_year
adjusted_salary = start_salary
inflation_list = []

print(f'current_month: {current_month}')
print(f'current_year: {current_year}')
#print(f'month_counter: {month_counter}')
#print(f'year_counter: {year_counter}')

while year_counter <= current_year:
    # New salary after 1 month = salary + salary * (1 + inflation_by_month / 100) / 12
    adjusted_salary = adjusted_salary * (1+inflation_by_month[str(year_counter)][month_counter-1]/100/12)
    # print(f'month_counter: {month_counter}')
    print('Adjusted salary after month: ' + str(year_counter) +
    '-' + str(month_counter+1) + ': ' + str(round(adjusted_salary)) + ' kr')

    # Add up monthly inflation to only calculate average 
    inflation_list.append(inflation_by_month[str(year_counter)][month_counter-1])

    month_counter += 1
    if month_counter > 11:
        month_counter = 0
        year_counter += 1

    # Exit loop when month_counter exeeds current_month in last year
    if year_counter == current_year and month_counter == current_month:
        break

Average_Inflation = mean(inflation_list)


### Print ###
print('----------------------------------------------')
print('Inflation adjusted salary at: ' + str(current_year) + '-' + str(current_month) +
' should be: ' + str(round(adjusted_salary)) + ' kr')
print(f'Monthly average inflation since {start_year}-{start_month} was: '+ str(round(Average_Inflation,2))+'%')

print('Current salary / Inflation adjusted salary: '+ str(100*round(current_salary/adjusted_salary,2)) +'%')