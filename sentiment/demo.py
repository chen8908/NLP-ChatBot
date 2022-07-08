from sentiment import *
from sentiment.sentiment import get_sentiment_with_keras_model,get_sentiment_with_cnsenti,get_sentiment_with_emotion

if __name__ == '__main__':
    while True:
        msg = input('請輸入問題(enter離開)')
        if msg == "":
            break
        else:
            sentiment_cnsenti = get_sentiment_with_cnsenti(msg)
            print(str(sentiment_cnsenti))
            Emotion= get_sentiment_with_emotion(msg)
            print(str(Emotion))
            keras_model = get_sentiment_with_keras_model(msg)
            print(str(keras_model))