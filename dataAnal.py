import _json

def valueByTag(place,arrPerson):
    value = 0

    for tag in arrPerson:

        if (tag in place):
            value += place[tag]*arrPerson[tag]
            #print(place[teg])
    return (value)

def sortByValue(arr):
    max = 0
    for i in range(len(arr)/2):
        for j in range(len(arr)/2 - 1, i, -1):
            if arr[j][1] > arr[j - 1][1]:
                test1 = arr[j][0]
                test2 = arr[j][0]
                arr[j][0] = arr[j - 1][0]
                arr[j][0] = arr[j - 1][0]
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
arrPerson = {"burger":1,"pizza":2,"c":3,"d":4}
personPrise = 2

def getTopPlaces (json):

    # json = {"places":[{"name": "test1", "tags": {"burger": 1, "pizza": 2}, "price": 1, "location": "", "id": 1, "desc": "@"},
    #                  {"name": "test2", "tags": {"pizza": 1}, "price": 2, "location": "", "id": 2, "desc": "@"}]}

    arrPlaces = []
    for place in json["places"]:
        arrPlaces.append([place["id"], valueByTag(place["tags"], arrPerson)])

    print (arrPlaces)
    sortByValue(arrPlaces)
    print ("After sort")
    print (arrPlaces)
    for i in range(1, arrPlaces.__len__() / 2 + 1):
        arrPlaces[i][1] = arrPlaces[i][1] / float(arrPlaces[0][1])
    arrPlaces[0][1] = 1
    print ("After 0-1")
    print (arrPlaces)

    print("test")

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

    for place in json["places"]:
        arrValueOfPrices.append([place["id"], place["price"]])
    print (arrValueOfPrices)

    for i in range(0, arrValueOfPrices.__len__() / 2 + 1):
        arrValueOfPrices[i][1] = (arrValueOfPrices[i][1] - personPrise) / 2.0

    sortByValue(arrValueOfPrices)
    print (arrValueOfPrices)

    for i in range(0, arrPlaces.__len__() / 2 + 1):
        arrPlaces[i][1] += arrValueOfPrices[i][1]
    print ("Itog")
    print (arrPlaces)



