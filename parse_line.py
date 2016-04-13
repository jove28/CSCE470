#!/usr/bin/python -tt
# parses the file by words, and displays number.
import sys

def print_(filename):
  word_count = {}
  input_file = open(filename, 'r')
  i = 0
  for line in input_file:
    word_count[line] = i
    i += 1
    
    if(line.isspace()):
      continue
    elif( line[0] == "T" and line[4] == "S"):
      i = 0
    else:
      print line , ": " , word_count[line]
  input_file.close()  # Not strictly required, but good form.
  return word_count

def main():
  if len(sys.argv) != 3:
    print 'usage: ./prac.py {--count } file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  
  if option == '--count':
    print_(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
