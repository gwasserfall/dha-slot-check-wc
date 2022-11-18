from dataclasses import dataclass
from datetime import datetime, timedelta

import requests
import time

import os

@dataclass
class branch_map:
    Capetown = "YCI"
    Wynberg =  "YIN"
    George = "YCF"


today = datetime.now()

date_from = (today + timedelta(days=1)).strftime("%d-%m-%Y")
date_to = (today + timedelta(days=8)).strftime("%d-%m-%Y")

branch_code = branch_map.Capetown

params = {
    "branch_code" : branch_code,
    "date_from" : date_from,
    "date_to": date_to,
    "send_date" : int(time.time())
}

push_hash = os.getenv("PUSH_GUID", ":(")

r = requests.get("https://services.dha.gov.za/api/appointment/gettimeslotdetails/", params=params)

payload = r.json()["Payload"]

if len(payload) > 2:
    # showcase
    requests.get(f"""https://push.techulus.com/api/v1/notify/{push_hash}?title=Slots Available!&body=Quickly reserve a slot for Capetown!!""")

else:
    print(f"{datetime.now()} : No slots...")
