from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GitOps Pipeline Deployed via Render", "status": "success"}

@app.get("/version")
def read_version():
    return {"version": "1.0.1", "environment": "production"}
