#loading the needed modules
import os
import csv

#Setting file path for the CSV file

bank_csv = os.path.join("PyBank", "Resources","budget_data.csv")

# Creating the lists/variables to store data. 

pl_monthly = []
date_monthly = []
count=0
# Opening the csv using the path

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvreader)
   
    # reading through each row
    for row in csvreader:

      #counting the number of rows without the header  
      count = count + 1     
   
      # Creating a list with dates by appending each value in the date column as a string
      date_monthly.append(row[0])

      # Creating a list with profits/losses by appending each value in the P/L column as a string
      pl_monthly.append(int(row[1]))

#calculating the number of distinct/unique dates      
unique_months=len(set(date_monthly))

#Calculating the net amount of profits and losses for the entire period
net_pl=sum(pl_monthly)

#Setting two lists, one with the initial month and the  next with the subsequent month
initial_plmonthly=pl_monthly[0::1]
next_plmonthly=pl_monthly[1::1]

#Calculating the differences between months
monthly_difference=[x1 - x2 for (x1, x2) in zip(next_plmonthly, initial_plmonthly)]

#Average for the 85 data points
average_change=sum(monthly_difference)/((count)-1)

#greatest increase/decrease in profits 
greatest_profits = max(monthly_difference)
greatest_losses = min(monthly_difference)

#To take into account the number of months, the month removed in the above calculation should be added back
increase_date = date_monthly[monthly_difference.index(greatest_profits)+1]
decrease_date = date_monthly[monthly_difference.index(greatest_losses)+1]

#number formats can be used as a place holder in concatenating variables and statements 
print('''Financial Analysis
-----------------------------
Total Months: %d
Total: $%d
Average Change: $%.2f
Greatest Increase in Profits: %s ($%d)
Greatest Decrease in Profits: %s ($%d)
''' %(count,net_pl,average_change,increase_date,greatest_profits,decrease_date,greatest_losses))

#path should be in the same folder as the main file
with open('PyBank/pybank.txt', 'w') as text:
    text.write('''Financial Analysis
------------------------------
Total Months: %d
Total: $%d
Average Change: $%.2f
Greatest Increase in Profits: %s ($%d)
Greatest Decrease in Profits: %s ($%d)
''' %(count,net_pl,average_change,increase_date,greatest_profits,decrease_date,greatest_losses))
