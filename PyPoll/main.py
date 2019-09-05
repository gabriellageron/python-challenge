#import OS module
import os
#import module for reading csv
import csv

file_num = 1

election_csv = os.path.join('Resources', 'election_data.csv')

#creates dictionary to be used for candidate name and vote count
votes = {}

#create variable total votes and sets to zero
total_votes = 0

#obtains data in file
with open(election_csv, 'r') as csvfile:
        csvread = csv.reader(csvfile)
        #skips header line
        next(csvread, None)

        #create dict from file using col 3 (candidate name) once
        #count vote as entry
        #count total vote by adding 1 for each loop

        for row in csvread:
            total_votes += 1
            if row[2] in votes.keys():
                votes[row[2]] = votes[row[2]] + 1
            else:
                votes[row[2]] = 1

#create lists  for candidates and vote counts

candidates = []
number_votes = []

#use dict key and value to put them into lists
for key, value in votes.items():
    candidates.append(key)
    number_votes.append(value)

#create vote percent list
vote_percentage = []
for n in number_votes:
    vote_percentage.append(round(n/total_votes*100,1))

#zip candiadte, number votes, vote percentage into tuple
finished_data = list(zip(candidates, number_votes, vote_percentage))

#create winner list
winner_list = []

for name in finished_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

 #make winner list a string with the first entry
winner = winner_list[0]

#output to txt file

output_file = os.path.join('Output', 'election_results_' + str(file_num) + '.txt')


with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in finished_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

    #prints output
    with open(output_file, 'r') as readfile:
        print(readfile.read())




