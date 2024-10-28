from fastapi import FastAPI, Request, HTTPException
import hmac
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
Payload={}

app = FastAPI()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET").encode()  

@app.post("/webhook")
async def webhook_listener(request: Request):
    # Verify the signature
    signature = request.headers.get("X-Hub-Signature-256")
    if not signature:
        raise HTTPException(status_code=400, detail="Signature missing")

    body = await request.body()
    mac = hmac.new(WEBHOOK_SECRET, body, hashlib.sha256)
    expected_signature = f"sha256={mac.hexdigest()}"

    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")

    # Process event
    payload = await request.json()
    Payload=payload
    event_type = request.headers.get("X-GitHub-Event")

    # Process event based on type
    if event_type == "issues":
        # Issue Processing
        print("Issue event received:")
    elif event_type == "pull_request":
        # PR Processing
        print("PR event received:")

    # print(f"Received event: {event_type}")
    return {"status": "Webhook received"}