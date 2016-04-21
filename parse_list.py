import sys
import os
import re

mainDictionary = []

def parse_file(fileName):
  inputFile = open((fileName), 'r')
  
  for line in inputFile:
    word = line.rstrip().split(',')
    mainDictionary.append(word)

def getKey(item):
  return (item[2], item[1])
  
  
#def getClass(classList):
  
  

def main():
  parse_file("Database.txt")
  sortedDictionary = sorted(mainDictionary,key = getKey)
  
  if len(sys.argv) != 3:
    print 'usage: ./parse_list.py {--class} query'
    sys.exit(1)
  option = sys.argv[1]
  query = sys.argv[2].lower()
  
  if option == '--class':
    for item in sortedDictionary:
      lastName = []
      lastName= item[0].lower().split(' ')
      if lastName[0] == query:
        print item 
        
  else:
    print 'unknown option: ' + option
    sys.exit(1)


if __name__ == '__main__':
  main()
