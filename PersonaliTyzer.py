from flask import Flask
import requests
import json
import math
from flask import request
app = Flask(__name__)

@app.route('/PersonaliTyzer', methods=['POST'])
def HandleCall():
    print(request.data)
    jsonRequest = json.loads(request.data)
    print('parsed Json')
    return str(Analyze(jsonRequest))
    

def Analyze(body):
    text = body['text']
    
    print(text)

    vector = body['vector']
    username = '9fcf0840-1315-4b0b-a448-8cf5b6ceb510'
    password = 'SBPqWCzEcpTK'
    url = 'https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2016-10-20'

    try:
        response = requests.post(url, headers={'Content-Type': 'text/plain;charset=utf-8'}, auth=(username, password), data=text)
        personality = json.loads(response.content)['personality']
        needs = json.loads(response.content)['needs']
    except Exception as e: 
        print (str(e))
        print type(e)
        return 0

    synthPers = {}

    for p in personality:
        synthPers[p['name']] = p['percentile']
    for n in needs:
        synthPers[n['name']] = n['percentile']

    for key in synthPers:
        print(key + ': ' + str(synthPers[key]))

    return dist(vector, synthPers)
    

def dist(dict1, dict2):
    distance = 0

    for key in dict1:
        distance += math.pow(float(dict1[key]) - float(dict2[key]), 4)

    return math.pow(distance, .5)
    

    
