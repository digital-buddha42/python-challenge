import os

import csv

csvpath = os.path.join('..', 'Resources', 'zoo.csv')

# First column is the animal type and the second column is the name of the animal

# We want to count how many of each type of animal we have at the zoo. We actually don't care 
# what the names of each of the animals are, just how many of each type we have.

# Create an empty dictionary to hold the animals and their counts
animals = {}

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    total_animals = 0
    for row in csvreader:
        
        total_animals += 1
        # If the animal type is already in the dictionary, increment the count else 
        # add the animal type to the dictionary
        if row[0] in animals:
            animals[row[0]] += 1
        else:
            animals[row[0]] = 1
            
# Print the contents of the dictionary, the keys are the animals and the values are the counts
# Here's an example of how to loop through a dictionary and print out the contents   
for key, value in animals.items():
    print(f'There are {value} {key}s at the zoo.')   
    
print('\n')
    
# Or maybe we want to print out like this with the percentage of the total
print('Zoo Animals')
print('-----------')
most_animal = 0
most_animal_type = ''
for key, value in animals.items():
    print(f'{key}: {value} {round(value/total_animals*100,2)}%')   
    if value > most_animal:
        most_animal = value
        most_animal_type = key
        
print(f'\nThe most common animal is the {most_animal_type} with {most_animal}.')
