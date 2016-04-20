import sys
import os
import re



mainDictionary = []

def parse_file(fileName):
  inputFile = open(( fileName), 'r')
  
  for line in inputFile:
    word = line.rstrip().split(',')
    mainDictionary.append(word)

def getKey(item):
  return item[0][2]
  
  
#def getClass(classList):
  
  

def main():

  if len(sys.argv) != 3:
    print 'usage: ./prac.py {--parse} file'
    sys.exit(1)
  option = sys.argv[1]
  fileName = sys.argv[2]
  
  if option == '--parse':
    parse_file(fileName)
    sorted(mainDictionary,key = getKey)
    
    for item in mainDictionary:
      if item[2] == 'CAVERLEE J':
        print item 
    
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
