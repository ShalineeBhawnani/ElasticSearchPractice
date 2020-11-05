from datetime import datetime
from elasticsearch import Elasticsearch

def connect_elasticsearch():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es.ping():
        print('Connected')
    else:
        print('could not connect!')
    return es
def create_index(es_object, index_name):
    created = False
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(index=index_name)
            print('Created Index',index_name)
        created = True
    except Exception as ex:
        print("exception",str(ex))
    finally:
        print("already there")
        return created

es = connect_elasticsearch()
create_index(es,'recipes')

