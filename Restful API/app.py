from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi object flask
app= Flask(__name__)

#inisiasi object flask_restful
api= Api(app)

#inisasi object flask_cors
CORS(app)

#inisiasi variabel bertipe dictionary
item={} # ini variabel global, dictionary disini= json

#class resource
class iniResource(Resource):
    #metode get dan post
    def get(self):
        
        return item
        
        
        
    def post(self):
        harga= request.form["harga"]
        barang= request.form["barang"]
        item["harga"]= int(harga)
        item["barang"]= barang
        response={"msg": "Terima kasih sudah menjual barang"}
        return response
        

#setup resourcenya
api.add_resource(iniResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5505)


