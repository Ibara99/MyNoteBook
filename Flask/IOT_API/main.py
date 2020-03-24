# Credit : https://pythonforundergradengineers.com/flask-iot-server-validation-time-stamps.html
from flask import Flask, render_template
from config import API_KEY, MAC_ADDRESS
from datetime import datetime

import requests
app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('https://api.thingspeak.com/channels/254616/fields/1/last.txt')
    temp_c_in = r.text
    temp_f = str(round(((9.0 / 5.0) * float(temp_c_in) + 32), 1)) + ' F'
    return render_template("index.html", temp=temp_f)

@app.route("/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>", methods=['GET'])
def update(api_key, mac, field, data):
    return render_template("update.html", data=data)

@app.route("/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>", methods=['GET'])
def write_data_point(api_key, mac, field, data):
    if (api_key == API_KEY and mac == MAC_ADDRESS):
        d = datetime().now()
        d = d.strftime("%d-%b-%Y %H:%M:%S")
        return render_template("showrecent.html", data=data, time_stamp=d)

    else:
        return render_template("403.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #app.run(host='localhost')
