
from flask import Flask , jsonify , request , make_response
from flask_cors import CORS
from flask_restful import Api, Resource
import main


app = Flask(__name__)
api = Api(CORS(app))



#CORS(app)

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}
    
    def post(self):
          some_json = request.get_json()   
          return {'about': some_json } , 201
      
api.add_resource(HelloWorld,'/')        

#@app.route('/' , methods=['GET','POST'])
#def index():
#    if(request.method == 'POST'):
#        some_json = request.get_json()
#        print(type(some_json))
#        #print(main.Print())
#        #result = jsonify(main.Print())
#        
#        return make_response(jsonify({"Your result":main.Print()}),201)
#    else:
#        return jsonify({"About":"Hello World"})
    

if __name__ == '__main__' :
    app.run(debug = True)
    


