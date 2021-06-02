#import packages
import os
import csv

#open and read csv file
pybank_csv = os.path.join('Resources', 'budget_data.csv')

with open(pybank_csv, "r") as pybank_file:
    csvreader = csv.reader(pybank_file, delimiter=",")

    print ("Financial Analysis")
    print ("------------------------")
    #skip header
    next(csvreader, None)

    bank_data = list(csvreader)
    
   
    # Finding the length of the bank data
    total_months = len(bank_data)
    print(f"Total Months: {total_months}")
    
    total_profits = 0
    greatest_increase = 0
    greatest_decrease = 0
    change_data=[]
    row_num = 1
    prev_month = 0
    
    # Summing the total difference in profits
    for row in bank_data:    
        total_profits = total_profits + int(row[1])
    # Creating a list of Change Data
        if row_num > 1:
           change_data.append(int(row[1])- prev_month)
        row_num = row_num +1
        prev_month = int(row[1])
    
    
    print("Total: $"+str(total_profits))
    
    # Average profit
    sum_data= sum(change_data)
    avg_change = round(sum_data/len(change_data), 2)
    print("Average Change: $" +str(avg_change))
    
    # Creating an index for the Change Data 
    change_index = [i for i in range(1,len(bank_data))]
    

# Zipping the two lists to a tuple
bank_zip = zip(change_index, change_data)
    
 
# Finding and storing max increase and decrease
max_increase= max(change_data)
max_decrease= min(change_data)

# Finding and storing the Max increase and decrease index
for row in bank_zip:
    if row[1] == max_increase:
        max_item =row[0]
    elif row[1] ==max_decrease:
        min_item =row[0]

max_object= bank_data[max_item]
min_object= bank_data[min_item]
max_date = max_object[0]
min_date = min_object[0]

# Print results
print ("Greatest Increase in Profits: "+ max_date + " ($"+str(max_increase)+")" )
print ("Greatest Decrease in Profits: "+ min_date + " ($"+str(max_decrease)+")" )


# Output to a txt file the Printed string 
import sys   
original_stdout = sys.stdout

with open('analysis/Financial.txt', 'w') as f:
    sys.stdout = f 
    print ("Financial Analysis")
    print ("------------------------")
    print(f"Total Months: {total_months}")
    print("Total: $"+str(total_profits))
    print("Average Change: $" +str(avg_change))
    print ("Greatest Increase in Profits: "+ max_date + " ($"+str(max_increase)+")" )
    print ("Greatest Decrease in Profits: "+ min_date + " ($"+str(max_decrease)+")" )
    sys.stdout = original_stdout