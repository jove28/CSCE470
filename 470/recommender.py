import sys
import os
import re
import parse
import math


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

def getNormalDistribution(results):
    diff = 0
    mean = getAvg(results)

    for item in results:
        diff += abs(float(item[9]) - mean)**2
        
    dev = math.sqrt(diff/len(results))


    for item in results:
        term = ((float(item[9]) - mean ) / dev)
        if term >= 0 and term < 1:
            item.append(term*4)
        elif term >= 1 and term < 2:
             item.append(term*5)
        elif term >=2:
            item.append(term*6)
        elif term < 0 and term >= -1:
            item.append(term*3)
        elif term <-1 and term >= -2:
            item.append(term*2)
        else:
            item.append(term*1)
    return results
    
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

def getSemester(results):
    master = []
    spring = []
    summer = []
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
        
    master.append(spring)
    master.append(summer)
    master.append(fall)
    return master
    
def getSemesterAvg(results):
    master = getSemester(results)
    
    spring = master[0]
    summer = master[1]
    fall = master[2]
    
    springAvg = getAvg(spring)
    summerAvg = getAvg(summer)
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
    
# returns list of list by class instructor
#[ [[csce-121,Daugherity],[csce-121,daugherity]],[[csce-121,lee]].etc..]  
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

def calcRank(result):
    distAvg = 0
    semDist = 0
    for item in result:
        distAvg += float(item[15])
        semDist += float(item[17])
    distAvg = distAvg/len(result)
    semDist = semDist/len(result)
    total = distAvg*60 + semDist*80
    return total
    
        
        
def format(results):
    final = []
    final.append(str(results[0][2]) + ", " + str(results[0][3]))
    final.append(str(results[0][0]))
    avg = getAvg(results)
    final.append(str(avg))
    final.append(getMinMax(results))
    final.append(getSemesterAvg(results) )
    final.append(calcRank(results))
    return final
    
def sortAvg(item):
    return item[5]

def recommender(classInput, instructor, results):
    list = []
    if classInput and instructor and classInput != '-':
        temp = []
        temp.append(str(results[0][2]) + ", " + str(results[0][3]))
        temp.append(str(results[0][0]))
        avg = getAvg(results)
        temp.append(str(avg))
        temp.append( getMinMax(results) )
        temp.append(getSemesterAvg(results) )
        list.append(temp)

    elif instructor and classInput == '-':
        gauss = getNormalDistribution(results)
        result  = getInstructorClass(gauss)
        final = calcSemesterTaught(result)
        list = []
        for item in final:
            list.append(format(item))
        list = sorted(list, key = sortAvg, reverse = True )
    elif classInput != '-' and not instructor:
        gauss = getNormalDistribution(results)
        result = getClassInstructor(gauss)
        final = calcSemesterTaught(result)
        list = []
        for item in final:
            list.append(format(item))
        list = sorted(list, key = sortAvg, reverse = True )

    return list

def calcSemesterTaught(results):
    length = 0
    avg = 0
    diff = 0
    
    for item in results:
        for obj in item:
            length += len(item)
            semester = obj[1]
            obj.append( int(semester[-5:]) - 2016 + 5.5)
            
    for item in results:
        for obj in item:
            avg += float(obj[16])
    mean = avg / length

    for item in results:
        for obj in item:
            diff += abs(float(obj[16]) - mean)**2
        
    dev = math.sqrt(diff/length)


    for item in results:
        for obj in item:
            term = ((float(obj[16]) - mean ) / dev)
            if term >= 0 and term < 1:
                obj.append(term*4)
            elif term >= 1 and term < 2:
                obj.append(term*5)
            elif term >=2:
                obj.append(term*6)
            elif term < 0 and term >= -1:
                obj.append(term*3)
            elif term <-1 and term >= -2:
                obj.append(term*2)
            else:
                obj.append(term*1)

    return results  

    

# For testing:
def main():
    dictionary = parse.parse_file()
    name = "CSCE-221"
    instructor = "SCHAEFER"
    result = parse.getClass(name, instructor, dictionary)
#     temp2 = getNormalDistribution(result)
#     temp = getClassInstructor(temp2)
#     temp3 = calcSemesterTaught(temp)
   
#     list = []
#     for item in temp3:
#             list.append(format(item))
#     list = sorted(list, key = sortAvg, reverse = True )
#     # for item in temp3:
#     #     for obj in item:
#     #         print obj
    print result
    
    
if __name__ == '__main__':
  main()
  