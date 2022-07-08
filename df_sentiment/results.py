
from df.result import get_df_answer
from sentiment.sentiment import get_sentiment_answer

def get_df_st_answer(msg):
    df_answer = get_df_answer(msg)
    st_answer = get_sentiment_answer(msg)
    result = dict(df_answer, **st_answer)  # dict合併

    return result
