from datetime import datetime
from elasticsearch import Elasticsearch

def connect_elasticsearch():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es.ping():
        print('Connected')
    else:
        print('could not connect!')
    return es

# Create an Elasticsearch index
def create_index(es_object, index_name):
    created = False
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(index=index_name)
            print('Created Index',index_name)
        else :
            print('Index Already Exist',index_name)
        created = True
    except Exception as ex:
        print("exception",str(ex))
    finally:
        return created

# Delete an Elasticsearch index
def delete_index(es_object, index_name):
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.delete(index=index_name)
            print('Deleted Index',index_name)
    except Exception as ex:
        print("exception",str(ex))

# Get every indices class in a cluster
def get_index(es_object):
    indices_dict = es_object.indices.get_alias("*")
    indices_dicts = es_object.indices.get_alias().keys()

    print(indices_dict.items())
    print("get index names only in cluster",indices_dicts)
    
es = connect_elasticsearch()
# create_index(es,'recipes')
get_index(es)

