import zlib

from helpers import prefill_stack, clean_stack
from settings import datastore_client


def call_unset(name, operations_name):
    key = datastore_client.key("Task", zlib.crc32(bytes(name, 'ascii')))

    task = datastore_client.get(key)

    prefill_stack(operations_name, task)
    clean_stack()
    datastore_client.delete(task)

    return "None"
