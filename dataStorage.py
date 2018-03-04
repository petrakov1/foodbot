#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import redis
import json
import requests
import ast

url = 'redis://h:pefdc000ffe64e9ee1d5b61c52070f9a98839b0413371070bf7ff0fab173c7231@ec2-34-252-202-201.eu-west-1.compute.amazonaws.com:43329'
r = redis.StrictRedis.from_url(url)

def createPlaces():
    places = []
    r.set("places",json.dumps(places))
    r.set("last_id",0)
    

def getAllPlaces():
    return r.get("places")

def getPlace(id):
    json_data = r.get("places")
    places = json.loads(json_data)
    for place in places:
        if (place['id']==id):
            return place
def editPlace(id):
    json_data = r.get("places")
    places = json.loads(json_data)
    for i in range(0,len(places)):
        print(places[i])
        if places[i]['id'] == id:
            places[i]['id'] = 6
            break
            # print(place)
    r.set("places",json.dumps(places))

def addPlace(name,price,location,address,desc,tags):
    id = int(r.get("last_id"))+1
    r.set("last_id",id)
    place = {"id":id,
        "name":name,
        "price":price,
        "location":location,
        "address": address,
        "desc":desc,
        "tags":tags
        }
    json_data = r.get("places")
    places = json.loads(json_data)
    places.append(place)
    r.set("places",json.dumps(places))

def createUser(user_id):
    user = {"tags":{},"price":1,"places":0}
    r.set("user_"+str(user_id),json.dumps(user))

def changeUser(user_id,choosedTags,priceDelta):
    user = r.get("user_"+str(user_id))
    user = json.loads(user)
    # user["price"] += priceDelta
    userTags = user["tags"]
    for choosedTag in choosedTags:
        if choosedTag not in userTags:
            userTags[choosedTag] =  choosedTags[choosedTag]
        else:
            userTags[choosedTag] += choosedTags[choosedTag]

    user["tags"] = userTags    
    r.set("user_"+str(user_id),json.dumps(user))

def getUser(user_id):
    return r.get("user_"+str(user_id))

def getNPlaces(n):
    json_data = r.get("places")
    places = json.loads(json_data)
    rezPlace = []
    for i in range(0,n):
        rezPlace.append(places[i])
    return rezPlace
