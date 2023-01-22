import json
import logging
import os

from flask import Flask, request
from supabase import Client, create_client
from werkzeug.middleware.proxy_fix import ProxyFix

from .utils import check_signature

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


def save(dataset):
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    r = supabase.table("generated").select("*").execute()
    data = supabase.table("generated").insert(dataset).execute()
    app.logger.info(data)


@app.route("/", methods=["POST", "GET"])
async def home():
    if request.method == "GET":
        return "nothing to see here"
    else:
        data = request.data
        signature = request.headers.get("X-MYAX-SIGNATURE")
        secret = os.environ.get("AX_WEBHOOK_SECRET")
        if check_signature(signature, data, secret):
            app.logger.info("signature valid")
            dataset = json.loads(data)
            dataset["document_id"] = dataset.pop("id")
            save(dataset)

    return "OK"
