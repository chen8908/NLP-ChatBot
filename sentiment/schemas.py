from typing import Dict
from pydantic import BaseModel

class SentimentIn(BaseModel):
    message:str #詢問文字

class SentimentOut(BaseModel):
    sentiment_keras_model:str
    sentiment_cnsenti:Dict[str,float]
    sentiment_emotion:Dict[str,int]
