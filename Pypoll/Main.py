import os
import csv

    # Create a path to the CSV file
election_data = os.path.join('Resources', 'election_data.csv')


    # Open and read the CSV file
with open(election_data) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
   
    # Initialize variables
    total_ballots = 0
    candidate_votes = {}

    # Loop through each row in the file
    for row in csv_reader:
        total_ballots += 1  # This will start at 0 and count 1 for each row of Candidate
        candidate = row['Candidate']
        
        # Add the vote to the candidate's total, the if the candidate is already in the dict, it will add a vote to the existing total, else it will add candiate to dict with 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

        # Print out the results
print(f'Total Ballots: {total_ballots}')
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_ballots) * 100
    print(f'{candidate}: {percentage:.2f}% ({votes})')

        # Find and print the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f'Winner: {winner}')

    # Create a path to save in Analysis 
analysis_file_path = os.path.join('analysis', 'Pypoll_analysis.txt')

        #Save print out as a text file
with open(analysis_file_path, 'w') as text_file:
    text_file.write('Pypoll_Analysis\n')
    text_file.write('----------------------------\n')
    text_file.write(f'Total Ballots: {total_ballots}\n')
    
     #Loop print for each candidate
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_ballots) * 100
        text_file.write(f'{candidate}: {percentage:.2f}% ({votes})\n')
   
    text_file.write(f'Winner: {winner}')
