from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import os
from tqdm import tqdm

es = Elasticsearch([{'host':'localhost', 'port': 9200}])
es.indices.delete(index='glassdoor_reviews', ignore=[400, 404])
es.indices.create(index='glassdoor_reviews', ignore=400)
DATA_PATH='data'

def populate_elasticsearch():
    doc=[]
    for file in tqdm(os.listdir(DATA_PATH)):
        with open(os.path.join(DATA_PATH,file),encoding='utf-8') as f:
            company=file.replace('.txt','')
            for line in f:
                data=json.loads(line)
                authorInfo=data['authorInfo'].split('-')
                mydict={
                    "company": company,
                    "rating": data['rating'],
                    "pros": data['pros'],
                    "cons": data['cons'],
                    "adviceManagement": data['adviceManagement'],
                    "dateReviewed": authorInfo[0].strip(),
                    "authorInfo": authorInfo[1].strip(),
                    "authorLocation": data['authorLocation']
                }
                doc.append(mydict)
                if len(doc) >= 1000:
                    bulk(es, doc, index="glassdoor_reviews")
                    doc = []
    print(len(doc))
    bulk(es, doc, index="glassdoor_reviews")


if __name__ == "__main__":
    populate_elasticsearch()
