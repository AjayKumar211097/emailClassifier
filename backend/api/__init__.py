import azure.functions as func
from azure.functions import AsgiMiddleware
from fastapi import FastAPI

# Minimal, simplest test app definition: 
app_fastapi = FastAPI()

@app_fastapi.get("/")
async def root():
    return {"Hello": "World!"}

# the simplest documented way:
app = AsgiMiddleware(app_fastapi).main