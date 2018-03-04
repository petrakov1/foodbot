#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import redis
import json
import requests
import ast

url = 'redis://h:p1d9ba703af8034ed13a18125dc4a79f41840465fe1fb8a4e66eb5d801f0866cc@ec2-52-212-239-249.eu-west-1.compute.amazonaws.com:13169'
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
def addPlaceImage(id,link):
    json_data = r.get("places")
    places = json.loads(json_data)
    for i in range(0,len(places)):
        print(places[i])
        if places[i]['id'] == id:
            places[i]['img'] = link
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

def createUser(user_id,price):
    user = {"tags":{},"price":price,"places":{}}
    r.set("user_"+str(user_id),json.dumps(user))

def changeUserIgnore(user_id,place_id):
    user = r.get("user_"+str(user_id))
    user = json.loads(user)
    if place_id not in user["places"]:
        user["places"][place_id] =  0
    r.set("user_"+str(user_id),json.dumps(user))

def changeUser(user_id,choosedTags,place_id):
    user = r.get("user_"+str(user_id))
    user = json.loads(user)
    userTags = user["tags"]
    for choosedTag in choosedTags:
        if choosedTag not in userTags:
            userTags[choosedTag] =  choosedTags[choosedTag]
        else:
            userTags[choosedTag] += choosedTags[choosedTag]
    
    if place_id not in user["places"]:
        user["places"][place_id] =  1
    
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
