# backend/function_app.py

import azure.functions as func
from azure.functions import AsgiFunctionApp
from fastapi import FastAPI, Depends, HTTPException
from llmservice.classifier import classify_description
from emailservice.mailer import send_email


app_fastapi = FastAPI(title="Maintenance API")

# CRUD endpoints
@app_fastapi.get("/")
async def root():
    return {"status": "Backend är igång!"}

@app_fastapi.post("/maintenance/")
def create_record(data):
    # classify and notify
    tag = classify_description(data.description)
    send_email(
        recipient="admin@example.com",
        subject=f"[{data.provider}] Maintenance – {tag}",
        body=f"{data.description}\nStart: {data.start_time}\nEnd: {data.end_time}"
    )
    return {"Message": "Email Sent"}

@app_fastapi.get("/maintenance/")
def read_records():
    return {"ok": True}

@app_fastapi.get("/maintenance/{id}")
def read_record(id):
       # classify and notify
    print(f"--- Sending Email ---")
    return {"Message": id+"Read Success"}

# Wrap FastAPI app for Azure Functions (v4)
app = AsgiFunctionApp(app=app_fastapi, http_auth_level=func.AuthLevel.ANONYMOUS)
