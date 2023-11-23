from fastapi import FastAPI
import json
from pymongo import MongoClient



def get_uri():
    """
    Gets the first line of the file .info as the uri for a mongdoDB database
    """

    with open('.info','r') as file:
        return file.readline().strip()
    

client = MongoClient(get_uri())
print('Connected to client')
db = client['pnwmap']
print('Got db')

def find_doc(collection, search=''):
    """
    Returns JSON string of the query results in a collection

    Parameters
    ----------
    collection : str
        Name of the collection to search

    search : str
        Used to find documents with either the same name field or
        in the searchTerms field, can be empty
    """

    res = db[collection].find_one(
        {'$or': [
            {'name': search},
            {'searchTerms': search}
        ]}
    )

    return str(res)

def get_all(collection):
    """
    Returns JSON string of all documents in a collection

    Parameters
    ----------
    collection : str
        Name of the collection to search
    """

    res = db[collection].find({})

    return str(list(res))

# Start app
app = FastAPI()

# Not sure if this is necessary, but it is there
@app.get('/')
async def root():
    return {'message': 'you need to specify your intent'}

# route to get all documents in a collection
@app.get('/{collection}')
async def root(collection):
    return {'message': get_all(collection)}

# route to search for specific data
@app.get('/{collection}/{search}')
async def root(collection, search):
    return {'message': find_doc(collection, search)}