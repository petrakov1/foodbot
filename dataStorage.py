import os
import redis
import json
import requests
import ast

url = 'redis://h:pefdc000ffe64e9ee1d5b61c52070f9a98839b0413371070bf7ff0fab173c7231@ec2-34-252-202-201.eu-west-1.compute.amazonaws.com:43329'
r = redis.StrictRedis.from_url(url)

def createPlaces():
    places = {"places":[]}
    r.set("places",places)

def getAllPlaces():
    print(r.get("places"))
    

def addPlace(place):
    json_data = str(r.get("places"))
    json_data = json_data.replace('u"','"')
    places = json.loads(json_data)
    places["places"].append(place)
    print(str(places).encode("ascii"))
    r.set("places",str(places).replace("'",'"'))
    

place = {"id":2,
        "name":"test",
        "price":1,
        "location":"",
        "desc":"@",
        "tags":[{"burger":1}]
        }
createPlaces()
addPlace(place)