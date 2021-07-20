from django.http import HttpResponse

import tensorflow as tf
from django.shortcuts import render
from keras.models import load_model
from transformers import BertTokenizer
import numpy as np

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
data = r'C:\Users\ASUS\Desktop\SentimentBertAnalyser\SentimentBertAnalyser\sentiment_model'
model = tf.keras.models.load_model(data)


def prep_data(text):
    # tokenize to get input IDs and attention mask tensors
    tokens = tokenizer.encode_plus(text, max_length=256,
                                   truncation=True, padding='max_length',
                                   add_special_tokens=True, return_token_type_ids=False,
                                   return_tensors='tf')
    # tokenizer returns int32 tensors, we need to return float64, so we use tf.cast
    return {'input_ids': tf.cast(tokens['input_ids'], tf.float64),
            'attention_mask': tf.cast(tokens['attention_mask'], tf.float64)}


from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def result(request):
    var1 = request.GET['Phrases']
    in_tensor = prep_data(var1)
    probs = model.predict(in_tensor)[0]
    print(probs)
    answer = np.argmax(probs)

    return render(request, 'result.html', {'answer': answer})
