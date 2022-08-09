from helpers import prefill_stack, clean_stack
from settings import datastore_client


def call_unset(name, operations_name):
    query = datastore_client.query(kind="Task")
    query.add_filter("name", "=", name)
    results = list(query.fetch())

    prefill_stack(operations_name, results)
    clean_stack()
    datastore_client.delete_multi(results)

    return "None"
