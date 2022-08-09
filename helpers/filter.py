from settings import datastore_client


def name_filter(name):
    query = datastore_client.query(kind="Task")
    query.add_filter("name", "=", name)
    results = list(query.fetch())

    if results:
        value = list(query.fetch())[0]["value"]
        return value
    else:
        return "None"
