
from fastapi import FastAPI
import uvicorn
from df import df_app
from sentiment import st_app
from df_sentiment import df_st_app

app = FastAPI()

app.include_router(df_app, prefix='/df', tags=['Dialogflow'])
app.include_router(st_app, prefix="/st", tags=["Sentiment"])
app.include_router(df_st_app, prefix='/df_st', tags=['Dialogflow + Sentiment'])

# 啟動命令: uvicorn run:app --reload

if __name__ == "__main__":
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
