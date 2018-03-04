#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _json
import math

def valueByTag(place,arrPerson):
    value = 0

    for tag in arrPerson:

        if (tag in place):
            value += place[tag]*arrPerson[tag]

    return (value)

def sortByValue(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j][1] > arr[j - 1][1]:
                test1 = arr[j][0]
                test2 = arr[j][1]
                test3 = arr[j][2]
                arr[j][0] = arr[j - 1][0]
                arr[j][1] = arr[j - 1][1]
                arr[j][2] = arr[j - 1][2]
                arr[j - 1][0] = test1
                arr[j - 1][1] = test2
                arr[j - 1][2] = test3

def getTopPlaces (json_Plase, json_Person,clientPoint):

    arrPerson = json_Person["tags"]
    personPrise = json_Person["price"]

    arrPlaces = []

    for place in json_Plase:
        distance = distance_([place["location"]["lon"], place["location"]["lat"]], clientPoint)
        if (distance < 3):
            arrPlaces.append([place["id"], valueByTag(place["tags"], arrPerson), distance])

    print (arrPlaces)
    sortByValue(arrPlaces)

    if (arrPlaces.__len__()==0): arrPlaces.append([0,0,0])

    if (arrPlaces[0][1] != 0):
        for i in range(1, arrPlaces.__len__()):
            arrPlaces[i][1] = arrPlaces[i][1] / float(arrPlaces[0][1])
        arrPlaces[0][1] = 1

    arrValueOfPrices = []

    for place in json_Plase:
        arrValueOfPrices.append([place["id"], place["price"]])

    for i in range(0, arrValueOfPrices.__len__()):
        arrValueOfPrices[i][1] = (personPrise - arrValueOfPrices[i][1]) / 2.0

    for i in range(0, arrPlaces.__len__()):
        for j in range(0, arrValueOfPrices.__len__()):
            if (arrPlaces[i][0]==arrValueOfPrices[j][0]):
                arrPlaces[i][1] = 2 * arrPlaces[i][1] + arrValueOfPrices[j][1]

    sortByValue(arrPlaces)

    while arrPlaces.__len__()>5:
        arrPlaces.pop()
    print (arrPlaces)
    return (arrPlaces)

def distance_(point1, point2):
    R = 6371
    dLat = math.radians(point2[0] - point1[0])
    dLon = math.radians(point2[1] - point1[1])
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(point1[0])) * math.cos(math.radians(point2[0])) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d

#jsonPlaces = [{"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": {"lat":59.9317145,"lon":30.3457811}, "id": 1, "desc": "@"},
#              {"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": {"lat":59.9317405,"lon":30.3457811}, "id": 2, "desc": "@"},
#              {"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": {"lat":59.9317145,"lon":30.3456811}, "id": 3, "desc": "@"},
#              {"name": "Pizaa", "tags": {"pasta": 1}, "price": 1, "location": {"lat":59.9317145,"lon":30.3457854}, "id": 4, "desc": ""},
#              {"name": "a", "tags": {"pasta": 1, "fri": 1}, "price": 2, "location": {"lat":59.9317405,"lon":30.3457811}, "id": 5, "desc": ""},
#              {"name": "Pizaa", "tags": {"fri": 2}, "price": 1, "location": {"lat":59.9317405,"lon":30.3457811}, "id": 6, "desc": ""},
#              {"name": "a", "tags": {"burger": 1, "fri": 1}, "price": 2, "location": {"lat":59.9317405,"lon":30.3457811}, "id": 7, "desc": ""}]
#jsonPerson = {"tags": {"burger":1,"pizza":2}, "price": 1, "places": 0}

#clientPoint = (59.9368993,30.3154044)
#getTopPlaces(jsonPlaces,jsonPerson,clientPoint)
