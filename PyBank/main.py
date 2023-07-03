""" PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results. """


### From Day 2, Activity 8

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Counters
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
    # This is the main loop!

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_profit_losses = net_profit_losses + profit_loss

        if total_months > 1:
            change = profit_loss - last_profit_losses

            sum_profit_losses = sum_profit_losses + change
            

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        last_profit_losses = int(row[1])
        
    ave_change = sum_profit_losses / (total_months - 1)
    
    print(f"Total Months: {total_months}")
    print(f'Total: ${net_profit_losses}')
    print(f"Average Change: ${round(ave_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    

