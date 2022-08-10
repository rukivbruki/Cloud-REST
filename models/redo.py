from helpers import update_stack
from settings import datastore_client
from helpers.getter import get_name, get_stack


def call_redo():
    pointer = get_stack('pointer') - 1
    operations = get_stack('operations')
    update_stack('pointer', pointer)

    if pointer < 0:
        return "NO COMMANDS"

    curr_entity = operations[pointer]
    curr_name = curr_entity["task"]["name"]
    curr_value = curr_entity["task"]["value"]
    command = curr_entity["command"]

    if command == "unset":
        datastore_client.delete(curr_entity["task"])
        return f"{curr_name} = {get_name(curr_name)}"
    elif command == "set":
        datastore_client.put(curr_entity["task"])
        return f"{curr_name} = {curr_value}"
