import csv
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{"host":"localhost", "port":9200}])

def create_index(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Index '{index_name}' created.")

def insert_data(index_name, csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            es.index(index=index_name, body=row)

if __name__ == "__main__":
    index_name = "courses"
    csv_file_paths = ["./data/output.csv"]

    create_index(index_name)

    for csv_file_path in csv_file_paths:
        insert_data(index_name,csv_file_path)