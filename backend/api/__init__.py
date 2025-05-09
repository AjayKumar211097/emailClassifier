import azure.functions as func
from azure.functions import AsgiFunctionApp
from fastapi import FastAPI, HTTPException
from llmservice.classifier import classify_description
from emailservice.mailer import send_email

app_fastapi = FastAPI(title="Maintenance API")

@app_fastapi.get("/")
async def root():
    return {"status": "Backend är igång!"}

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

app = AsgiFunctionApp(app=app_fastapi, http_auth_level=func.AuthLevel.ANONYMOUS)
