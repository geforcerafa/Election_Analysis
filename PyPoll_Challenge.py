#Add our dependencies
#from functools import total_ordering
import os
import csv

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
county_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}
county_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    # for row in file_reader:
    #   print(row)

    #Read and print the header row.
    headers = next(file_reader)
 #   print(headers)

    #print each row in the CSV file.
    for row in file_reader:
  #      print(row)
        # Add the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        county_name = row[1]

        #If the candidate does not match any existing candidate...
        if county_name not in county_options:
            #Add the candidate name to the candidate list.
            county_options.append(county_name)

            # 2.  Begin tracking that candidate's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count.
        county_votes[county_name] += 1

        # Save the results to our text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count into the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping throuth the counts
            # 1. Iterate through the candidate list.
    for county_name in county_votes: 
                # 2 Retrieve vote count of a candidate.
        votes = county_votes[county_name]
                # 3 Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
                # 4 Print the candidate name and percentage of votes and total votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal-
        print(county_results)
        #Save the candidate results to our text file.
        txt_file.write(county_results)

    # Determine winning vote count, winning percentage and cadidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_county_summary = (
        f"-------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
    #    f"Winning Vote Count: {winning_count:,}\n"
     #   f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n")

    # Print total votes.
    # print(total_votes)
    # Print the candidate list.
    # print(candidate_options)
    #print(candidate_votes)
    # print(winning_candidate_summary)
    print(winning_county_summary) 
    txt_file.write(winning_county_summary)

#Add our dependencies
#from functools import total_ordering
import os
import csv

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    # for row in file_reader:
    #   print(row)

    #Read and print the header row.
    headers = next(file_reader)
 #   print(headers)

    #print each row in the CSV file.
    for row in file_reader:
  #      print(row)
        # Add the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2.  Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Save the results to our text file
with open(file_to_save, "a") as txt_file:

# Print the final vote count into the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
   # print(election_results, end="")
    # Save the final vote count to the text file.
   # txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping throuth the counts
            # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes: 
                # 2 Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
                # 3 Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
                # 4 Print the candidate name and percentage of votes and total votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal-
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count, winning percentage and cadidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n")

    # Print total votes.
    # print(total_votes)
    # Print the candidate list.
    # print(candidate_options)
    #print(candidate_votes)
    # print(winning_candidate_summary)
    print(winning_candidate_summary) 
    txt_file.write(winning_candidate_summary)