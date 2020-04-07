import json

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
