
# Convert ADVENTURECARDS JSON file to CSV
# (it's not elegant but it works)

import json
import csv
import ast
import sys

# Opens JSON file and loads the data with open('data.json') as json_file:'

# read file
with open('adventuredecks_file.json', 'r') as f:
    data = f.read()

#grab items
decks_data = json.loads(data)

#creat output CSV file and writer
csv_file = open('adventuredecks.csv', 'w')
#csv_writer = csv.writer(csv_file)

def_stdout = sys.stdout
sys.stdout = csv_file

for deck in decks_data:
    #cleanup
    str1 = str(ast.literal_eval(deck))+","
    str2 = str(ast.literal_eval(json.dumps(decks_data[deck]["items"])))
    str3 = str1 + str2.replace("'","").replace("[", "")

    #print the thing
    print(str3)

sys.stdout = def_stdout
csv_file.close()