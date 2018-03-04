#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import dataAnal
import dataStorage
import json


# dataStorage.addPlace(6,"Pizaa",1,{},"",{"fri":2})
# dataStorage.addPlace(7,"a",2,{},"",{"burger":1,"fri":1})
# dataStorage.addPlace(6,"v",3,{},"",{"pasta":2,"burger":1,"pizza":1})

places = dataStorage.getNPlaces(14)
    # print(places)
for place in places:
    p = place
    print(str(place["id"])+" "+place["img"])
# dataAnal.getTopPlaces(json_data)
# print(dataStorage.getPlace(5))

# place = dataStorage.getPlace(5)

# print place['name']
# dataStorage.createPlaces()
# dataStorage.editPlace(8)
# dataStorage.addPlace("Мастер кебаб",1,{"lat": 30.346492,"lon":59.971417},"ул. Смолячкова, 16","Шаверма",{"шаверма":1,"шаурма":1})
# dataStorage.addPlace("Суши Wok",1,{"lat": 30.3407157,"lon":59.971353},"ул. Смолячкова, 12","Суши и роллы",{"суши":1,"роллы":1,"вок":1,"лапша":1})
# dataStorage.addPlace("Цех 85",1,{"lat": 30.345278,"lon":59.971190},"ул. Смолячкова, 14, корп. 1, литера Б, пом. 11Н","Булочная, пекарня",{"пекарня":1,"булочная":1,"сендвичи":1,"кофе":1})
# dataStorage.addPlace("Social Club",2,{"lat": 30.3423567,"lon":59.9265407},"ул. Рубинштейна, 40/11","Хорошая коктейльная карта",{"вегитарианское":1,"вино":1,"салаты":1,"закуски":1})
# dataStorage.addPlace("Tse Fung",3,{"lat": 30.3438724,"lon":59.9292339},"ул. Рубинштейна, 13","Китайский ресторан",{"экзотическое":1,"лапша":1,"супы":1,"закуски":1,"горячее":1})
# dataStorage.addPlace("Frank",2,{"lat": 30.3419475,"lon":59.9264781},"ул. Рубинштейна, 29/28","Хорошая коктейльная карта",{"ребра":1,"бургеры":1,"бар":1,"коктейли":1})
# dataStorage.addPlace("Makaroni",2,{"lat": 30.342772,"lon":59.9273573},"ул. Рубинштейна, 23","Итальянская кухня",{"пицца":1,"закуски":1,"паста":1,"равиолли":1})
# dataStorage.addPlace("PITA'S",2,{"lat": 30.352859,"lon":59.9318357},"Невский пр., 65","Шаверма",{"шаверма":2,"закуски":1})
# dataStorage.addPlace("FAN OF DONUTS",2,{"lat": 30.3440565,"lon":59.9292283},"ул. Рубинштейна, 26а","Вкусные пончики",{"сладкое":2,"пончики":1, "кофе":1})
# dataStorage.addPlace("Duo Asia",2,{"lat": 30.3448066,"lon":59.9302288},"ул. Рубинштейна, 20","Азиатская кухня",{"азиатское":1, "закуски":1, "морепродукты":1, "экзотическое":1})
# dataStorage.addPlace("Vinostudia",2,{"lat": 30.3427261,"lon":59.9270631},"улица Рубинштейна, 38,","Винный бар-ресторан",{"закуски":1, "паста":1, "вино":1})
# dataStorage.addPlace("Буше",2,{"lat": 30.3454974,"lon":59.9247308},"Разъезжая ул., 13","Уютное место",{"сладкое":2, "кофе":1, "сендвичи":1, "выпечка":1})
# dataStorage.addPlace("Punk Brew",2,{"lat": 30.344455,"lon":59.9303796},"ул. Рубинштейна, 9","Пивной бар",{"пицца":1,"бургеры":1,"бар":1,"коктейли":1,"пиво":1})
# dataStorage.addPlace("Булочная Ф. Вольчека № 9",1,{"lat": 30.3416675,"lon":59.9702991},"ул. Смолячкова, 11","Булочная",{"сладкое":1, "пироги":1, "кофе":1, "выпечка":1})
# dataStorage.addPlaceImage(15,"http://phink.team/images/15.jpg")
# dataStorage.addPlaceImage(10,"http://phink.team/images/8.jpg")
# dataStorage.addPlaceImage(13,"http://phink.team/images/12.jpg")
# dataStorage.addPlaceImage(12,"http://phink.team/images/12.jpg")
# dataStorage.addPlaceImage(5,"http://phink.team/images/4.jpeg")
# dataStorage.addPlaceImage(14,"http://phink.team/images/13.jpg")
# # dataStorage.addPlaceImage(7,"http://phink.team/images/6.jpg")
# dataStorage.addPlaceImage(8,"http://phink.team/images/6.jpg")

# # print(dataStorage.getUser(320962426))
# print(dataStorage.getAllPlaces())