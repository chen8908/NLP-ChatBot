
<p align="center">
  <a href="#"><img src="https://i.imgur.com/QRSDtge.png" alt="FastAPI_Dialogflow" width="450"></a>
</p>
<p align="center">
    <em>使用最火紅的 FastAPI框架 搭建 Dialogflow自然語言對話機器人</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/FastAPI-v0.78.0-brightgreen" alt="FastAPI">
</a>
<a href="#" target="_blank">
    <img src="https://img.shields.io/badge/Dialogflow-ES-brightgreen" alt="Coverage">
</a>
<a href="#" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

## FastAPI 串接 Dialogflow 智能客服應用

>  Dialogflow 自然語言對話的人機互動技術，利用 FastAPI 串接接口，可實現針對用戶信息加以分析 (如:情緒分析等)

首先，要先於 Dialogflow 中設定 Intents、Entities、Training phrases，並於 GCP 取得專案金鑰，再利用 FastAPI 搭建接口，
實現取得用戶信息並返回結果。而我們搭建了三個接口

* /df/get_df : 返回 Dialogflow 回傳值
* /st/sentiment : 情緒分析
* /df_st/get_df_sentiment : 返回 Dialogflow 與情緒分析之結果


## Requirements:

* Python 3.6+
* 已建置好 [Dialogflow](https://cloud.google.com/dialogflow/es/docs) 設定
* 已完成 [身分驗證](https://cloud.google.com/dialogflow/es/docs/quick/setup) 並取得專案金鑰

## Usage:

### 前動作

1. 將取得的金鑰 (JSON) 放置專案目錄中


2. 修改 df 目錄中的 `__init__.py` 與 `results.py` 的專案資訊

   * `os.environ["GOOGLE_APPLICATION_CREDENTIALS"]` : 專案金鑰路徑

   * `DIALOGFLOW_PROJECT_ID` : 專案 ID

   * `DIALOGFLOW_LANGUAGE_CODE` : 語系
***
### 接口一 : 返回 Dialogflow 回傳值 ( /df/get_df )
可透過此接口來獲取用戶信息，並返回 DF 回應
1. InModel Request - POST 請求 :

   **Parameters 參數**
   * Request Header
     * `x-token` : 密鑰
   * Request Body
     *  `message` : 詢問文字

   ```python
   # df/schemas.py
   
   class DFIn(BaseModel):
       message: str 
   ```
   
2. OutModel Response :

   **Parameters 參數**
   * Response Body
     * `intent` : 意圖
     * `confidence` : 信心值
     * `fulfillment` : 回應

   ```python
   # df/schemas.py
   
   class DFOut(BaseModel):
    intent: str
    confidence: float
    fulfillment: str
    mood: Optional[float] = None
   ```
***
### 接口二 : 情緒分析 ( /st/sentiment )
此接口可輸入訊息，並針對接收的訊息情緒分析

目前會回傳四個結果，包含 kears、cnsenti 等分析結果
1. InModel Request - POST 請求 :

   **Parameters 參數**
   * Request Header
     * `x-token` : 密鑰
   * Request Body
     *  `message` : 詢問文字

   ```python
   # sentiment/schemas.py
   
   class SentimentIn(BaseModel):
       message: str 
   ```
   
2. OutModel Response :

   **Parameters 參數**
   * Response Body
        * `sentiment_keras_model` : 情緒分析(keras模型)
        * `sentiment_cnsenti` : 情緒分析(cnsenti)
        * `sentiment_cnsenti_calculate` : 情緒分析(cnsenti_calculate)
        * `sentiment_emotion` : 情緒分析(emotion)
   ```python
   # sentiment/schemas.py
   
   class SentimentOut(BaseModel):
    sentiment_keras_model: str
    sentiment_cnsenti: Dict[str, float]
    sentiment_cnsenti_calculate: Dict[str, float]
    sentiment_emotion: Dict[str, int]
   ```
***
### 接口三 : 返回 Dialogflow 與情緒分析之結果 ( /st/sentiment )
此接口結合接口一與接口二

同時回傳 Dialogflow 回應與情緒分析之結果
1. InModel Request - POST 請求 :

   **Parameters 參數**
   * Request Header
     * `x-token` : 密鑰
   * Request Body
     *  `message` : 詢問文字

   ```python
   # df_sentiment/schemas.py
   
   class DF_STIn(BaseModel):
       message: str 
   ```
   
2. OutModel Response :

   **Parameters 參數**
   * Response Body
        * `intent` : 意圖
        * `confidence` : 信心值
        * `fulfillment` : 回應
        * `sentiment_keras_model` : 情緒分析(keras模型)
        * `sentiment_cnsenti` : 情緒分析(cnsenti)
        * `sentiment_cnsenti_calculate` : 情緒分析(cnsenti_calculate)
        * `sentiment_emotion` : 情緒分析(emotion)
   ```python
   # df_sentiment/schemas.py
   
   class DF_STOut(BaseModel):
    intent: str
    confidence: float
    fulfillment: str
    sentiment_keras_model: str
    sentiment_cnsenti: Dict[str, float]
    sentiment_cnsenti_calculate: Dict[str, float]
    sentiment_emotion: Dict[str, int]
   ```
## Test:

於終端機下開啟專案目錄

並輸入以下指令來測試專案
```
pytest
```
