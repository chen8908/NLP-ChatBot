
from fastapi import APIRouter, Depends
from df import schemas
from df.result import get_df_answer
from ext import access

df_app = APIRouter()


@df_app.post('/get_df', response_model=schemas.DFOut)
async def get_df(msg: schemas.DFIn, x_token: str = Depends(access)):
    """
    ## 接口一 : 返回 Dialogflow 回傳值\n
    可透過此接口來獲取用戶信息，並返回 DF 回應\n
    使用接口前，請完成前動作設定方可使用 (詳細參閱 [README.md](https://github.com/jds-3t3/FastAPI_with_Dialogflow))\n
    """
    if x_token == 200:
        return get_df_answer(msg.message)
