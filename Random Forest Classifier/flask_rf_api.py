import numpy as np
import pickle as pkl
from flask import Flask, request, jsonify


app = Flask("rf")

@app.route("/predict",methods=["POST"])
def predict():
    with open("rf.pkl","rb") as model_file:
        model = pkl.load(model_file)
        
    if request.method=="POST":
        try:
            data = request.get_json()
            
            s_length = int(data["s_length"])
            s_width  = int(data["s_width"])
            p_length = int(data["p_length"])
            p_width  = int(data["p_width"])
            
            ip = np.array([[s_length, s_width, p_length, p_width]])
            
            prediction = model.predict(ip)
            
            results = {"result":str(prediction)}
         
        except:
            return jsonify("Please enter a number.")
    return jsonify(results)

app.run(port=8000)


## Load Model


    
    
    