
from fastapi import APIRouter, Depends
from df_sentiment import schemas, results
from ext import access

df_st_app = APIRouter()

@df_st_app.post('/get_df_sentiment', response_model=schemas.DF_STOut)
def get_df_sentiment(msg: schemas.DF_STIn, x_token: str = Depends(access)):
    """
    ## 接口三 : 返回 Dialogflow 與情緒分析之結果\n
    此接口結合接口一與接口二\n
    同時回傳 Dialogflow 回應與情緒分析之結果\n
    """
    if x_token == 200:
        return results.get_df_st_answer(msg.message)
