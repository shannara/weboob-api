from flask import Flask, request
from flask_restplus import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from flask_httpauth import HTTPBasicAuth
import subprocess
from modules.capabilities import Capabilities

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)
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
