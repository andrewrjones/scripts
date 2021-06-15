import argparse
from google.cloud import bigquery

parser = argparse.ArgumentParser()
parser.add_argument('--dry', action='store_true')
parser.add_argument('--dataset', action='store', type=str, required=True)
args = parser.parse_args()

client = bigquery.Client()

dataset_id=args.dataset
tables = client.list_tables(dataset_id)
    
for table in tables:
    # TODO: I think the API has a proper ID
    id =".".join([table.project,table.dataset_id,table.table_id])

    print(id)
    
    if not args.dry:
        client.delete_table(id)