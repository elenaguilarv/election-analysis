# The data we need to retrieve.
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total voter counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Determine the winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in csv file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add name to list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

# To do: print out each candidate's name, vote count and percentage of
# votes to the terminal
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = 
        # vote_percentage
        winning_count = votes 
        winning_percentage = vote_percentage
        # Set winning_candidate equal to the candidate's name
        winning_candidate = candidate

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)