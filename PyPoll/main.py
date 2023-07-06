import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = {}
most_votes = 0
most_votes_candidate = ''

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    ### This is the main loop! ###

    for row in csvreader:

        total_votes += 1

        # If the candidate in the row matches any candidate from candidates list currently,
        # Increment a vote for the candidate within the dictionary, else add a new key value pair to the dictionary for the new candidate.
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # Compare the new vote total against current highest total, if new total is higher, store candidate and new total.
        if candidates[row[2]] > most_votes:
            most_votes = candidates[row[2]]
            most_votes_candidate = row[2]

# Print results to screen
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate, votes in candidates.items():
    print(f'{candidate}: {round(votes/total_votes*100,3)}% ({votes})')  
print('-------------------------')
print(f'Winner: {most_votes_candidate}')
print('-------------------------')

    # Specify the file to write to
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as f:
    f.write('Election Results\n')
    f.write('-------------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('-------------------------\n')
    for candidate, votes in candidates.items():
        f.write(f'{candidate}: {round(votes/total_votes*100,3)}% ({votes})\n')   
    f.write('-------------------------\n')
    f.write(f'Winner: {most_votes_candidate}\n')
    f.write('-------------------------')