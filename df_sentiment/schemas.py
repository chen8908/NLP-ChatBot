
from typing import Dict
from pydantic import BaseModel

class DF_STIn(BaseModel):
    message: str

class DF_STOut(BaseModel):
    intent: str
    confidence: float
    fulfillment: str
    sentiment_keras_model: str
    sentiment_cnsenti: Dict[str, float]
    sentiment_emotion: Dict[str, int]
