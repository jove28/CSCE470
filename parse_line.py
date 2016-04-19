#!/usr/bin/python -tt
# parses the file by words, and displays number.
import sys
import os
import re

#removes whitespace and writes new file
def parse_file(fileName):
  inputFile = open(os.path.join("Texts", fileName), 'r')
  outputFile = open(os.path.join("Texts", "C" + fileName), 'w')
  
  for line in inputFile:
    if(line.isspace()):
      continue
    else:
      outputFile.write(line)
  inputFile.close()
  outputFile.close()

#file format output
#     0          1      2  3  4  5  6   7   8  9 10 11 12    13     14  15  16  17  18   19
# { [Class, Instructor, A, B, C, D, F, GPR, I, S, U, Q, X, %A, %B, %C, %D, %F , SY]
  
def show(fileName):
  CLASS = ""
  SY = "SPRING 2015"
  PERCENT0 = ""
  COURSE = ""
  PROF = ""
  MASTER = ""
  
  inputFile = open(os.path.join("Texts", fileName), 'r')
  outputFile = open(os.path.join("Texts", "E" + fileName), 'w')
  for line in inputFile:
    word = line.split()

    if word[0] == "GRADE":
      p = re.compile('(FALL|SPRING|SUMMER) \w{4}')
      temp = p.search(' '.join(word))
      if(temp.group(0) != SY):
        SY = temp.group(0)
    else:
      if re.match('((\w){4}-(\w){3}-(\w){3})',' '.join(word)): #CLASS
        check = 0
        p = re.compile('((\w){4}-(\w){3}-(\w){3})')
        regex = p.search(' '.join(word))
        temp = regex.group(0)
        CLASS = ''.join(temp[0:8])
        PROF = ' '.join(word[14:16])
        GRADE = PROF + ',' + ','.join(word[1:6]) + ',' + ','.join(word[7:13]) 
        
        MASTER =  CLASS + ',' + SY + ',' + GRADE + ',' + PERCENT0
        print MASTER
        outputFile.write(str(MASTER) + '\n')
        
      # elif re.match('((\w){2}.(\w){2}%)',' '.join(word)):
      #   p = re.compile('((\w){2}.(\w){2}%)')
      #   temp = p.search(' '.join(word))
      #   PERCENT0 = ','.join(word[0:5])
      #   MASTER =  CLASS + ',' + SY + ',' + GRADE + ',' + PERCENT0
      #   print MASTER
      #   outputFile.write(str(MASTER)+ '\n')
      else:
        continue
        
  outputFile.close()  

def main():

  if len(sys.argv) != 3:
    print 'usage: ./prac.py {--parse | --count | -- show} file'
    sys.exit(1)

  option = sys.argv[1]
  fileName = sys.argv[2]
  
  if option == '--parse':
    parse_file(fileName)
  elif option == '--show':
    show(fileName)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
