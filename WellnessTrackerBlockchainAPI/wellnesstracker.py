from flask import Flask
from flask import request
from flask import make_response, jsonify
from datetime import date
import json
import requests
from web3 import Web3

# Blockchain connction
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
address = '0x32612531c85B6092B7381B58De72c4Fe0b8F5Cd5'
abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"},{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_bodytemperature","type":"string"},{"internalType":"int256","name":"_bloodpressure","type":"int256"},{"internalType":"int256","name":"_respiraton","type":"int256"},{"internalType":"int256","name":"_glucose","type":"int256"},{"internalType":"int256","name":"_heartrate","type":"int256"},{"internalType":"int256","name":"_cholesterol","type":"int256"},{"internalType":"int256","name":"_oxygensaturation","type":"int256"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

# contract connection eshtablishment
contract = web3.eth.contract(address=address, abi=abi)
web3.eth.defaultAccount = web3.eth.accounts[0]

app = Flask(__name__)


@app.route("/wtb/add", methods=["GET"])
def datainsertion():
    try:
        req = request.json
        print(req)
        bodytemperature = req['bodytemperature']
        bloodpressure = req['bloodpressure']
        respiration = req['respiration']
        glucose = req['glucose']
        heartrate = req['heartrate']
        cholesterol = req["cholesterol"]
        oxygensaturation = req["oxygensaturation"]
        records = contract.functions.set(bodytemperature, int(bloodpressure), int(respiration), int(glucose), int(heartrate), int(cholesterol), int(oxygensaturation)).transact()
        return "Data Inserted"
    except:
        return "something went wrong"


@app.route("/wtb/view", methods=["GET"])
def retrievedata():
    try:
        records = contract.functions.get().call()
        stat = {}
        stat['bodytemperature'] = records[0]
        stat['bloodpressure'] = records[1]
        stat['respiration'] = records[2]
        stat['glucose'] = records[3]
        stat['heartrate'] = records[4]
        stat['cholesterol'] = records[5]
        stat['oxygensaturation'] = records[6]
        return jsonify({"data": stat})
    except:
        return "something went wrong"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)