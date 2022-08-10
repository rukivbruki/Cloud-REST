import zlib
from google.cloud import datastore

from settings import datastore_client


def init_stack():
    operations_task = datastore.Entity(datastore_client.key("Stack", zlib.crc32(b'operations')))
    pointer_task = datastore.Entity(datastore_client.key("Stack", zlib.crc32(b'pointer')))
    operations_task.update({'value': [], 'name': 'operations'})
    pointer_task.update({'value': 1, 'name': 'pointer'})
    datastore_client.put_multi([operations_task, pointer_task])