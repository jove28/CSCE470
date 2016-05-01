import sys
import os
import re
reload(sys)
sys.setdefaultencoding("utf-8")

#parse database.txt into a list
def parse_file():
  inputFile = open(('Database.txt'), 'r')
  mainDictionary = []
  
  for line in inputFile:
    word = line.rstrip().split(',')
    mainDictionary.append(word)
    
  sortedDictionary = sorted(mainDictionary,key = getKey)
  return sortedDictionary

def getKey(item):
  return (item[0], item[2])
  
  
#returns class based on input  
def getClass(className, instructor, dictionary):
  classList = []
  
  if className and instructor and className != '-':
    print "both"
    for item in dictionary:
      if className == item[0] and instructor == item[2]:
        classList.append(item)
  elif className and className != '-':
    print "classname"
    for item in dictionary:
      if className == item[0]:
        classList.append(item)
  elif instructor:
    print "instrcutor"
    for item in dictionary:
      if instructor == item[2]:
        classList.append(item)
          
  return classList
  

# For testing:
def main():
  dictionary = parse_file()
  name = "CSCE-121"
  instructor = ""
  result = getClass(name, instructor, dictionary)
  
  for item in result:
    print item
  


if __name__ == '__main__':
  main()
  
