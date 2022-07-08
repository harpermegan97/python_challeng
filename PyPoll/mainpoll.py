import csv
import os

print("Election Results")
print("--------------------------------------")

election_data0 = os.path.join("Resources", "election_data.csv")
with open(election_data0,'r+') as csvfile0: 
    csvreader0 = csv.reader(csvfile0, delimiter=",")
    next(csvreader0, None)
    numitems = len(list(csvreader0))



election_data1 = os.path.join("Resources", "election_data.csv")
with open(election_data1,'r+') as csvfile:  
     

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    print("Total Votes: ", len(list(csvreader)))
    

print("--------------------------------------")








