import zlib

from settings import datastore_client


def update_stack(name, value):
    with datastore_client.transaction():
        key = datastore_client.key("Stack", zlib.crc32(bytes(name, 'ascii')))

        task = datastore_client.get(key)

        task.update({"value": value, "name": name})
        datastore_client.put(task)
