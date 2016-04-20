import sys
import os
import re

#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
#given the folder Project/ 
#it will get rid of empty lines and condense a folder to a file
#move the files from Project/file.txt to the folder pdftotext
def parse_files(mainFolder):
  for folder in os.listdir(mainFolder):
    outputFile = open(os.path.join(mainFolder, folder + '.txt' ), 'w')
    for file in os.listdir(mainFolder + "/" + folder):
      if file.endswith(".txt"):
        openedFile = open(os.path.join(mainFolder + '/' + folder, file), "r")
        for line in openedFile:
          if(line.isspace()):
            continue
          else:
            outputFile.write(line)
        openedFile.close()
    outputFile.close()
    
    

#file format output
#     0          1      2  3  4  5  6   7   8  9 10 11 12    13     14  15  16  17  18   19
# { [Class, Instructor, A, B, C, D, F, GPR, I, S, U, Q, X, %A, %B, %C, %D, %F , SY]
  
def show(mainFolder):
  CLASS = ""
  SY = "SPRING 2015"
  PERCENT0 = ""
  COURSE = ""
  PROF = ""
  MASTER = ""
  
  outputFile = open(("Database.txt"), 'w')
  for file in os.listdir(mainFolder):
    inputFile = open(os.path.join(mainFolder, file), 'r')
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
          #print MASTER
          outputFile.write(str(MASTER) + '\n')
        else:
          continue
    inputFile.close()
  outputFile.close()  
    
    
    
  
def main():
  if len(sys.argv) != 3:
    print 'usage: ./extract_files.py {--parse | --extract} Folder'
    sys.exit(1)
  option = sys.argv[1]
  mainFolder = sys.argv[2]
  
  if option == '--parse':
    parse_files(mainFolder)
  elif option == '--extract':
    show(mainFolder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
