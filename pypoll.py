# Import the needy modules 

import os 
import csv

# the file path 
file_path = os.path.join('raw_data', 'election_data_2.csv')

# empty list of candidates
candidate = []

# open the file
with open(file_path, newline='') as csv_file:

    # read the file
    csv_reader = csv.reader(csv_file, delimiter = ',')

    next(csv_reader, None)

    # loop the file 
    for row in csv_reader:
        candidate.append(row[2])
        # print(candidate)

# get the vote count and print 
vote_count = len(candidate)
print('.......................................')
print('Total Votes: ' + str(vote_count))

# list of candidates just in case 
list_candidate = set(candidate)
# print(list_candidate)

# {'Li', 'Khan', 'Correy', "O'Tooley"}



# make a dictionary of candidate and their votes
votes = {}

# get the keys and values for the dictionary by looping 
for name in candidate:
    if name in votes:
        votes[name] = votes[name] +1 
    else:
        votes[name] = 1

# print(votes)

each_votes = list(votes.values())


# find the percents of votes for each candidates 
for key, value in votes.items():
    votes[key] = round((value/vote_count)*100,0)

print('.......................................')

# find the max of the vote and sort the canditas 
for key, value in sorted(votes.items(), key = lambda pair: pair[1], reverse = True):
    print('{0}: {1}'.format(key,value))
    max_vote = max(votes, key=votes.get)

print('.......................................')
print('Winner: ' + max_vote, votes[max_vote])
print('.......................................')

