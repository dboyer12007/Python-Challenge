import os
import csv

  # Create a path
budget_data = os.path.join('Resources', 'budget_data.csv')

  # Open and read

with open(budget_data) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    # Read Header
    csv_header = next(csv_reader)
    print(f'Header:{csv_header}')
    
    # Intitialize lists 
    dates = []
    profits = []

    #Extract Data
    for row in csv_reader:
        print(row)
        dates.append(row['Date'])
        profits.append(int(row['Profit/Losses']))

    # print number of months
    months_count = len(dates)
    print(f'Months: {len(dates)}')

    #print the sum of the Profits
    total_profit = sum(profits)   
    print(f'Total:${total_profit:,.2f}')
    

    #print the greatest increase in profits
    max_profit = max(profits)
    print(f'Greatest Profit: ${max_profit:,.2f}')

     #print the greatest loss in profits
    min_profit = min(profits)
    print(f'Greatest Loss: ${min_profit:,.2f}')

     
     # Find monthly changes 
    monthly_changes = []
    for i in range (1, len(profits)):
        monthly_change = profits[i] - profits[i-1]
        monthly_changes.append(monthly_change)
     
    
    # Find and print average change
    average_change = sum(monthly_changes) / len(monthly_changes)
    print(f'Average Change: ${average_change:,.2f}')
    
        
        # Print the greatest increase
    max_increase = max(monthly_changes)
    print (f'Greatest Increase in Profits: (${max_increase:,.2f})')
  
    # Print the greatest decrese
    max_decrease = min(monthly_changes)
    print (f'Greatest Decrease in Profits: (${max_decrease:,.2f})')


    # Create a path to save in Analysis 

analysis_file_path = os.path.join('Analysis', 'Analysis.txt')

    # Save as a text file

with open(analysis_file_path, 'w') as text_file:
    text_file.write('Analysis\n')
    text_file.write('----------------------------\n')
    text_file.write(f'Total Months: {months_count}\n')
    text_file.write(f'Total: ${total_profit:,.2f}\n')
    text_file.write(f'Average Change: ${average_change:,.2f}\n')
    text_file.write(f'Greatest Increase in Profits: ${max_increase:,.2f}\n')
    text_file.write(f'Greatest Decrease in Profits: ${max_decrease:,.2f}\n')

