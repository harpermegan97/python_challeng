import csv
import os

print("Financial Analysis")
print("--------------------------------------")

budget_data0 = os.path.join("Resources", "budget_data.csv")
with open(budget_data0,'r+') as csvfile0: 
    csvreader0 = csv.reader(csvfile0, delimiter=",")
    next(csvreader0, None)
    numitems = len(list(csvreader0))



budget_data1 = os.path.join("Resources", "budget_data.csv")
with open(budget_data1,'r+') as csvfile:  
     

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    print("Total Months: ", len(list(csvreader)))
    

budget_data2 = os.path.join("Resources", "budget_data.csv")
with open(budget_data2,'r+') as csvfile1: 
    csvreader = csv.reader(csvfile1, delimiter=",")
    next(csvreader, None)
    total = 0
    for row in csvreader:
         total += int(row[1])
    
    print("Total :  $", total)

budget_data3 = os.path.join("Resources", "budget_data.csv")
with open(budget_data3,'r+') as csvfile2: 
    csvreader = csv.reader(csvfile2, delimiter=",")
    next(csvreader, None)
    total = 0
    for row in csvreader:
         total += int(row[1])

    print("Average Change :  $", total / numitems)




