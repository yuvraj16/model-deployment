# Simple Introduction to Flask API
# Exposing SUM of two numbers as API

from flask import Flask, request, jsonify

app = Flask("add_number")

@app.route('/')
def add():
    a= request.args.get("a")
    b= request.args.get("b")
    return str(int(a)+int(b))

#"Can give port as we want, default will be 5000"
#app.run(port=7000)

## Once this python is run, a link is generated, 
## we can pass the values of a,b in link
## eg: http://127.0.0.1:7000/?a=10&b=20

## or use post method given below to post the a and b

#
# When Using POST Method to supply data

@app.route('/add_two',methods=['POST'])
def add_two():
    if request.method == 'POST':
        try:
            data = request.get_json()
            a = int(data["a"])
            b = int(data["b"])
            
            results = {"result":str(int(a)+int(b))}
         
        except:
            return jsonify("Please enter a number.")
    return jsonify(results)
# "Can give custom port number as we want, default will be 5000"


@app.route('/health')
def health():
    return "All Ok"


app.run(port=7000)