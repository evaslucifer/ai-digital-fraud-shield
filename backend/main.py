from fastapi import FastAPI
from routes.url_routes import router as url_router

app = FastAPI(title="AI Digital Fraud Shield")

# Register API routes
app.include_router(url_router)

@app.get("/")
def home():
    return {"message": "AI Fraud Detection API Running"}