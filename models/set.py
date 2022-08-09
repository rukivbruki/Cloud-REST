import zlib
from helpers import prefill_stack, clean_stack
from settings import datastore_client
from google.cloud import datastore


def call_set(name, value, operations_name):
    task = datastore.Entity(datastore_client.key("Task", zlib.crc32(bytes(name, 'ascii'))))
    task.update(
        {"name": name, "value": value}
    )

    prefill_stack(operations_name, task)
    clean_stack()
    datastore_client.put(task)

    return f"{name} = {value}"
