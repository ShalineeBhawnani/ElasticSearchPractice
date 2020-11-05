from datetime import datetime
from elasticsearch import Elasticsearch

data = {
        "author": "Chestermo",
        "gender": "male",
        "age": "24",
        "body_fat": "15%",
        "interest": ["couch potato", "eat and sleep"]
    }

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

def insert_one_data(_index, data):
    res = es.index(index=_index, doc_type='authors', id=1, body=data)
    # index will return insert info: like as created is True or False
    print(res)

def insert_data_by_bulk(data):
    res = helpers.bulk(es, data)
    print(res)

# Delete an Elasticsearch index
def delete_index(es_object, index_name):
    try:
        if es_object.indices.exists(index_name):
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

def search_by_index_and_id(es,_index, _id):
    res = es.get(
        index=_index,
        id=_id
    )
    print(res)
    return res

es = connect_elasticsearch()
# create_index(es,'author')
# insert_one_data('author', data)
search_by_index_and_id(es,'author', 1)

# get_index(es)

