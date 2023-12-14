from google.cloud import storage, bigquery
import os
import json

# Fungsi memasukkan data ke GCS
def write_to_gcs(bucket_name, blob_name, data_list):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    json_data = json.dumps(data_list)
    blob.upload_from_string(json_data)

# Fungsi ekstrak data dari GCS
def read_gcs(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_text()
    return data

# Fungsi memindahkan data ke BigQuery
def write_bigquery(table_id, insert_table_json):
    client = bigquery.Client()
    table = client.get_table(table_id)
    insert_table = json.loads(insert_table_json)
    errors = client.insert_rows_json(table, insert_table)
    if errors:
        print('Errors occurred: {}'.format(errors))
    else:
        print('Successfully')

# Data yg dimasukkan
bucket_name = os.getenv('BUCKET_NAME')
blob_name = 'taufik_task1.json'
data_list = [
    {"name": "taufik", "age": 22, "city": "Jakarta", "gender": "Male"},
    {"name": "ali", "age": 25, "city": "bandung", "gender": "Male"},
    {"name": "nisa", "age": 28, "city": "makassar", "gender": "Female"},
    {"name": "tiara", "age": 32, "city": "yogyakarta", "gender": "Female"}
]
write_to_gcs(bucket_name, blob_name, data_list)

data = read_gcs(bucket_name, blob_name)
insert_table_json = data
project_id = os.getenv('PROJECT_ID')
table_id = f'{project_id}.my_dataset.my_table'
write_bigquery(table_id, insert_table_json)