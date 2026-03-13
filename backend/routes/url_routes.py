from fastapi import APIRouter
from analyzers.url_analyzer import analyze_url

router = APIRouter()

@router.post("/analyze-url")
def analyze_url_endpoint(data: dict):

    url = data.get("url")

    if not url:
        return {"error": "URL is required"}

    result = analyze_url(url)

    return result