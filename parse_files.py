import sys
import os

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
  
def main():
  if len(sys.argv) != 3:
    print 'usage: ./parse_file.py {-folder} file'
    sys.exit(1)
  option = sys.argv[1]
  mainFolder = sys.argv[2]
  
  if option == '-folder':
    parse_files(mainFolder)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
