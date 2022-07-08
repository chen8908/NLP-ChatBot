from fastapi import HTTPException
from cnsenti import Sentiment
from cnsenti import Emotion
import pickle
from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
import numpy as np

def get_sentiment_with_keras_model(msg):
    # 匯入字典
    with open('./sentiment/word_dict.pk', 'rb') as f:
        word_dictionary = pickle.load(f)
    with open('./sentiment/label_dict.pk', 'rb') as f:
        output_dictionary = pickle.load(f)
    try:
        # 資料預處理
        input_shape = 180
        x = [[word_dictionary[word] for word in msg]]
        x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)
        model_save_path = './sentiment/corpus_model.h5'
        lstm_model = load_model(model_save_path)
        y_predict = lstm_model.predict(x)
        label_dict = {v: k for k, v in output_dictionary.items()}
        result = label_dict[np.argmax(y_predict)]

    except KeyError:
        raise HTTPException(status_code=400, detail='KeyError')

    return result

def get_sentiment_with_cnsenti(msg):
    senti= Sentiment(merge=True,
                     encoding='utf-8')
    result = senti.sentiment_count(msg)
    return result

def get_sentiment_with_emotion(msg):
    result = Emotion().emotion_count(msg)
    return result

def get_sentiment_answer(msg):
    result = {
        'sentiment_keras_model': get_sentiment_with_keras_model(msg),
        'sentiment_cnsenti': get_sentiment_with_cnsenti(msg),
        'sentiment_emotion': get_sentiment_with_emotion(msg)
    }
    return result