# loading the needed modules
import os
import csv

# Setting file path for the CSV file

election_csv = os.path.join("PyPoll", "Resources","election_data.csv")

# Creating the lists/variables to store data. 
candidate_percentage=[]
candidates= []
candidate_numbers=[]
count=0
# Opening the csv using the path

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 # skipping the header   
    csv_header = next(csvreader)

 # Reading through each row
    for row in csvreader:

      # Counting the number of rows   
      count = count + 1     
   
      # Creating a list with cantidates by appending each value in the candidate column as a string
      candidates.append(row[2])

# Creatig a list with candidate unique names
unique_candidates=list(set(candidates))

# Adding number of votes and '%'s to the two lists initialized in the beginning using the unique candidates names
for x in unique_candidates:

      candidate_numbers.append(candidates.count(x))
      candidate_percentage.append(candidates.count(x)/count*100)

# Creating numbers and percentages dictionaries with the candidates as keys
candidates_numbers_dict=dict(zip(unique_candidates,candidate_numbers))
candidates_percentage_dict=dict(zip(unique_candidates,candidate_percentage))

# Create a dictionary that has key-value pairs arranged by candidates numbers
sorted_candidates_numbers_dict=(dict(sorted(candidates_numbers_dict.items(), key=lambda x:x[1], reverse=True)))

# Extract an ordered unique candidate list from the preceeding dictionary
ordered_unique_candidates=list(sorted_candidates_numbers_dict.keys())


# Mapping using candidates numbers dictionary to print the Key paring the value with the highest number of observations
winners_name=max(candidates_numbers_dict, key=lambda x: candidates_numbers_dict[x])

# Printing results for all candidates in the ordered unique candidates list/Making it a dynamic print
print('''Election Results
--------------------------
Total Votes: %d
--------------------------'''%(count))

for x in ordered_unique_candidates:
   print('%s: %.3f%% (%d)'%(x,candidates_percentage_dict[x],candidates_numbers_dict[x]) )  

print('''---------------------------
Winner: %s
---------------------------
''' %(winners_name))

# Creating a text file for the results
with open('PyPoll/pypoll.txt', 'w') as text:
    text.write('''Election Results
--------------------------
Total Votes: %d
--------------------------\n'''%(count))

# Appending the candidates results to the text file
for x in ordered_unique_candidates:
   with open('PyPoll/pypoll.txt', 'a') as text:
    text.write('%s: %.3f%% (%d)\n'%(x,candidates_percentage_dict[x],candidates_numbers_dict[x]) )  

# Appending the winner results to the text file
with open('PyPoll/pypoll.txt', 'a') as text:
   text.write('''---------------------------
Winner: %s
---------------------------
''' %(winners_name))
