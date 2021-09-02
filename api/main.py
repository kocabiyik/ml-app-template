from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.on_event("startup")
def startup():
    print("App is starting")


class PredictRequest(BaseModel):
    review: str


class PredictResponse(BaseModel):
    id: int
    sentiment: float


@app.get("/health", response_model=str)
async def get_health():
    """
    Health check
    """
    return "healthy"


@app.post("/api/v1.0/predict", response_model=PredictResponse)
async def predict_sentiment(request_payload: PredictRequest):
    """
    Predicts sentiment of a movie review.
    """
    pass
