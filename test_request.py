import requests

BASE = "http://127.0.0.1:8080/"

GET = "name=ivan"
NUMEQUALTO = "numequalto?value=32"
SET = "set?name=ivan&value=33"
UNSET = "unset.py?name=ivan"
UNDO = '/undo'
REDO = '/redo'
END = "/end"

response = requests.get(BASE + SET)

print(response.text)

