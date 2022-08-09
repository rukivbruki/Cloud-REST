import shared
from settings import datastore_client
from helpers.filter import name_filter


def call_undo():
    if shared.pointer > len(shared.operations) - 2:
        return "NO COMMANDS"

    curr_entity = shared.operations[shared.pointer]
    curr_name = curr_entity["task"][0]["name"]
    curr_value = curr_entity["task"][0]["value"]
    prev_entity = shared.operations[shared.pointer + 1]
    command = curr_entity["command"]

    if command == "set":
        datastore_client.delete(curr_entity["task"][0])
        if shared.pointer < len(shared.operations) - 2:
            datastore_client.put_multi(prev_entity["task"])
        shared.pointer += 1

        return f"{curr_name} = {name_filter(curr_name)}"

    elif command == "unset":
        print(curr_entity["task"])
        datastore_client.put_multi(curr_entity["task"])
        shared.pointer += 1

        return f"{curr_name} = {curr_value}"
