import os

from flask import Flask
from flask_restful import Api, reqparse

from resources.random_json import RandomJSON
from resources.random_csv import RandomCSV


app = Flask(__name__)
app.config['PROPOGATE_EXCEPTIONS'] = True
api = Api(app)

@api.representation('text/csv')
def output_csv(data, code, headers=None):
    pass


# Random sink addresses
api.add_resource(RandomJSON, '/random/json/<int:amount>')
api.add_resource(RandomCSV, '/random/csv/<int:amount>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
