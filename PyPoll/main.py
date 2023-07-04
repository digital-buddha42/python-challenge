import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
total_charles = 0
total_diana = 0
total_raymon = 0

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
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)

    print(f"Total Votes: {total_votes}")
    print(f"{candidates[0]}")