from settings import datastore_client
from helpers import get_name, update_stack, get_stack


def call_undo():
    pointer = get_stack('pointer')
    operations = get_stack('operations')

    if pointer > len(operations) - 2:
        return "NO COMMANDS"

    curr_entity = operations[pointer]
    curr_name = curr_entity["task"]["name"]
    curr_value = curr_entity["task"]["value"]
    prev_entity = operations[pointer + 1]
    command = curr_entity["command"]

    if command == "set":
        datastore_client.delete(curr_entity["task"])
        if pointer < len(operations) - 2:
            datastore_client.put(prev_entity["task"])
        update_stack('pointer', pointer + 1)

        return f"{curr_name} = {get_name(curr_name)}"

    elif command == "unset":
        datastore_client.put(curr_entity["task"])
        update_stack('pointer', pointer + 1)

        return f"{curr_name} = {curr_value}"
