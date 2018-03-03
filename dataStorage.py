import os
import redis
import _json
import requests

url = 'redis://h:pefdc000ffe64e9ee1d5b61c52070f9a98839b0413371070bf7ff0fab173c7231@ec2-34-252-202-201.eu-west-1.compute.amazonaws.com:43329'
r = redis.StrictRedis.from_url(url)

def createPlaces():
    places = {"places":[]}
    r.set("places",places)

def getAllPlaces():
    print(r.get(places))

createPlaces()
getAllPlaces()
