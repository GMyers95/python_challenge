import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")
month_count = 0
volume = 0
best_profit = 0 
best_month = ""
worst_loss = 0
worst_month = ""
change = []
pl_change = []
with open(csvpath, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    row = next(csvreader)
    for row in csvreader:
        change.append(int(row[1]))
        month_count += 1
        volume += (int(row[1]))
        #Greg's help stopped here
    print(f"There are {month_count} months considered in this dataset.")
    print(f"The net total of Profits/Losses over the entire period is: ${volume}")

for x in range(len(change)-1):
        pl_change.append(change[x + 1] - change[x])
        best_profit = int(max(pl_change))
        worst_loss = int(min(pl_change))
        if pl_change[x] > best_profit:
            pl_change[x] = best_profit
            best_month = row[0]
        elif pl_change[x] < worst_loss:
            pl_change[x] = worst_loss
            worst_month = row[0]
average_change = (round(sum(pl_change)/(len(change)-1),2))
print(f"The average change in Profits/Losses is ${average_change}.")
print(f"The best performing month is {best_month} with ${max(pl_change)} in profit.")
print(f"The worst performing month is {worst_month} with ${min(pl_change)} in loss.")
#need to export to a text file as well
with open("PyBank_text.txt",'w') as f:
    print(f"There are {month_count} months considered in this dataset.", file=f)
    print(f"The net total of Profits/Losses over the entire period is: ${volume}", file=f)
    print(f"The average change in Profits/Losses is ${average_change}.", file=f)
    print(f"The best performing month is {best_month} with ${max(pl_change)} in profit.", file=f)
    print(f"The worst performing month is {worst_month} with ${min(pl_change)} in loss.", file=f)
#how to fetch months for corresponding max/min?
#best/worth months not required according to rubric so decided not to struggle more with it.