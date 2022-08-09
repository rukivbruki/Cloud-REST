import shared
from settings import datastore_client
from helpers.getter import get_name


def call_redo():
    shared.pointer -= 1

    if shared.pointer < 0:
        return "NO COMMANDS"

    curr_entity = shared.operations[shared.pointer]
    curr_name = curr_entity["task"][0]["name"]
    curr_value = curr_entity["task"][0]["value"]
    command = curr_entity["command"]

    if command == "unset":
        datastore_client.delete(curr_entity["task"][0])
        return f"{curr_name} = {get_name(curr_name)}"
    elif command == "set":
        datastore_client.put_multi(curr_entity["task"])
        return f"{curr_name} = {curr_value}"
