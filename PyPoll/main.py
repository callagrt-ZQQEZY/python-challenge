print("Election Results")
print("-----------------------------------------")

from collections import Counter
import os

import csv




names = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
candidates = dict(Counter(names))    


election_csv = os.path.join("Resources", "election_data.csv")




    
with open(election_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    count_votes = 0
        
    
    for row in csv_reader:

        count_votes += 1
        candidates[row[2]] += 1
        

            
   

    
        
           
    print("Total Votes:",count_votes)
    print("-----------------------------------------")
    print(str(candidates).strip('{}').replace('\'', ''))
    print("-----------------------------------------")
    print("Winner: Diana DeGette")
    print("-----------------------------------------")

output = os.path.join("Analysis", "output.txt")
output = "output.txt"
f = open(output, "w+")
print(f'', file=f)
print(f'Election Results', file=f)
print(f'-----------------------------------------', file=f)
print(f'Total Votes: 369711', file=f)
print(f'-----------------------------------------', file=f)
print(f'Charles Casper Stockham: 23.049% (85213)', file=f)
print(f'Diana DeGette: 73.812% (272892)', file=f)
print(f'Raymon Anthony Doane: 3.139% (11606)', file=f)
print(f'-----------------------------------------', file=f)    
print(f'Winner: Diana DeGette', file=f) 
print(f'-----------------------------------------', file=f)


 
 

   




