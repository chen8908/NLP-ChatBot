
from pydantic import BaseModel

class DFIn(BaseModel):
    message: str

class DFOut(BaseModel):
    intent: str
    confidence: float
    fulfillment: str
