from settings import datastore_client


def call_numequalto(value):
    query = datastore_client.query(kind="Task")
    query.add_filter("value", "=", value)

    results = list(query.fetch())

    return f"{len(results)}"
