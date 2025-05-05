from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    # You could verify payload['ref'] or signature here
    subprocess.run("cd /home/ec2-user/my-repo && git pull", shell=True)
    # Optionally restart your app if needed
    subprocess.run("sudo systemctl restart fastapi", shell=True)
    return {"message": "Git pull triggered"}
