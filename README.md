# PYTHON API FOR VIEWING MONGODB CLUSTER DATA HOSTED ON HEROKU

Intended for use in a school project, but if you want to have
a simple way to get your data as text, this can work for you.

## FIND ONE OR FIND ALL

Find one document with a specific name/searchTerms field,
or just get all the documents in a collection.
Getting an entire collection DOESN'T need similar data structure.

## INSTALLATION
1. Set up environment (or don't)
>   `python -m venv (your venv name)`
<br>
2. Download requirements
>   `python -m pip install -r requirements.txt`
<br>
3. Update environment variables or add .env with:
- URI=(your MongDB cluster connection string)
- DB=(your database name you plan on using)
<br>
4. If local Run with uvicorn
>   `uvicorn main:app` or `uvicorn main:app --reload`
<br>
5. Get data???
>   Get an entire collection
>   `your-url/search/(collection-name)`<br>
>   Get documents with specific names
>   `your-url/serach/(collection-name)/(search-term)`<br>
- Returns as a JSON list of selected documents

