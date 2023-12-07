from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
import os
import sys
import json
from bson.json_util import dumps

def find_docs(db, collection, search=''):
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

    res = db[collection].find(
        {
            '$or': [
                {
                    'name': {
                        '$regex': search,
                        '$options': 'i',
                        '$exists': True
                    }
                },
                {
                    'abbr': {
                        '$regex': search,
                        '$options': 'i',
                        '$exists': True
                    } 
                }
        ]}
    )

    return json.loads(dumps(res))

def get_all(db, collection):
    """
    Returns JSON string of all documents in a collection

    Parameters
    ----------
    collection : str
        Name of the collection to search
    """

    res = db[collection].find({})

    return json.loads(dumps(res))

# Load .env as environment variables
load_dotenv()

# Set up client
client = None
try:
    # Connect to cluster with URI
    client = MongoClient(os.environ.get('URI'))
except ConfigurationError:
    print('Could not connect to the cluster')
    sys.exit()


# Connect to database
db = client[os.environ.get('DB')]


# Start app
app = FastAPI()

# Not sure if this is necessary, but it is there
@app.get('/')
async def root():
    return 'get the bts meal from mcdonalds'

# route to get all documents in a collection
@app.get('/search/{collection}')
async def root(collection):
    return get_all(db, collection)

# route to search for documents in a collection
@app.get('/search/{collection}/{name}')
async def root(collection, name):
    return find_docs(db, collection, name)
