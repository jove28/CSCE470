import sys
import os
import re
reload(sys)
sys.setdefaultencoding("utf-8")


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
  
  
  
def getClass(name, dictionary):
  classList = []
  for item in dictionary:
    if name == item[0]:
      classList.append(item)

  return classList
  

# For testing:
# def main():
#   dictionary = parse_file()
#   name = 'CSCE-313'
#   result = getClass(name, dictionary)
  
#   for item in result:
#     print item
  


# if __name__ == '__main__':
#   main()
  
