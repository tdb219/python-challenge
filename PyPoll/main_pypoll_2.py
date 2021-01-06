#open and read csv file
with open(pypoll_csv, 'r') as pypoll_file:
    csvreader = csv.reader(pypoll_file, delimiter = ",")
#identify and skip header
    csv_header = next(csvreader)
    next(csvreader, None)
    total_votes = len(list(csvreader))
    #print voting data
    votes=[]
    khan_votes = []
    correy_votes = []
    li_votes = []
    otooley_votes = []
    for row in csvreader:
        votes_cast=str(row[0])
        votes.append(votes_cast)
        khan = "Khan"
        correy = "Correy"
        li = "Li"
        otooley = "O'Tooley"
        candidates = row[2]
        if candidates == khan:
            khan_votes.append(candidates)
        if candidates == correy:
            correy_votes.append(candidates)
        if candidates == li:
            li_votes.append(candidates)
        if candidates == otooley:
            otooley_votes.append(candidates)
    khan_total = len(khan_votes)
    khan_percent = str(khan_total/total_votes*100)
    khan_float = float(khan_percent)
    khan_round = round(khan_float, 3)
    print("Khan: ", str(khan_round), "% ", "(" + str(khan_total), ")")
    
    correy_total = len(correy_votes)
    correy_percent = str(correy_total/total_votes*100)
    correy_float = float(correy_percent)
    correy_round = round(correy_float, 3)
    print("Correy: " + str(correy_round) + "% " + "(" + str(correy_total) + ")")


    li_total=len(li_votes)
    li_percent=str(li_total/total_votes*100)
    li_float = float(li_percent)
    li_round = round(li_float, 3)
    print("Li: " + str(li_round) + "% " + "(" + str(li_total) + ")")


    otooley_total = len(otooley_votes)
    otooley_percent = (otooley_total/total_votes*100)
    otooley_float = float(otooley_percent)
    otooley_round = round(otooley_float, 3)
    print("O'Tooley: " + str(otooley_round) + "% " + "(" + str(otooley_total) + ")")


    #output to csv
    polls_csv = zip(votes, khan_total, khan_percent, khan_float, khan_round, 
        correy_total, correy_percent, correy_float, correy_round,
        li_total, li_percent, li_float, li_round,
        otooley_total, otooley_percent, otooley_float, otooley_round,)
    
    output_file = os.path.join("poll_data.csv")

    with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Total Votes", "Candidate", "Number of Votes", "Percent of Votes", 
                         "Percent of Votes (float)", "Percent of Votes (round)"])

        writer.writerows(polls_csv)