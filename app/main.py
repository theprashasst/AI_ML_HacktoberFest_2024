from fastapi import FastAPI, Request, HTTPException
import hmac
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
repo_path="https://github.com/theprashasst/IdentifyMe-AI"           #example Repo path

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
    event_type = request.headers.get("X-GitHub-Event")

    #if even is push then update the embeddings 
    if event_type == "push":
        repo_path=payload["repository"]["html_url"]
        # embeddings updation
        pass

    # Process event based on type
    elif event_type == "issues":
        # Issue Processing
        print("Issue event received:")
    elif event_type == "pull_request":
        # PR Processing
        print("PR event received:")

    # print(f"Repo path: {repo_path}")
    return {"status": "Webhook received"}