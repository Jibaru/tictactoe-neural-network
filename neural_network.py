import pandas as pd
from keras.models import Sequential, Model,model_from_json
from keras.layers.core import Dense

def predict(X):
    jsonFile = open("data/model.json",'r')
    jsonModel = jsonFile.read()
    jsonFile.close()

    model = model_from_json(jsonModel)
    model.load_weights("data/weights.h5")
    
    model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics = ['accuracy']
    )
    result = model.predict(X)
    rounded = result.round()
    
    return {
        'original': result.tolist()[0][0],
        'rounded': rounded.tolist()[0][0]
    }