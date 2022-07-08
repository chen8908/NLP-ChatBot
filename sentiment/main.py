
from fastapi import APIRouter, Depends
from sentiment import schemas
from .sentiment import get_sentiment_answer
from ext import access

st_app = APIRouter()


@st_app.post('/get_sentiment', response_model=schemas.SentimentOut)
async def get_sentiment(msg: schemas.SentimentIn, x_token: str = Depends(access)):
    """
    ## 接口二 : 情緒分析\n
    此接口可輸入訊息，並針對接收的訊息情緒分析\n
    目前會回傳四個結果，包含 kears、cnsenti 等分析結果\n
    """
    if x_token == 200:
        return get_sentiment_answer(msg.message)
