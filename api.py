from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Apart(Resource):
    def get(self):
        data = pd.read_csv('apart.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        isim = request.args['isim']
        kat = request.args['kat']
        odasayısı = request.args['odasayısı']
        m2= request.args['m2']
        req_data = pd.DataFrame({'isim': [isim],
				  'kat': [kat],
                                  'odasayısı': [odasayısı],
				  'm2':[m2]})
        data = pd.read_csv('apart.csv')
        data = data.append(req_data, ignore_index=True)
        data.to_csv('apart.csv', index=False)
        return ({'message': 'Record successfully added.'}, 200)

class Name(Resource):
    def get(self):
        data = pd.read_csv('apart.csv',usecols=[0])
        data = data.to_dict('records')
        return {'data' : data}, 200

api.add_resource(Name, '/apartname')
api.add_resource(Apart, '/aparts')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)

