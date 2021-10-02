# Retrieve the Data
# 1. The total number of votes cast.
# 2. A complete list of the candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. the total number of votes each candidate won. 
# 5. The winner of the election based on popular vote.  

#Add our dependencies.
import csv
import os 
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter 
total_votes = 0

#Initialize cadidate options list 
candidate_options = []
#Create empty dictionay for candidates and their vote counts
candidate_votes = {}

#Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row. 
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total votes count. 
        total_votes += 1

        #Print Candidate name from each row
        candidate_name = row[2]

        # if name does not match any existing candidate in list 
        if candidate_name not in (candidate_options):

            #add the candidate name to the candidate list 
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add count to candidate's votes 
        candidate_votes[candidate_name] +=1

    #save the results to text file 
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"--------------------------\n")

        print (election_results, end = "")
        #Save the final vote count to the text file. 
        txt_file.write(election_results)
    

        #determine the percentage of votes for each candidate by looping through the counts 
        for candidate_name in candidate_votes:
            #retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            #calculate the percentage of votes for candidate 
            vote_percentage = (float(votes) / float(total_votes))*100
        
            # #print each candidate, their vote count, and percentag to the terminal

            candidate_results = (f"{candidate_name}]: received {vote_percentage: .1f} % ({votes:,})\n")

            print(candidate_results)
            #save candidate results to our text file 
            txt_file.write(candidate_results)

            #determine winning vote count and candidate 
            if (votes > winning_count) and (vote_percentage>winning_percentage): 
                #If true then set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage

                #Set winning candidate equal to the candidate's name 
                winning_candidate = candidate_name
        
        #Winning candidate Summary 
        winning_candidate_summary = (
            f"-----------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------------------\n")
        print(winning_candidate_summary)

        #save the winning candidate's name to the text file. 
        txt_file.write(winning_candidate_summary)