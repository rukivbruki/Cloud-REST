import requests

BASE = "https://fstp-358817.uw.r.appspot.com/undo"

GET = "name=ivan"
NUMEQUALTO = "numequalto?value=32"
SET = "set?name=ivan&value=33"
UNSET = "unset.py?name=ivan"
UNDO = '/undo'
REDO = '/redo'
END = "/end"

response = requests.get(BASE)

print(response.text)

