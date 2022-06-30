## Modele imports ##
from glob import glob
import re
import json
import sqlite3
#####################

## Main Code ##
conn = sqlite3.connect('json.db')

cur = conn.execute("SELECT ID FROM jsons;")
print(f"Last ID in database is {cur.fetchall()[-1][0]}, make sure json files are named correctly (aka bigger than 29).")
if input("Continue? y/N: ").lower() not in ["y", "yes"]:
    print("Change file names and run program again.")
    exit()

for file in glob('./json/*.json'):
    with open(file, "r", encoding="utf-8") as j:
        data = json.load(j)
        stringified_data = json.dumps(data)
        ID = re.findall(r'\d+', file)[0]
        try:
            conn.execute(f"INSERT INTO jsons (ID,JSON) VALUES ({ID}, '{stringified_data}');")
        except sqlite3.IntegrityError:
            print(f"Skipping file, object with ID {ID} already exists.")
            continue
        print(f"Added {file}.")

print("Jsons added, do you want to commit to db?")
if input("Continue? y/N: ").lower() not in ["y", "yes"]:
    conn.rollback()
    print("Changes reverted, db was untouched.")
    exit()

conn.commit()
print("Changes commited to db! Ending.")
conn.close()