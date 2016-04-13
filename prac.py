#!/usr/bin/python -tt
# parses the file by words, and displays number.
import sys

def print_(filename):
  word_count = {}
  input_file = open(filename, 'r')
  i = 0
  for line in input_file:
    words = line.split()
    for word in words:
      word_count[word] = i
      i += 1
      print word , ": " , word_count[word]
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
