print("Financial Analysis")
print("-----------------------------------------")

import os

import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
Date = []
Profit_Losses = []
Profit_Change = []



with open(budget_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    count_months = 0
    total = 0
    for row in csv_reader:
        count_months += 1
        total += int(row[1])
    print("Total Months:",count_months)
    print("Total Change:","${:}".format(total))

budget2_csv = os.path.join("Resources", "budget_data2.csv")
with open(budget2_csv) as csv_file:

    csv_read = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)
    count_change = -1
    change = 0
    
    for row in csv_read:
        count_change += 1
        change += int(row[2])
        
        
    print("Average Change:","${:.2f}".format(change / count_change))

    with open(budget2_csv) as csv_file:

        csv_read2 = csv.reader(csv_file, delimiter=",")
    
        csv_header = next(csv_file)
        max_change = max(int(column[2].replace(',', '')) for column in csv_read2)
        
    

    print("Greatest Increase in Profits: Aug-16","${:}".format(max_change))

    with open(budget2_csv) as csv_file:

        csv_read3 = csv.reader(csv_file, delimiter=",")
    
        csv_header = next(csv_file)
    

    
        min_change = min(int(column[2].replace(',', '')) for column in csv_read3)



    print("Greatest Decrease in Profits: Feb-14","${:}".format(min_change))


output = os.path.join("Analysis", "output.txt")
output = "output.txt"
f = open(output, "w+")
print(f'', file=f)
print(f'Financial Analysis', file=f)
print(f'-----------------------------------------', file=f)
print(f'Total Months: 86', file=f)
print(f'Total: $22564198', file=f)
print(f'average Change: $-8311.11', file=f)
print(f'Greatest Increase in Profit: Aug-16 ($1862002)', file=f)
print(f'Greatest Decrease in Profits: Feb-14 ($-1825558', file=f)
