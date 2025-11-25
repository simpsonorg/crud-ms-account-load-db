from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="crud-ms-account-load-db")

DEMO = {
    "101": {
        "customerId": "101",
        "firstName": "John",
        "lastName": "Doe",
        "birthDate": "1990-01-01",
        "email": "john.doe@example.com"
    }
}

class Demographic(BaseModel):
    customerId: str
    firstName: str | None = None
    lastName: str | None = None
    birthDate: str | None = None
    email: str | None = None   # <-- NEW FIELD ADDED

@app.get("/demographic/{customerId}")
def get_demographic(customerId: str):
    return DEMO.get(customerId, {"error": "not-found"})

@app.post("/demographic")
def save_demographic(rec: Demographic):
    DEMO[rec.customerId] = rec.dict()
    return {"status": "saved", "record": rec}

@app.get("/health")
def health():
    return {"status": "crud-db-up"}
