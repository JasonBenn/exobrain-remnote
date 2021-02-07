import json
from pprint import pprint
from typing import Dict

import requests
from dotenv import load_dotenv
import os
load_dotenv()

REMNOTE_API_KEY = os.getenv("REMNOTE_API_KEY")
REMNOTE_USER_ID = os.getenv("REMNOTE_USER_ID")


def get_by_name(name: str) -> Dict:
  response = requests.post("https://api.remnote.io/api/v0/get_by_name", {
    "apiKey": REMNOTE_API_KEY,
    "userId": REMNOTE_USER_ID,
    "name": name,
  })
  return json.loads(response.text)


def delete_by_name(remID: str) -> bool:
  response = requests.post("https://api.remnote.io/api/v0/delete", {
    "apiKey": REMNOTE_API_KEY,
    "userId": REMNOTE_USER_ID,
    "remId": remID,
  })
  response.raise_for_status()
  return response.status_code == 200


while rem := get_by_name("Untitled"):
  should_delete = rem["visibleRemOnDocument"] == []
  if should_delete:
    pprint(rem)
    delete_by_name(rem['_id'])
