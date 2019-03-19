#loading the needed modules
import os
import csv

#Setting file path for the CSV file

election_csv = os.path.join("PyPoll", "Resources","election_data.csv")

# Creating the lists/variables to store data. 
candidate_percentage=[]
candidates= []
candidate_numbers=[]
count=0
# Opening the csv using the path

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
 # reading through each row
    for row in csvreader:

      #counting the number of rows without the header  
      count = count + 1     
   
      # Creating a list with dates by appending each value in the date column as a string
      candidates.append(row[2])

      # Creating a list with profits/losses by appending each value in the P/L column as a string
      #.append(int(row[1]))

unique_candidates=list(set(candidates))


for x in unique_candidates:

      candidate_numbers.append(candidates.count(x))
      candidate_percentage.append(candidates.count(x)/count*100)
print(candidate_percentage)
candidates_numbers_dict=dict(zip(unique_candidates,candidate_numbers))
candidates_percentage_dict=dict(zip(unique_candidates,candidate_percentage))
print(candidates_numbers_dict)
winners_name=max(candidates_numbers_dict, key=lambda x: candidates_numbers_dict[x])
print(winners_name)

print('''Election Results
--------------------------
Total Votes: %d
--------------------------
Khan: %.3f (%d) 
Correy: %.3f (%d)
Li: %.3f (%d)
O'Tooley: %.3f (%d)
---------------------------
Winner: %s
---------------------------
''' %(count,candidates_percentage_dict['Khan'],candidates_numbers_dict['Khan']
    ,candidates_percentage_dict['Correy'],candidates_numbers_dict['Correy']
    ,candidates_percentage_dict['Li'],candidates_numbers_dict['Li']
    ,candidates_percentage_dict["O'Tooley"],candidates_numbers_dict["O'Tooley"],winners_name))

with open('PyPoll/pypoll.txt', 'w') as text:
    text.write('''Election Results
--------------------------
Total Votes: %d
--------------------------
Khan: %.3f (%d) 
Correy: %.3f (%d)
Li: %.3f (%d)
O'Tooley: %.3f (%d)
---------------------------
Winner: %s
---------------------------
''' %(count,candidates_percentage_dict['Khan'],candidates_numbers_dict['Khan']
    ,candidates_percentage_dict['Correy'],candidates_numbers_dict['Correy']
    ,candidates_percentage_dict['Li'],candidates_numbers_dict['Li']
    ,candidates_percentage_dict["O'Tooley"],candidates_numbers_dict["O'Tooley"],winners_name))
