#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _json
import math

def valueByTag(place,arrPerson):
    value = 0

    for tag in arrPerson:

        if (tag in place):
            value += place[tag]*arrPerson[tag]
            #print(place[teg])
    return (value)

def sortByValue(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j][1] > arr[j - 1][1]:
                test1 = arr[j][0]
                test2 = arr[j][1]
                arr[j][0] = arr[j - 1][0]
                arr[j][1] = arr[j - 1][1]
                arr[j - 1][0] = test1
                arr[j - 1][1] = test2


#def addPlaceToTop5Places(place1,max):
#    if arrTop5Places.__len__() > 5:
#        arrTop5Places[0].pop()
#        arrTop5Places[1].pop()
#    arrTop5Places[0].append(place1)
#    arrTop5Places[1].append(max)
#    sortByValue(arrTop5Places)
#    return(arrTop5Places[1][arrTop5Places[0].__len__()-1])


#arrPlaces = [{"a":30,"b":4,"d":10},{"a":1,"b":2,"c":3},{"a":3,"b":4,"c":5},]

#DATA SET
#arrPerson = {"burger":1,"pizza":2,"c":3,"d":4}
#personPrise = 2

def getTopPlaces (json_Plase, json_Person):

    arrPerson = json_Person["tags"]
    personPrise = json_Person["price"]

    arrPlaces = []

    #for place in json_Plase:
    #    print (place["location"]["lat"])
    #    distance = distance_([place["location"]["lat"],place["location"]["lon"]],clientPoint)
    #    print (arrPlaces[place["id"]])
    #    arrPlaces[place["id"]].apend(distance)

    for place in json_Plase:
        print (place["location"])
        print ("Test")
        print (distance_((place["location"]["lat"],place["location"]["lon"]),clientPoint))
        arrPlaces.append([place["id"], valueByTag(place["tags"],arrPerson), distance_((place["location"]["lat"],place["location"]["lon"]),clientPoint)])

    #print (arrPlaces)
    sortByValue(arrPlaces)
    #print ("After sort")
    #print (arrPlaces)
    if (arrPlaces[0][1] != 0):
        for i in range(1, arrPlaces.__len__()):
            arrPlaces[i][1] = arrPlaces[i][1] / float(arrPlaces[0][1])
        arrPlaces[0][1] = 1

    #print ("After 0-1")
    #print (arrPlaces)

    #print("test")

    # for tegs
    # max5 = 0
    # arrTop5Places = [[],[]]

    # for place in arrPlaces:
    #    if (valueByTag(place,arrPerson) > max5)|(arrTop5Places.__len__() <= 5):
    #        max5 = addPlaceToTop5Places(place, valueByTag(place,arrPerson))

    # for i in range(1,arrTop5Places[1].__len__()):
    #    arrTop5Places[1][i] = arrTop5Places[1][i]/float(arrTop5Places[1][0])
    # arrTop5Places[1][0] = 1



    # print (arrTop5Places)

    # for prices

    # arrValueOfPrices = [[1,2,3],[2,1,3]]
    arrValueOfPrices = []

    for place in json_Plase:
        arrValueOfPrices.append([place["id"], place["price"]])
    #print (arrValueOfPrices)

    for i in range(0, arrValueOfPrices.__len__()):
        arrValueOfPrices[i][1] = (personPrise - arrValueOfPrices[i][1]) / 2.0

    sortByValue(arrValueOfPrices)
    #print ("Before connection")
    #print (arrValueOfPrices)
    #print (arrPlaces)

    for i in range(0, arrPlaces.__len__()):
        for j in range(0, arrValueOfPrices.__len__()):
            if (arrPlaces[i][0]==arrValueOfPrices[j][0]):
                arrPlaces[i][1] = 2 * arrPlaces[i][1] + arrValueOfPrices[j][1]

    #print ("Itog")
    sortByValue(arrPlaces)
    #print (arrPlaces)


    return (arrPlaces)

def distance_(point1, point2):
    R = 6371
    dLat = math.radians(point2[0] - point1[0])
    dLon = math.radians(point2[1] - point1[1])
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(point1[0])) * math.cos(math.radians(point2[0])) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


#json = [{"name": "test1", "tags": {"burger": 1, "pizza": 2}, "price": 1, "location": "", "id": 1, "desc": "@"},
#                      {"name": "test2", "tags": {"pizza": 1}, "price": 2, "location": "", "id": 2, "desc": "@"},
#            {"name": "v", "tags": {"pasta": 2, "burger": 1, "pizza": 1}, "price": 3, "location": {}, "id": 6, "desc": ""}]

jsonPlaces = [{"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": {"lat": 30.352859,"lon":59.9318357}, "id": 1, "desc": "@"}, {"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": "", "id": 2, "desc": "@"}, {"name": "\u0422\u0435\u0441\u0442", "tags": {"burger": 1}, "price": 1, "location": "", "id": 3, "desc": "@"}, {"name": "Pizaa", "tags": {"pasta": 1}, "price": 1, "location": {}, "id": 4, "desc": ""}, {"name": "a", "tags": {"pasta": 1, "fri": 1}, "price": 2, "location": {}, "id": 5, "desc": ""}, {"name": "Pizaa", "tags": {"fri": 2}, "price": 1, "location": {}, "id": 6, "desc": ""}, {"name": "a", "tags": {"burger": 1, "fri": 1}, "price": 2, "location": {}, "id": 7, "desc": ""}]
jsonPerson = {"tags": {"burger":1,"pizza":2}, "price": 1, "places": 0}

clientPoint = (30.352856,59.9318351)
getTopPlaces(jsonPlaces,jsonPerson)