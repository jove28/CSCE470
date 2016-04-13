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

#helper_function, counts the lines  
def count_lines(fileName):
  inputFile = open(os.path.join("Texts", fileName), 'r')
  i = 0
  for line in inputFile:
   print line + ":" + str(i)
   i += 1
  inputFile.close()
   
   
  #     0       1      2  3  4  5  6   7   8  9 10 11 12    13        14  15  16  17  18   19
  # { [Class, Section, A, B, C, D, F, GPR, I, S, U, Q, X, Instructor, %A, %B, %C, %D, %F , SY]
  
  #     0       1      2  3  4  5  6   7   8  9 10 11 12  13  14  15  16  17  18  
  # { [Class, Section, A, B, C, D, F, GPR, I, S, U, Q, X, %A, %B, %C, %D, %F, SY]
   
def show(fileName):
  CLASS = ""
  CLASS1 = ""
  SECTION = ""
  SY = ""
  check = 0
  PERCENT0 = ""
  PERCENT1 = ""
  COURSE = ""
  
  inputFile = open(os.path.join("Texts", fileName), 'r')
  for line in inputFile:
    word = line.split()
    if word[0] == "TEXAS" or word[0] == "SECTION" or word[0] == "TOTAL":
      continue
    elif re.match('(-+)',' '.join(word)):
      continue
    elif word[0] == "GRADE":
      p = re.compile('(FALL|SPRING|SUMMER) \w{4}')
      temp = p.search(' '.join(word))
      SY = temp.group(0)
      print SY
    elif word[0] == "COLLEGE:":
      COLLEGE = " ".join(word[1::])
      print " ".join(word[1::])
    elif word[0] == "DEPARTMENT:":
      DEPARTMENT = " ".join(word[1::])
      print DEPARTMENT
    else:
      if re.match('((\w){4}-(\w){3}-(\w){3})',' '.join(word)): #CLASS
        check = 0
        p = re.compile('((\w){4}-(\w){3}-(\w){3})')
        temp = p.search(' '.join(word))
        #print word
        CLASS = temp.group(0)
        CLASS1 = CLASS[0:8]
        SECTION = CLASS[-3::]
        GRADE = word[1:6] + word[7:13] + word[14:16]
        
      if re.match('((\w){2}.(\w){2}%)',' '.join(word)):
        p = re.compile('((\w){2}.(\w){2}%)')
        temp = p.search(' '.join(word))
        PERCENT = temp.group(0)
        
        if check == 0: #for the class section
          PERCENT0 = word[0:5]
          #print PERCENT , "CLASS"
          print "CLASS", CLASS1 , SECTION , GRADE , PERCENT0 , SY
        
        else: # for the course total 
          PERCENT1 = word[0:5]
          #print PERCENT , "COURSE"
          print "COURSE", CLASS1 , SECTION , COURSE , PERCENT1 , SY
          
      if word[0] == "COURSE":
        check = 1
        COURSE = word[2:7] + word[8:14] + word[15:17]
        
        
      
  #     0       1      2  3  4  5  6   7   8  9 10 11 12    13        14  15  16  17  18   19
  # { [Class, Section, A, B, C, D, F, GPR, I, S, U, Q, X, Instructor, %A, %B, %C, %D, %F , SY]
  
  #     0       1      2  3  4  5  6   7   8  9 10 11 12  13  14  15  16  17  18  
  # { [Class, Section, A, B, C, D, F, GPR, I, S, U, Q, X, %A, %B, %C, %D, %F, SY]  
    
      
      
   
   
   
def main():

  if len(sys.argv) != 3:
    print 'usage: ./prac.py {--parse | --count | -- show} file'
    sys.exit(1)

  option = sys.argv[1]
  fileName = sys.argv[2]
  
  if option == '--parse':
    parse_file(fileName)
  elif option == '--count':
    count_lines(fileName)
  elif option == '--show':
    show(fileName)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
