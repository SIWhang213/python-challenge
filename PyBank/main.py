import os
import csv

# Set path for 'budget_data.csv' file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# the total number of months included in the dataset
total_num_months = 0

# the net total amount of Profit/Losses over the entire period
total_amount_PL = 0

# lists and variable for the changes in Profit/Losses over the entire period
profits = []
profit_changes = []
total_profit_change = 0

# the greatest increase in profits (date and amount) over the entire period
max_profit = 0

# the greatest decrease in profits (date and amount) over the entire period
min_profit = 0

with open(csvpath) as csvfile :
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    cvs_hearder = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_num_months += 1
        total_amount_PL += int(row[1])
        profits.append(row[1])
        if len(profits)>1:
            change = int(profits[len(profits)-1]) - int(profits[len(profits)-2] )  
            profit_changes.append(change)
            if change > max_profit:
                max_profit = change
                max_profit_month = row[0]
            if change < min_profit:
                min_profit = change
                min_profit_month = row[0]    

    for change in profit_changes:
        total_profit_change += change
    
    # the average of the changes in Profit/Losses over the entire period to 2 decimal places
    profit_average =  round(total_profit_change/len(profit_changes),2)    

# Set variable for output file
output_file = os.path.join('.','analysis','analysis_budget_data.csv')

#Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------------"])
    writer.writerow(["Total Months: " + str(total_num_months)])
    writer.writerow(["Total: " + "$"+ str(total_amount_PL)])
    writer.writerow(["Average Change: " + "$"+ str(profit_average)])
    writer.writerow(["Greatest Increase in Profit: " + max_profit_month + "  ($" + str(max_profit) +")"])
    writer.writerow(["Greatest Decrease in Profit: " + min_profit_month + "  ($" + str(min_profit) +")"])

# print output to the terminal
print("Financial Analysis")    
print("-----------------------------------")
print(f"Total Months: {str(total_num_months)}")
print(f"Total: ${str(total_amount_PL)}")
print(f"Average Change: ${str(profit_average)}")
print(f"Greatest Increase in Profit: {max_profit_month}  (${str(max_profit)})")
print(f"Greatest Decrease in Profit: {min_profit_month}  (${str(min_profit)})")