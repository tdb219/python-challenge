#import packages
import os
import csv

#open and read csv file
pybank_csv = os.path.join('Resources', 'Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(pybank_csv, "r") as pybank_file:
    csvreader = csv.reader(pybank_file, delimiter=",")

    #skip header
    next(csvreader, None)

    #part of code borrowed from Hilary Koerner
    #as well as plenty of Google Fu
    differ = {}
    
    #prevent data from prior rows from being deleted by Python
    prior_row = next(csvreader)
    prior_date = prior_row[0]
    prior_profit_loss = int(prior_row[1])

    #create a loop that runs through the months
    for row in csvreader:
        differ[row[0]] = int(row[1]) - prior_profit_loss
        prior_date = row[0]
        prior_profit_loss = int(row[1])
    
    #Create keys to pull the maximum value and minimum values from the csv
    #Code for keys developed using guide from https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    key_max = max(differ, key= lambda x: differ[x])
    key_min = min(differ, key= lambda x: differ[x])

    #create a list of all values for Profit/Losses
    profit_loss_list = differ.values()

    #create functions to find the Average Change, Greatest Increase and Decrease in Profit
    #print the results
    profit_changes = str(sum(profit_loss_list)/month_count-1)
    float_profit_changes = float(profit_changes)
    round_profit_changes = round(float_profit_changes,2)
    print("Average Change in Profit: $", str(round_profit_changes))

    profit_increase = (max(profit_loss_list))
    print("Greatest Increase in Profit: ", key_max, "$", str(profit_increase))
    ##print("Greatest Decrease in Profit: ", key_min, str(profit_decrease))


    profit_decrease = (min(profit_loss_list))
    print("Greatest Decrease in Profit: ", key_min, "$", str(profit_decrease))
    #print("Greatest Decrease in Profit: ", key_min, str(profit_decrease))

    #output to csv
    bank_csv = zip(round_profit_changes, profit_increase, profit_decrease)
    
    output_file = os.path.join("analysis", "bank_data.csv")

    with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Average Profit Change", "Greatest Profit Increase", "Greatest Profit Decrease"])

        writer.writerows(bank_csv)




