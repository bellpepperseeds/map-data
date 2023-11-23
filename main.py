from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
import os

def find_doc(db, collection, search=''):
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

def get_all(db, collection):
    """
    Returns JSON string of all documents in a collection

    Parameters
    ----------
    collection : str
        Name of the collection to search
    """

    res = db[collection].find({})

    return str(list(res))

# Load .env as environment variables
load_dotenv()

# Connect to cluster with URI
with MongoClient(os.environ.get('URI')) as client:
    ##print('Connected to client')

    # Connect to database
    db = client[os.environ.get('DB')]
    ##print('Got db')

    # Start app
    app = FastAPI()

    # Not sure if this is necessary, but it is there
    @app.get('/')
    async def root():
        return {'message': 'you need to specify your intent'}

    # route to get all documents in a collection
    @app.get('/{collection}')
    async def root(collection):
        return {'message': get_all(db, collection)}

    # route to search for specific data
    @app.get('/{collection}/{search}')
    async def root(collection, search):
        return {'message': find_doc(db, collection, search)}
