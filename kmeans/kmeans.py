# coding=utf-8
import codecs
import random
import math

class City:
    city_name = ''
    population = 0
    def __init__(self, city_name, population):
        self.city_name = city_name
        self.population = float(population)

def readdata(file):
    cities = []
    input_file = codecs.open(file,'r')
    lines = input_file.readlines()
    for line in lines:
        data =  line.rstrip('\n').split(' ')
        city = City(data[0], data[1])
        cities.append(city)
    input_file.close()
    return cities

def initial(k, cities):
    classes = []
    centroid = 0
    for i in range(k):
        centroid = random.uniform(min([cities[i].population for i in range(len(cities))]),\
         max([cities[i].population for i in range(len(cities))]))
        classes.append([City('none', centroid)])
    return classes

def calcuscontriod(classes):
    for aclass in classes:
        if len(aclass) == 1:
            continue
        else:
            centroid = 0
            for i in range(1, len(aclass)):
                centroid += aclass[i].population
            centroid /= len(aclass) - 1
            aclass[0] = City('none',centroid)
    return classes

def argmin(classes, cities):
    
    def mindist(classes, city):
        classfy_to = 0
        for i in range(len(classes)):
            if (city.population - classes[i][0].population)**2 \
            < (city.population - classes[classfy_to][0].population)**2:
                classfy_to = i
        classes[classfy_to].append(city)       

    for city in cities:
        mindist(classes, city)
    return classes

def printclass(classes):
    for aclass in classes:
        for city in aclass:
            print city.city_name,"=",city.population
        print "--------------------------"    

def getvar(classes):
    dist = 0
    for aclass in classes:
        for j in range(1,len(aclass)):
            dist += math.fabs(aclass[j].population -  aclass[0].population)
    return dist

k = 3 # how many clusters you want
epsilon = 0.0001 # constant number for terminating the loop
old_var = -1 # initial number for oldvar
cities = readdata('data\population.txt')
classes =  initial(k, cities)

while True:
    classes = argmin(classes, cities)
    new_classes = []
    classes = calcuscontriod(classes)
    new_var = getvar(classes)
    if math.fabs(new_var - old_var) < epsilon:
        break
    else:
        old_var = new_var
    for i in range(len(classes)):
        new_classes.append([classes[i][0]])
    classes = new_classes

printclass(classes)


