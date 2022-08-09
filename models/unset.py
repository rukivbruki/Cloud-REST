import shared
from settings import datastore_client


def call_unset(name, operations_name):
    query = datastore_client.query(kind="Task")
    query.add_filter("name", "=", name)
    results = list(query.fetch())

    shared.operations.insert(1, {'command': operations_name, "task": results})
    if shared.pointer > 1:
        del shared.operations[2:shared.pointer + 1]

    shared.pointer = 1

    datastore_client.delete_multi(results)

    return "None"
