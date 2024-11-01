# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
results = {} #Dictionary to store the vote count for eachcandidate

# Winning Candidate and Winning Count Tracker

winning_candidates = [] #List to store the winning candidate
winning_count = 0 # Variable to track the highest number of votes recieved by a candidate

# Open the CSV file and process it
with open(file_to_load, encoding="UTF-8") as election_data:
    reader = csv.reader(election_data, delimiter=",") # Create a CSV reader object

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1


        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in results:
            results[candidate_name] = 0

        # Add a vote to the candidate's count
        results[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w", newline="") as txt_file:
    writer = csv.writer(txt_file) # Create a CSV writer object

    # Print the total vote count (to terminal)
    print(f"Total Votes {total_votes}")

    # Write the total vote count to the text file
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow(["Total Votes " + str(total_votes)])
    writer.writerow(["-------------------------"])


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in results.keys():

        # Get the vote count and calculate the percentage
        votes = results[candidate_name]
        vote_percentage =(votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes # Update the highest vote count
            winning_candidates = [candidate_name]
        elif votes == winning_count:
            winning_candidates.append(candidate_name) # Add to the winning candidates list if it's a tie

        # Print and save each candidate's vote count and percentage
        output = candidate_name + ": " + str(round(vote_percentage, 3)) + "% (" + str(votes) + ")"
        print(output)
        writer.writerow([output]) 

    # Generate and print the winning candidate summary
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner: " + str(winning_candidates[0])]) # Write the winner to the text file
    writer.writerow(["-------------------------"])


    # Save the winning candidate summary to the text file

