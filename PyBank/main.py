#import OS moudule
import os

#module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

number_of_months = 0
profit_loss = 0
#previous_pl = int(row[1])
#current_pl = int(row[1])-previous_pl
net_change = []
month_of_change = []


#with open(csvpath, 'r') as file_handler:
    #lines = file_handler.read()
    #print(lines)
    #print(type(lines))


    
#The total number of months included in the dataset
with open(csvpath, 'r') as file:
    csv_reader_object = csv.reader(file)
    #first_row = next(csv_reader_object)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    first_row = next(csv_reader_object)
    for row in csv_reader_object:
        number_of_months += 1
        #The net total amount of "Profit/Losses" over the entire period
        profit_loss += int(row[1])
        previous_pl = int(first_row[1])
        current_pl = previous_pl - int(row[1])
        #test_profit_loss = int(row[1])-int(row[1])
        net_change = net_change + [current_pl]
        month_of_change += [row[0]]
        print(int(row[1]))
        #print(test_profit_loss)
print("Total Months: ", number_of_months)
print(profit_loss)
print(profit_loss)
print(current_pl)
print(previous_pl)
print(net_change)
print(month_of_change)


#sum the net change list, divide by net change list to get average - outside for loop

#greatest_increase = 0 - inside for loop
#greatest_dec = 99999999  - inside for loop

    


#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period