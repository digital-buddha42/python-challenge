### From Day 2, Activity 8

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Counters at extremes
total_months = 0
net_profit_losses = 0

sum_profit_losses = 0

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 999999999999
greatest_decrease_month = ""

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header

    ### This is the main loop! ###

    for row in csvreader:

        # Define variables by column. 
        date = row[0]

        # Convert profit_loss to integer!
        profit_loss = int(row[1])

        # Add 1 to total months counter. 
        total_months += 1

        # Add current row profit_loss to net_profit_loss.
        net_profit_losses = net_profit_losses + profit_loss

        # Check to see if a change occurred. (all but first row of table)
        if total_months > 1:

            # Caculate change using previous row value compared to current row.
            change = profit_loss - last_profit_losses

            # Add change to profit_loss sum.
            sum_profit_losses = sum_profit_losses + change
            
            # Check if the last change is greater than the most recent greatest stored increase.
            if change > greatest_increase:

                # Reset the greatest stored increase to the new greatest value. Store the month.
                greatest_increase = change
                greatest_increase_month = row[0]

            # Check if the last change is less than the most recent greatest stored decrease.
            if change < greatest_decrease:

                # Reset the greatest stored decrease to the new greatest value. Store the month.
                greatest_decrease = change
                greatest_decrease_month = row[0]

        # Store the profit loss in another variable. 
        # The next time through the loop, the previous value (now stored) can be used as comparison to calculate change.
        last_profit_losses = int(row[1])

    # Finally, outside the main loop, calculate ave_change.
    # since you have no change for the first row, subtract 1 from total months.    
    ave_change = sum_profit_losses / (total_months - 1)
    
    # Print summary info to screen
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f'Total: ${net_profit_losses}')
    print(f"Average Change: ${round(ave_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    

