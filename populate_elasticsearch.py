from elasticsearch import Elasticsearch, helpers
import json

def populate_elasticsearch():
    es = Elasticsearch([{'host':'localhost', 'port': 9200}])
    doc=[]
    with open('data/Amazon.txt', encoding='utf-8') as f:
        for line in f:
            doc.append(json.loads(line))
    print(len(doc))
    print(doc[20])
    helpers.bulk(es, doc, index='amazon',doc_type='_doc', request_timeout=200)

if __name__ == "__main__":
    populate_elasticsearch()