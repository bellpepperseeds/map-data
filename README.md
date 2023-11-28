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
2. Download requirements
>   `python -m pip install -r requirements.txt`
3. Update environment variables or add .env with:
- URI=your MongDB cluster connection string
- DB=your database name you plan on using
4. Run with uvicorn
>   `uvicorn main:app --reload`
5. Get data???
>   `your-url/collection-name`<br>
>   `your-url/collection-name/search-term`

