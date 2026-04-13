from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"message": "Server is running"}

# Log ingestion endpoint
@app.post("/api/logs")
def receive_logs(log: dict):
    print("Received log:", log)

    return {
        "status": "success",
        "received_data": log
    }