## Module imports ##
from typing import Union
from fastapi import FastAPI, Response
import json
import random
import sqlite3
#####################

## Main Code ##
app = FastAPI()
conn = sqlite3.connect('json.db')

@app.get("/")
def read_root(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    number = random.randint(1,29)
    cur = conn.execute(f"SELECT jsons FROM jsons WHERE ID={number};")
    img = json.load(cur.fetchall()[0])
    return img

print("Server is running...")