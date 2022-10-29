from flask import Flask, request
from app.mapper import mapInput, mapOutput
from app.neural_network import predict
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    input = []
    inputAsMatrix = {}
    
    for i in range(0, 3):
        if i not in inputAsMatrix:
            inputAsMatrix[i] = {}
        
        for j in range(0, 3):
            value = request.args.get(f"input[{i}][{j}]", 'b')
            input.append(mapInput(value))
            inputAsMatrix[i][j] = value
            
    output = predict(np.array([
        input,
    ]))
    
    return {
        'result': mapOutput(output['rounded']),
        'output': output,
        'input': inputAsMatrix
    }
