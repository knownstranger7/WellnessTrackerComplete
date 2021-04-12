from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
from chd import chdprediction
import random

app = Flask(__name__)
api = Api(app)


def MedRecN():
    MedRecN = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(80, 120),
        "Respiration": random.randint(12, 16),
        "Glucose": random.randint(72, 140),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(95, 100),
    }
    return MedRecN


def Diabetes():
    Diabetes = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(80, 120),
        "Respiration": random.randint(12, 16),
        "Glucose": random.randint(200, 350),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(95, 100)

    }
    return Diabetes


def Prediabetes():
    Prediabetes = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(90, 120),
        "Respiration": random.randint(12, 16),
        "Glucose": random.randint(140, 199),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(95, 100)

    }
    return Prediabetes


def Bronchiectasis():
    Bronchiectasis = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(90, 120),
        "Respiration": random.randint(40, 60),
        "Glucose": random.randint(72, 140),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(95, 100),
    }
    return Bronchiectasis


def CongenitalHeartDefect():
    CongenitalHeartDefect = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(90, 120),
        "Respiration": random.randint(12, 16),
        "Glucose": random.randint(72, 140),
        "Heart Rate": random.randint(45, 60),
        "Cholesterol": random.randint(200, 270),
        "Oxygen Saturation": random.randint(95, 100),
    }
    return CongenitalHeartDefect


def Hypoxemia():
    Hypoxemia = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(90, 120),
        "Respiration": random.randint(12, 16),
        "Glucose": random.randint(72, 140),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(50, 96),
    }
    return Hypoxemia


def AcuteAsthma():
    AcuteAsthma = {
        "Steps": random.randint(4000, 10000),
        "Body Temperature": (round(random.uniform(35.5, 37.5), 1)),
        "Blood Pressure": random.randint(90, 120),
        "Respiration": random.randint(20, 30),
        "Glucose": random.randint(72, 140),
        "Heart Rate": random.randint(60, 100),
        "Cholesterol": random.randint(125, 200),
        "Oxygen Saturation": random.randint(92, 95),
    }
    return AcuteAsthma


class MedicalData(Resource):
    def get(self, state):
        diseases = {"A": AcuteAsthma(), 'B': Bronchiectasis(), 'C': CongenitalHeartDefect(
        ), 'D': Diabetes(), 'H': Hypoxemia(), 'N': MedRecN(), 'P': Prediabetes()}
        return diseases[state]


api.add_resource(MedicalData, '/medidata/<string:state>')

   
@app.route("/chdprediction")
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

if __name__ == "__main__":
    app.run()
