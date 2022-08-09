from google.cloud import datastore

datastore_client = datastore.Client.from_service_account_json(
    r"path to json")

# datastore_client = datastore.Client()
