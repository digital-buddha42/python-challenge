import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
total_charles = 0
total_diana = 0
total_raymon = 0
winner = ''

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

        if row[2] == 'Charles Casper Stockham':
            total_charles += 1
        elif row[2] == 'Diana DeGette':
            total_diana += 1
        elif row[2] == 'Raymon Anthony Doane':
            total_raymon += 1

    total_charles_percent = total_charles/total_votes
    formatted_percentage_charles = f"{total_charles_percent:.3%}"

    total_diana_percent = total_diana/total_votes
    formatted_percentage_diana = f"{total_diana_percent:.3%}"

    total_raymon_percent = total_raymon/total_votes
    formatted_percentage_raymon = f"{total_raymon_percent:.3%}"

    if total_charles > total_diana:
        winner = candidates[0]
        winner_total = total_charles
    else:
        winner = candidates[1]
        winner_total = total_diana
    if total_raymon > winner_total:
        winner = candidates[2]
        winner_total = total_raymon

    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    print(f'{candidates[0]}: {formatted_percentage_charles} ({total_charles})')
    print(f'{candidates[1]}: {formatted_percentage_diana} ({total_diana})')
    print(f'{candidates[2]}: {formatted_percentage_raymon} ({total_raymon})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

    # Specify the file to write to
    output_path = os.path.join("analysis", "analysis.txt")

    with open(output_path, 'w') as f:
        f.write('Election Results\n')
        f.write('-------------------------\n')
        f.write(f'Total Votes: {total_votes}\n')
        f.write('-------------------------\n')
        f.write(f'{candidates[0]}: {formatted_percentage_charles} ({total_charles})\n')
        f.write(f'{candidates[1]}: {formatted_percentage_diana} ({total_diana})\n')
        f.write(f'{candidates[2]}: {formatted_percentage_raymon} ({total_raymon})\n')
        f.write('-------------------------\n')
        f.write(f'Winner: {winner}\n')
        f.write('-------------------------')