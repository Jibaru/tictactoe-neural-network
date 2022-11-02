from flask import Flask, jsonify, make_response, request
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
    response = make_response(jsonify({
        'result': mapOutput(output['rounded']),
        'output': output,
        'input': inputAsMatrix
    }))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
