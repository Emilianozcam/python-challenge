# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
profit_loss = 0 #To store the total profit/loss over the entire period
net_changes = {} #Dictionary to track changes in profit/loss by month
# Open and read the csv
with open(file_to_load, encoding= "UTF-8") as financial_data:
    reader = csv.reader(financial_data, delimiter=",") #Read the csv data using coma as delimeter

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1 #Increment the month count
    total_net += int(first_row[1]) #Add the profit/loss from the first row to the total
    profit_loss = int(first_row[1]) #Initializae profit_loss with the first row's value


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1 #Increment month count for each row processed
        total_net += int(row[1]) #Add current month's profit/loss to the total


        # Track the net change
        current_pl = int(row[1]) #Convert the current month's profit/loss to an integer
        net_change = current_pl - profit_loss #Calculate the change from the previous month
        net_changes[row[0]] = net_change #Store the net change with the month as the key

        profit_loss = current_pl #Update profit_loss for the next iteration

        # Calculate the greatest increase in profits (month and amount)
        great_increase_month = max(net_changes, key=net_changes.get) #Find the month with the highest increase
        great_increase = net_changes[great_increase_month] #Get the value of the greatest increase

        # Calculate the greatest decrease in losses (month and amount)
        great_decrease_month = min(net_changes,key=net_changes.get) #Find the month with the lowest increase
        great_decrease = net_changes[great_decrease_month] #Get the value of the greatest decrease

# Calculate the average net change across the months
average_change = sum(net_changes.values()) / len(net_changes) #Calculate the average change
average_change_round = round(average_change, 2) #Round the average change to two decimal places
# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change_round}\n"
    f"Greatest Increase in Profits: {great_increase_month} (${great_increase})\n"
    f"Greates Decrease in Profits: {great_decrease_month} (${great_decrease})\n"
)
# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

