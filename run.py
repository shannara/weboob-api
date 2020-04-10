from flask import Flask, request
from flask_restx import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_httpauth import HTTPBasicAuth
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)

capabilities = '''
[
    {"id": "1", "name": "audio"},
    {"id": "2", "name": "bands"},
    {"id": "3", "name": "bank"},
    {"id": "4", "name": "bill"},
    {"id": "5", "name": "bugtracker"},
    {"id": "6", "name": "calendar"},
    {"id": "7", "name": "cinema"},
    {"id": "8", "name": "content"},
    {"id": "9", "name": "dating"},
    {"id": "10", "name": "gallery"},
    {"id": "11", "name": "gauge"},
    {"id": "12", "name": "geolocip"},
    {"id": "13", "name": "housing"},
    {"id": "14", "name": "job"},
    {"id": "15", "name": "library"},
    {"id": "16", "name": "lyrics"},
    {"id": "17", "name": "messages"},
    {"id": "18", "name": "parcel"},
    {"id": "19", "name": "paste"},
    {"id": "20", "name": "pricecomparison"},
    {"id": "21", "name": "radio"},
    {"id": "22", "name": "recipe"},
    {"id": "23", "name": "shop"},
    {"id": "25", "name": "torrent"},
    {"id": "24", "name": "subtitle"},
    {"id": "26", "name": "translate"},
    {"id": "27", "name": "travel"},
    {"id": "28", "name": "video"},
    {"id": "29", "name": "weather"}
]
'''

class Capabilities():
    def list(self):
        '''Get list of capabilities'''
        return json.loads(capabilities)

    def get(self, id):
        capDict = self.list()
        for cap in capDict:
            if cap["id"] == id:
                return cap["name"]

cap = Capabilities()

@api.route('/list')
class LIST(Resource):
    #@auth.login_required
    def get(self):
        '''Get list of capabilities'''
        return cap.list()

@api.route('/cap')
class CAP(Resource):
    #@auth.login_required
    def get(self, id, command):
        # Accept both id or fullname of capability
        capability = cap.get(id) if id.isdigit() else id

        process = subprocess.run(['weboob',capability,command,'-f','json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = process.stdout.decode('UTF-8')
        print(stdout)

    def post(self):
        # Accept both id or fullname of capability
        capability = request.json.get('capability')
        command = request.json.get('command')
        args = request.json.get('args')
        # Set args empty
        if args == None:
          args = ''

        print(capability + ' ' + command + ' ' + args)
        process = subprocess.run(['boo'+capability,command,args,'-n','10000','-f','json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = process.stdout.decode('UTF-8')
        return stdout

@api.route('/auth')
class AUTH(Resource):
   def post(self):
       username = request.json.get('username')
       password = request.json.get('password')

       #print(username + ' ' + password)
       return "200"

api.add_resource(LIST, '/list')
api.add_resource(CAP, '/cap')
api.add_resource(AUTH, '/auth')

if __name__ == '__main__':
     app.run(port='5002')
