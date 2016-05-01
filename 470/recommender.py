import sys
import os
import re
import parse


# list of objects -> avg
def getAvg(results):
    avg = 0
    if len(results) == 0:
        return 0
    else:
        for item in results:
            avg += float(item[9])
    avg = avg / len(results)
    return avg

#list of objects - > min/max    
def getMinMax(results):
    max = 0
    min = 100
    for item in results:
        if max <= float(item[9]):
            max = float(item[9])
    for item in results:
        if min >= float(item[9]):
            min = float(item[9])
    return str(str(max) + " / " + str(min))

def getSemesterAvg(results):
    summer = []
    spring = []
    fall = []
    
    for item in results:
        word = item[1]
        if word[:-5] == "SPRING":
            spring.append(item)
        elif word[:-5] == "SUMMER":
            summer.append(item)
        elif word[:-5] == "FALL":
            fall.append(item)
        else:
            continue
        
    summerAvg = getAvg(summer)
    springAvg = getAvg(spring)
    fallAvg = getAvg(fall)

    if summerAvg <= springAvg:
        if springAvg < fallAvg:
            return "Fall: " + str(fallAvg)
        else:
            return "Spring: " + str(springAvg)
    elif summerAvg >= springAvg:
        if summerAvg > fallAvg:
            return "Summer " + str(summerAvg)
        else:
            return "Fall: " + str(fallAvg)
 
def getKey2(item):
    return (item[2], item[3])
    
def getKey3(item):
    return item[0]

def getInstructorClass(results):
    master = sorted(results , key = getKey3)
    slave = []
    temp =  []
    index = []
    
    for item in master:
        name = str(item[0])
        if len(index) == 0:
            index.append(name)
            temp.append(item)
        elif name in index:
            temp.append(item)
        else:
            index.append(name)
            slave.append(temp)
            temp = []
            temp.append(item)
    slave.append(temp)
    return slave
  
def getClassInstructor(results):
    master = sorted(results , key = getKey2)
    slave = []
    temp =  []
    index = []
    
    for item in master:
        name = str(item[2]) + " " + str(item[3])
        if len(index) == 0:
            index.append(name)
            temp.append(item)
        elif name in index:
            temp.append(item)
        else:
            index.append(name)
            slave.append(temp)
            temp = []
            temp.append(item)
    slave.append(temp)
    return slave
    
def format(results):
    final = []
    final.append(str(results[0][2]) + ", " + str(results[0][3]))
    final.append(str(results[0][0]))
    avg = getAvg(results)
    final.append(str(avg))
    final.append( getMinMax(results) )
    final.append(getSemesterAvg(results) )
    return final
    
def sortAvg(item):
    return item[2]
    
def recommender(classInput, instructor, results):
    list = []
    if classInput and instructor and classInput != '-':
        list = []
        list.append(format(results))
    elif instructor and classInput == '-':
        final  = getInstructorClass(results) 
        print final
        list = []
        for item in final:
            list.append(format(item))
        list = sorted(list, key = sortAvg, reverse = True )
    elif classInput != '-' and not instructor:
        final = getClassInstructor(results)
        list = []
        for item in final:
            list.append(format(item))
        list = sorted(list, key = sortAvg, reverse = True )
    return list


# For testing:
def main():
    dictionary = parse.parse_file()
    name = ""
    instructor = "CAVERLEE"
    result = parse.getClass(name, instructor, dictionary)
    
    for item in result:
        print item


if __name__ == '__main__':
  main()
  
