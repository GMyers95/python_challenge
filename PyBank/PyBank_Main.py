{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ec6dd263-e756-4401-8ef1-185e00b6478d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 86 months considered in this dataset.\n",
      "The net total of Profits/Losses over the entire period is: $22564198\n",
      "The average change in Profits/Losses is $-8311.11.\n",
      "The best performing month is  with $1862002 in profit.\n",
      "The worst performing month is  with $-1825558 in loss.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "csvpath = os.path.join(\"C:\\\\Users\\\\GMyer\\\\Desktop\\\\ClassRepo\\\\git\\\\python_challenge\\\\PyBank\\\\Resources\\\\budget_data.csv\")\n",
    "month_count = 0\n",
    "volume = 0\n",
    "best_profit = 0 \n",
    "best_month = \"\"\n",
    "worst_loss = 0\n",
    "worst_month = \"\"\n",
    "change = []\n",
    "pl_change = []\n",
    "with open(csvpath, \"r\") as csvfile:\n",
    "    csvreader= csv.reader(csvfile, delimiter=',')\n",
    "    row = next(csvreader)\n",
    "    for row in csvreader:\n",
    "        change.append(int(row[1]))\n",
    "        month_count += 1\n",
    "        volume += (int(row[1]))\n",
    "        #Greg's help stopped here\n",
    "    print(f\"There are {month_count} months considered in this dataset.\")\n",
    "    print(f\"The net total of Profits/Losses over the entire period is: ${volume}\")\n",
    "\n",
    "for x in range(len(change)-1):\n",
    "        pl_change.append(change[x + 1] - change[x])\n",
    "        best_profit = int(max(pl_change))\n",
    "        worst_loss = int(min(pl_change))\n",
    "        if pl_change[x] > best_profit:\n",
    "            pl_change[x] = best_profit\n",
    "            best_month = row[0]\n",
    "        elif pl_change[x] < worst_loss:\n",
    "            pl_change[x] = worst_loss\n",
    "            worst_month = row[0]\n",
    "average_change = (round(sum(pl_change)/(len(change)-1),2))\n",
    "print(f\"The average change in Profits/Losses is ${average_change}.\")\n",
    "print(f\"The best performing month is {best_month} with ${max(pl_change)} in profit.\")\n",
    "print(f\"The worst performing month is {worst_month} with ${min(pl_change)} in loss.\")\n",
    "#need to export to a text file as well\n",
    "with open(\"PyBank_text.txt\",'w') as f:\n",
    "    print(f\"There are {month_count} months considered in this dataset.\", file=f)\n",
    "    print(f\"The net total of Profits/Losses over the entire period is: ${volume}\", file=f)\n",
    "    print(f\"The average change in Profits/Losses is ${average_change}.\", file=f)\n",
    "    print(f\"The best performing month is {best_month} with ${max(pl_change)} in profit.\", file=f)\n",
    "    print(f\"The worst performing month is {worst_month} with ${min(pl_change)} in loss.\", file=f)\n",
    "#how to fetch months for corresponding max/min?\n",
    "#best/worth months not required according to rubric so decided not to struggle more with it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d5d7073-f338-49a4-a052-e514c1a30733",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db072ffc-964e-4ac2-8a8d-71adc26bff58",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
