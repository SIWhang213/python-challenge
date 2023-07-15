import os
import csv

# Set path for 'election_data.csv' file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# the total number of votes cast
total_num_votes = 0

# A complete list of candidates who receives votes
candidates = []

# Open the file 'election_data.csv'
with open(csvpath) as csvfile :
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    cvs_hearder = next(csvreader)

    # Find first candidate
    first_line = next(csvreader)
    candidates.append(first_line[2])
    
    for row in csvreader:
        # count the total number of votes cast
        total_num_votes += 1

        # find candidate names who received votes
        candidate_temp = row[2]
        if candidate_temp != candidates[len(candidates)-1]:
            candidates.append(candidate_temp)
    
    # Subtract duplicate elements from the list named candidates
    #candidates_list = list(set(candidates))
    candidates_list = [candidate for i, candidate in enumerate(candidates) if candidate not in candidates[:i]]

# the total number of votes each candidate won
total_num_votes_each_candidate =[]

# the percentage of votes each cadidate won
percentage_votes_each_candidate = []

# Find the total number of votes each candidate won
for candidate in candidates_list:
    total_num_votes_temp = 0
    # Open the file 'election_data.csv'
    with open(csvpath) as csvfile :
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=",")
        # count the number of votes that one candidate won    
        for row in csvreader:           
            candidate_temp = row[2]    
            if candidate_temp == candidate:
                total_num_votes_temp += 1
    total_num_votes_each_candidate.append(total_num_votes_temp)    

# Find the percentage of votes each candidate won using list comprehension
percentage_votes_each_candidate = [(votes / total_num_votes) * 100 for votes in total_num_votes_each_candidate]

# Zip all three lists together into tuples
candidates_data = list(zip(candidates_list,percentage_votes_each_candidate,total_num_votes_each_candidate))

# Find the winner of the election based on popular vote
winner_index = percentage_votes_each_candidate.index(max(percentage_votes_each_candidate))
winner = candidates_list[winner_index]

# Set variable for output file
output_file = os.path.join('.','analysis','analysis_election_data.csv')

#Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------------"])
    writer.writerow(["Total Votes: " + str(total_num_votes)])
    writer.writerow(["-----------------------------------"])
    for candidate_data in candidates_data:
        writer.writerow([str(candidate_data[0]) + ": " + str(round(candidate_data[1],3)) + "% " + "(" + str(candidate_data[2]) +")"])
    
    writer.writerow(["-----------------------------------"])
    writer.writerow(["Winner:  " + winner])
    writer.writerow(["-----------------------------------"])

# print output to the terminal
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {str(total_num_votes)}")
print("-----------------------------------")
for candidate_data in candidates_data:
    print(f"{str(candidate_data[0])}: {str(round(candidate_data[1],3))}%  ({str(candidate_data[2])})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")