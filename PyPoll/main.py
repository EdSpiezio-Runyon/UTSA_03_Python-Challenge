# OPEN CSV FOR READING
# # Import the OS module
import os

# Import module for reading CSV file
import csv

# Connect input path to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Create output path and filename for saved analysis text file
save = os.path.join('Analysis', 'analysis.txt')

# Establish initial variables
candidates = []
candidate_votes = {}
win_candidate = ""
win_count = 0
win_percent = 0

# Open the election results and read the file
with open(csvpath) as csvfile:

    # Read the file object with the reader function.
    csvreader = csv.reader(csvfile)

    # Read the headers row.
    csv_header = next(csvreader)

    # Read each row of data after the header to calculate the data
    total_votes = 0

    # Print each row in the CSV file
    for row in csvreader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate names (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
        if candidate_name not in candidates:

            # Add it to the list of candidates
            candidates.append(candidate_name)

            # Then track that candidate's vote count as the program progresses row by row
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates's count (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
        candidate_votes[candidate_name] += 1

# Display the results on screen and save to the analysis text file
with open(save, "w") as txt_file:

    # Diplay the results on screen (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
    election_results = (
        f"\nElection Results\n"
        f"------------------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file (source: (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
    txt_file.write(election_results)
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage (source: https://github.com/JovaniPink/election-analysis/blob/master/PyPoll.py)
        votes = candidate_votes[candidate_name]
        vote_percent = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percent:.3f}% ({votes:,})\n"

        # Display each candidate's voter count and percentage on screen
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate
        if (votes > win_count) and (vote_percent > win_percent):
            win_count = votes
            win_candidate = candidate_name

    # Display the  winning candidate's results on screen
    win_candidate_summary = (
        f"------------------------------------------------------\n"
        f"Winner: {win_candidate}\n"
        f"------------------------------------------------------\n")
    print(win_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(win_candidate_summary)