# Add our dependencies
import csv
import os
# Assign a variable for the file to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total voter counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Challenge- Counties that voted
counties = []
# Declare empty dictionary
county_votes = {}

# Determine the winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Empty string for county name with largest voter turnout
largest_county_turnout = ""
largest_county_votes = 0

# Open the election results
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read header row
    header = next(reader)
    # Print each row in csv file
    for row in reader:
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
        
        # Get county name from each row
        county_name = row[1] 

        if county_name not in counties:
            # Add it to list of counties
            counties.append(county_name)
            # Track each county's votes
            county_votes[county_name] = 0

        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to terminal
    election_results = (
        f'\nElection Results\n'
        f'----------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'----------------------\n'
        f'\nCounty Votes:\n')
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)

    # Challenge- save final county vote count to text file
    for county in county_votes:
        # Retrieve vote count and percentages
        county_vote = county_votes[county]
        county_percent = int(county_vote)/int(total_votes)*100
        
        county_results = (
        f'{county}:{county_percent:.1f}%({county_vote:,})\n')
        print(county_results, end="")
        txt_file.write(county_results)

        # Challenge- Determine winning vote count of county
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county

        # Print county of largest voter turnout
    largest_county_turnout = (f'\n----------------------\n'
        f"Largest County Turnout:{largest_county_turnout}\n----------------------\n")
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage in terminal
        print(candidate_results)
        # Save candidate results to our text file
        txt_file.write(candidate_results)
            # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_candidate = candidate
            winning_percentage = vote_percentage 

    # Print winning candidate's results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate's results to text file.
    txt_file.write(winning_candidate_summary)