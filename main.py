## Module imports ##
from typing import Union
from fastapi import FastAPI, Response
import json
import random
#####################

## Main Code ##
app = FastAPI()

@app.get("/")
def read_root(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    number = random.randint(1,29)
    j = open(f'./json/{number}.json')
    return json.load(j)

print("Server is running...")