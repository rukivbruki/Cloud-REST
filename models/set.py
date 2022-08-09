from settings import datastore_client
from google.cloud import datastore
import shared


def call_set(name, value, operations_name):
    task = datastore.Entity(datastore_client.key("Task", hash(name)))
    task.update(
        {"name": name, "value": value}
    )

    if len(shared.operations) == 0:
        shared.operations.append({'command': operations_name, "task": "NO COMMANDS"})
        shared.operations.append({'command': operations_name, "task": "NO COMMANDS"})

    shared.operations.insert(1, {'command': operations_name, "task": [task]})
    if shared.pointer > 1:
        del shared.operations[2:shared.pointer + 1]

    shared.pointer = 1

    datastore_client.put(task)

    return f"{name} = {value}"
