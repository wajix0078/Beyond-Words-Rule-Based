# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask , jsonify , request , make_response
from flask_cors import CORS
import main



app = Flask(__name__)
CORS(app)

@app.route('/' , methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        print(type(some_json))
        #print(main.Print())
        #result = jsonify(main.Print())
        
        return make_response(jsonify({"Your result":main.Print()}),201)
    else:
        return jsonify({"About":"Hello World"})
    

if __name__ == '__main__' :
    app.run(debug = True)
    


