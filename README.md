# PYTHON API FOR VIEWING MONGODB CLUSTER DATA

Intended for use in a school project, but if you want to have
a simple way to get your data as text, this can work for you.

## FIND ONE OR FIND ALL

Find one document with a specific name/searchTerms field,
or just get all the documents in a collection.
Getting an entire collection DOESN'T need similar data structure.

## INSTALLATION
1. Set up environment
>   `python -m venv (your venv name)`
- Download requirements
>   `python -m pip install -r requirements.txt`
- Run with uvicorn
>   `uvicorn main:app --reload`
- Get data???
>   `your-url/collection-name`<br>
>   `your-url/collection-name/search-term`