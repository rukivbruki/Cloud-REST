import shared
from settings import datastore_client


def call_end():
    fetch_limit = 100
    entities = True
    shared.operations = []

    while entities:
        query = datastore_client.query(kind='Task')
        entities = list(query.fetch(limit=fetch_limit))
        for entity in entities:
            datastore_client.delete(entity.key)

    return 'CLEANED'
