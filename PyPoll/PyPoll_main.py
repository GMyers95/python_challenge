{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ff755fe9-3ffc-464b-978e-92ed7de23124",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 369711 total votes in this dataset.\n",
      "Charles Casper Stockham received 23.049% (85213) of the total votes.\n",
      "Diana DeGette received 73.812% (272892) of the total votes.\n",
      "Raymon Anthony Doane received 3.139% (11606) of the total votes.\n",
      "Diana DeGette wins this election!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "csvpath = os.path.join(\"C:\\\\Users\\\\GMyer\\\\Desktop\\\\ClassRepo\\\\git\\\\python_challenge\\\\PyPoll\\\\Resources\\\\election_data.csv\")\n",
    "total_votes = 0\n",
    "candidates = []\n",
    "unique_cands = {}\n",
    "most_votes = 0\n",
    "winner = \"\"\n",
    "x = unique_cands.keys()\n",
    "with open(csvpath, \"r\") as csvfile:\n",
    "    csvreader= csv.reader(csvfile, delimiter=',')\n",
    "    row = next(csvreader)\n",
    "    for row in csvreader:\n",
    "        total_votes += 1\n",
    "        candidates.append(row[2])\n",
    "    print(f\"There are {total_votes} total votes in this dataset.\")\n",
    "    for candidate in candidates: \n",
    "        if not candidate in unique_cands.keys():\n",
    "            unique_cands[candidate] = 1\n",
    "        else:\n",
    "            unique_cands[candidate] += 1\n",
    "    for k,v in unique_cands.items():\n",
    "        print(f\"{k} received {round(((v)/total_votes)*100,3)}% ({v}) of the total votes.\")\n",
    "        if (v) > int(most_votes):\n",
    "            most_votes = (v)\n",
    "        if (v) == most_votes:\n",
    "            winner = (k)\n",
    "    print(f\"{winner} wins this election!\")\n",
    "#Send script as text file\n",
    "with open(\"PyPoll_text.txt\",'w') as f:\n",
    "    print(f\"There are {total_votes} total votes in this dataset.\", file=f)\n",
    "    for k,v in unique_cands.items():\n",
    "        print(f\"{k} received {round(((v)/total_votes)*100,3)}% ({v}) of the total votes.\", file=f)\n",
    "    print(f\"{winner} wins this election!\", file=f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9786b35-4b02-405a-bb6f-2450d50fcacc",
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
