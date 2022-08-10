from helpers import update_stack
from settings import datastore_client


def call_end():
    fetch_limit = 100
    entities = True
    update_stack("operations", [])

    while entities:
        query = datastore_client.query(kind='Task')
        entities = list(query.fetch(limit=fetch_limit))
        for entity in entities:
            datastore_client.delete(entity.key)

    return 'CLEANED'
