import _json

def valueByTag(place,arrPerson):
    value = 0
    for teg in arrPerson:
        if (teg in place):
            value += place[teg]*arrPerson[teg]
            #print(place[teg])
    return (value)

def sortByValue(arr):
    max = 0
    for i in range(len(arr[1])):
        for j in range(len(arr[1]) - 1, i, -1):
            if arr[1][j] > arr[1][j - 1]:
                test1 = arr[0][j]
                test2 = arr[1][j]
                arr[0][j] = arr[0][j - 1]
                arr[1][j] = arr[1][j - 1]
                arr[0][j - 1] = test1
                arr[1][j - 1] = test2


def addPlaceToTop5Places(place1,max):
    if arrTop5Places.__len__() > 5:
        arrTop5Places[0].pop()
        arrTop5Places[1].pop()
    arrTop5Places[0].append(place1)
    arrTop5Places[1].append(max)
    sortByValue(arrTop5Places)
    return(arrTop5Places[1][arrTop5Places[0].__len__()-1])


arrPlaces = [{"a":30,"b":4,"d":10},{"a":1,"b":2,"c":3},{"a":3,"b":4,"c":5}]
arrPerson = {"a":1,"b":2,"c":3,"d":4}

print("test")

#кусочек для тегов
max5 = 0
arrTop5Places = [[],[]]
arrValueOfPlaces = []
for place in arrPlaces:
    if (valueByTag(place,arrPerson) > max5)|(arrTop5Places.__len__() <= 5):
        max5 = addPlaceToTop5Places(place, valueByTag(place,arrPerson))

print (arrTop5Places)

#кусочек для цены

