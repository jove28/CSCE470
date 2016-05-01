import sys
import os
import re

#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

#after the pdf files  have been converted to txt
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
#     0     1        2      3          4  5  6   7   8  9 10 11 12    13  
# { [Class, SY, Last Name, First Name, A, B, C, D, F, GPR, I, S, U, Q, X ] }


#run on folder pdftotext to get the usefull data
def show(mainFolder):
  CLASS = ""
  SY = "SPRING 2015"
  PROF_F = ""
  PROF_L = ""
  MASTER = ""
  
  outputFile = open(("Database.txt"), 'w')
  #for each file get the specified data
  for file in os.listdir(mainFolder):
    inputFile = open(os.path.join(mainFolder, file), 'r')
    for line in inputFile:
      word = line.split()
      #get what term
      if word[0] == "GRADE":
        p = re.compile('(FALL|SPRING|SUMMER) \w{4}')
        temp = p.search(' '.join(word))
        if(temp.group(0) != SY):
          SY = temp.group(0)
      else:
        #parse each line that matches the regex containing a className-classNumber-classSection 
        if re.match('((\w){4}-(\w){3}-(\w){3})',' '.join(word)): #CLASS
          p = re.compile('((\w){4}-(\w){3}-(\w){3})')
          regex = p.search(' '.join(word))
          temp = regex.group(0) #get the entire line as a string 
          CLASS = ''.join(temp[0:8])
          PROF_L = ''.join(word[14:15]) 
          PROF_F = ''.join(word[15:16])
          GRADE = PROF_L + ',' + PROF_F + ',' + ','.join(word[1:6]) + ',' + ','.join(word[7:13]) 
          MASTER =  CLASS + ',' + SY + ',' + GRADE 
          #print MASTER
          outputFile.write(str(MASTER) + '\n')
        else:
          continue
    inputFile.close()
  outputFile.close()  
    
    
    
  
  
#to start, first convert pdf files using pdttotext -layout pdffile.pdf
# then './extract_files.py --parse Folder' to remove whitespace
# then './extract_files.py --extract Folder' to get the database.txt
def main():
  if len(sys.argv) != 3:
    print 'usage: ./extract_files.py {--parse | --extract} Folder'
    sys.exit(1)
  option = sys.argv[1]
  mainFolder = sys.argv[2]
  
  #gets rid of whitespace
  if option == '--parse':
    parse_files(mainFolder)
  #extracts usefull data
  elif option == '--extract':
    show(mainFolder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
