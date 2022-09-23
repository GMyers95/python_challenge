import os
import csv
csvpath = os.path.join("Resources","election_data.csv")
total_votes = 0
candidates = []
unique_cands = {}
most_votes = 0
winner = ""
x = unique_cands.keys()
with open(csvpath, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    row = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidates.append(row[2])
    print(f"There are {total_votes} total votes in this dataset.")
    for candidate in candidates: 
        if not candidate in unique_cands.keys():
            unique_cands[candidate] = 1
        else:
            unique_cands[candidate] += 1
    for k,v in unique_cands.items():
        print(f"{k} received {round(((v)/total_votes)*100,3)}% ({v}) of the total votes.")
        if (v) > int(most_votes):
            most_votes = (v)
        if (v) == most_votes:
            winner = (k)
    print(f"{winner} wins this election!")
#Send script as text file
with open("PyPoll_text.txt",'w') as f:
    print(f"There are {total_votes} total votes in this dataset.", file=f)
    for k,v in unique_cands.items():
        print(f"{k} received {round(((v)/total_votes)*100,3)}% ({v}) of the total votes.", file=f)
    print(f"{winner} wins this election!", file=f)