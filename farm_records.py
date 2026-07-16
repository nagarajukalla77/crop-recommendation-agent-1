import json
import os


FILE="records/farm_records.json"


def save_farm_record(record):

    os.makedirs(
        "records",
        exist_ok=True
    )


    if os.path.exists(FILE):

        with open(FILE,"r") as f:
            data=json.load(f)

    else:

        data=[]


    data.append(record)


    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)



def get_records():

    if os.path.exists(FILE):

        with open(FILE,"r") as f:
            return json.load(f)

    return []