import json
import os
from datetime import datetime


FILE = "logs/history.json"


def save_prediction(data):

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(FILE):

        with open(FILE,"r") as f:
            history=json.load(f)

    else:
        history=[]


    data["date"]=str(datetime.now())

    history.append(data)


    with open(FILE,"w") as f:
        json.dump(history,f,indent=4)



def load_history():

    if os.path.exists(FILE):

        with open(FILE,"r") as f:
            return json.load(f)

    return []