## ax-supabase

store the webhook from AX in supabase

this demo uses Flask and is deployed on fly.io


### setup

Create a table in supabase named "generated" and add the following fields (keep `id` and `created_at`):
```
document_id: uuid
uid: text
text: text
text_modified: timestamp without time zone
collection_id: int8
collection_name: text
language: varchar
html: text
html_axite: text
```

create a fly app with `fly launch`

add secrets (get them from your supabase project api settings):
```
flyctl secrets set SUPABASE_URL=my-url-to-my-awesome-supabase-instance
flyctl secrets set SUPABASE_KEY=my-supa-dupa-secret-supabase-api-key
```

and the webhook secret from AX:
```
flyctl secrets set AX_WEBHOOK_SECRET=copy-from-collection-settings-and-set-url-too
```


### deploy

```
flyctl deploy
```


### development

```
python -m pip install -r requirements.txt
FLASK_APP=app.main flask run
```
