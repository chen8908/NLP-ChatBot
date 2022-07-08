import pickle
import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras_preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Dense, Embedding, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data(filepath,input_shape=20):
    df = pd.read_csv(filepath)
    #標籤及詞彙表
    labels, vocabulary = list(df['label'].unique()),list(df['evaluation'].unique())

    #建造字元級別的特徵
    string = ''
    for word in vocabulary:
        string +=word
    vocabulary = set(string)

    #字典列表
    word_dictionary = {word: i+1 for i,word in enumerate(vocabulary)}
    with open('word_dict.pk','wb') as f:
        pickle.dump(word_dictionary,f)
    inverse_word_dicrionary = {i+1:word for i,word in enumerate(vocabulary)}
    label_dictionary = {label:i for i,label in enumerate(labels)}
    with open('label_dict.pk','wb') as f:
        pickle.dump(label_dictionary,f)
    output_dictionary={i:labels for i , labels in enumerate(labels)}

    vocab_size = len(word_dictionary.keys())#詞彙表大小
    label_size = len(label_dictionary.keys())#標籤類別數量
    #序列填充,input_shape填充,長度不足的按0去填充
    x=[[word_dictionary[word] for word in sent] for sent in df['evaluation']]
    x=pad_sequences(maxlen=input_shape,sequences=x,padding='post',value=0)
    y=[[label_dictionary[sent]] for sent in df['label']]
    y=[np_utils.to_categorical(label,num_classes=label_size) for label in y]
    y=np.array([list(_[0]) for _ in y])

    return x,y,output_dictionary,vocab_size,label_size,inverse_word_dicrionary

#建立深度學習模型，Embedding + LSTM + Softmax.
def create_LSTM(n_units,input_shape,output_dim,filepath):
    x, y, output_dictionary, vocab_size, label_size, inverse_word_dicrionary=load_data(filepath)
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size + 1, output_dim=output_dim,
                        input_length=input_shape, mask_zero=True))
    model.add(LSTM(n_units, input_shape=(x.shape[0], x.shape[1])))
    model.add(Dropout(0.2))
    model.add(Dense(label_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    #    plot_model(model, to_file='./model_lstm.png', show_shapes=True)
    model.summary()

    return model

#模型訓練
def model_train(input_shape,filepath,model_save_path):

    #將資料分為訓練集及測試集，占比為9:1
    #input_shape=100
    x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary =load_data(filepath,input_shape)
    train_x,test_x,train_y,test_y = train_test_split(x,y,train_size=0.1,random_state=42)

    #模型輸入引數，需要自己調整
    n_units = 100
    batch_size = 32
    epochs = 15
    output_dim = 20

    # 模型訓練
    lstm_model = create_LSTM(n_units, input_shape, output_dim, filepath)
    lstm_model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1)

    # 模型儲存
    lstm_model.save(model_save_path)

    N = test_x.shape[0]  # 測試的條數
    predict = []
    label = []
    for start, end in zip(range(0, N, 1), range(1, N+1, 1)):
        sentence = [inverse_word_dictionary[i] for i in test_x[start] if i != 0]
        y_predict = lstm_model.predict(test_x[start:end])
        label_predict = output_dictionary[np.argmax(y_predict[0])]
        label_true = output_dictionary[np.argmax(test_y[start:end])]
        print(''.join(sentence), label_true, label_predict) # 輸出預測結果
        predict.append(label_predict)
        label.append(label_true)

    acc = accuracy_score(predict, label) # 預測準確率
    print('模型在測試集上的準確率為: %s.' % acc)

if __name__ == '__main__':
    filepath = 'C:/Users/sun/PycharmProjects/JD-Chatbot-main/sentiment/corpus.csv'
    input_shape = 180
    model_save_path = 'corpus_model.h5'
    model_train(input_shape, filepath, model_save_path)
