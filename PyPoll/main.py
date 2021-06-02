#open and read csv file
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
# with open("Resources/Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv", 'r') as pypoll_file:
with open(csvpath) as pypoll_file:
    csvreader = csv.reader(pypoll_file, delimiter = ",")

    # identify and skip header
    print ("Election Results")
    print ("-------------------------")
    csv_header = next(csvreader)

    #storing the data as a list
    election_data = list(csvreader)
    total_voted = len(election_data)
    print("Total Votes: "+str(total_voted))
    print ("-------------------------")
    
    # Counting the votes for each candidate
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    for row in election_data:
        if row[2] == "Khan":
            khan_votes = khan_votes +1 
        elif row[2] == "Correy":
            correy_votes= correy_votes +1
        elif row[2] == "Li":
            li_votes= li_votes +1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes +1
    #calculating the percentages of the votes for each candidate
    khan_perc = 100* khan_votes/total_voted
    correy_perc = 100* correy_votes/total_voted
    li_perc = 100* li_votes/total_voted
    otooley_perc = 100* otooley_votes/total_voted
    
    khan_round = round(khan_perc,3)
    correy_round = round(correy_perc,3)
    li_round = round(li_perc,3)
    otooley_round = round(otooley_perc,3)
    
    print(f"Khan: {str(khan_round)}% ({str(khan_votes)})")
    print(f"Correy: {str(correy_round)}% ({str(correy_votes)})")
    print(f"Li: {str(li_round)}% ({str(li_votes)})")
    print(f"O'Tooley: {str(otooley_round)}% ({str(otooley_votes)})")
    print ("-------------------------")
    
    #Finding the total for the winner
    winner_total = max(khan_votes,correy_votes,li_votes,otooley_votes)
    #Creating a list of the final talley of the Votes for each candidate
    final_vote_count = []
    final_vote_count.append(khan_votes)
    final_vote_count.append(correy_votes)
    final_vote_count.append(li_votes)
    final_vote_count.append(otooley_votes)
    #determining the winner
    for row in final_vote_count:
        if winner_total == khan_votes:
                winner = "Khan"
        elif winner_total == correy_votes:
                winner = "Correy"
        elif winner_total == li_votes:
                winner = "Li"
        elif winner_total == otooley_votes:
                winner = "O'Tooley"
    print(f"Winner: {winner}")

            
        
print ("-------------------------")


#output txt file of the printed strings
import sys   
original_stdout = sys.stdout

with open('analysis/FinalElection.txt', 'w') as f:
    sys.stdout = f 
    print ("Election Results")
    print ("-------------------------")
    print("Total Votes: "+str(total_voted))
    print ("-------------------------")
    print(f"Khan: {str(khan_round)}% ({str(khan_votes)})")
    print(f"Correy: {str(correy_round)}% ({str(correy_votes)})")
    print(f"Li: {str(li_round)}% ({str(li_votes)})")
    print(f"O'Tooley: {str(otooley_round)}% ({str(otooley_votes)})")
    print ("-------------------------")
    print(f"Winner: {winner}")
    print ("-------------------------")
    sys.stdout = original_stdout