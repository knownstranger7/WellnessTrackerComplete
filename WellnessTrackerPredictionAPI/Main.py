from chd import chdprediction
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask("Heart Disease Predition")
CORS(app, support_credentials=True)



@app.route("/")
@cross_origin(support_credentials=True)
def home():
    return "welcome to prediction model"
    
@app.route("/chdpredicton")
@cross_origin(support_credentials=True)
def predictingchd():
    chdresponse = {}
    heartrate = request.args.get('heartrate')
    bloodpressure = request.args.get('bp')
    cholesterol = request.args.get('chol')
    chdrisk = chdprediction().predict(([[int(heartrate), int(bloodpressure), int(cholesterol)]]))
    if chdrisk == 0:
        chdresponse['chd'] = "Negative"
    else:
        chdresponse['chd'] = "Positive"
    return jsonify(chdresponse)


app.run(port=8000)
