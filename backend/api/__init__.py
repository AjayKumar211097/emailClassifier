import azure.functions as func
from azure.functions import AsgiMiddleware
from fastapi import FastAPI

from llmservice.classifier import classify_description
from emailservice.mailer import send_email

from pymongo import MongoClient
import certifi


app_fastapi = FastAPI()

@app_fastapi.get("/")
async def root():
    return {"Hello": "World!"}

@app_fastapi.post("/maintenance/")
async def create_record(data: dict):
    tag = classify_description(data["description"])
    send_email(
    recipient="admin@example.com",
    subject=f"[{data['provider']}] Maintenance – {tag}",
    body=f"{data['description']}\nStart: {data['start_time']}\nEnd: {data['end_time']}"
    )
    return {"Message": "Email Sent"}

@app_fastapi.get("/maintenance/")
async def read_records():
    return {"ok": True}

@app_fastapi.get("/maintenance/{id}")
async def read_record(id: int):
    return {"Message": f"{id} Read Success"}

# MongoDB connection
ProdDB = "mongodb+srv://skoglund1:JakobSkoglund2001@junet-cluster.uzee4js.mongodb.net/?retryWrites=true&w=majority&appName=Junet-Cluster"
client = MongoClient(ProdDB, tlsCAFile=certifi.where())
db = client["llm_analys"]
collection = db["driftstorningar"]

@app_fastapi.get("/driftstorningar")
async def get_driftstorningar():
    data = list(collection.find({}, {"_id": 0}))
    return data

app = AsgiMiddleware(app_fastapi).main