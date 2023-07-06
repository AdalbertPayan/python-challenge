import os
import csv

pypoll_csv = os.path.join('Resources', 'election_data.csv')

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called election_data.csv. 
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#set variable and dictionary values
    total_votes = 0
    candidates = {}
    most_votes = 0
    winner = ""

#loop through the data
    for row in csv_reader:
        total_votes += 1
#assign candidate column to a variable
        candidate = row[2]
#total number of votes cast
        if candidate in candidates:
            candidates[candidate] += 1
        else: 
            candidates[candidate] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#A complete list of candidates who received votes, and the percentage of votes each candidate won
for candidate, votes in candidates.items():
    print(f"{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})")
#most votes per candidate and winner of the election based on popular vote
    if votes > most_votes:
        most_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export a text file with the results
output_path = os.path.join("Analysis", "election_results.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Total Votes: {total_votes}\n")
    analysis.write("-------------------------\n")
    for candidate, votes in candidates.items():
        analysis.write(f"{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Winner: {winner}\n")
    analysis.write("-------------------------\n")