import sys
import os
count = {}

def word_count_dict(folderName):
  for filename in os.listdir(folderName):
    f = open(os.path.join(folderName, filename), "r")
    for line in f:
      words = line.lower().split()     
      for word in words:
        if len(word) == 6 and word.isalpha():
          if not word in count:
            count[word] = 1
          else:
            count[word] = count[word] + 1
    f.close()
  return count

def get(index):
  return index[1]

def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count = word_count_dict(filename)
  items = sorted(word_count.items(), key=get_count, reverse=True)
  for item in items[:10]:
      print item[0], item[1]
  

def get_count(word_count_tuple):
  #Returns the count from a dict word/count tuple  -- used for custom sort.
  return word_count_tuple[1]


# This basic command line argument parsing code is provided and
# calls the print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./121007964.py -folder'
    sys.exit(1)

  folder = sys.argv[2]
  if folder == "books":
    print_words(folder)
  else:
    print 'unknown folder: ' + folder
    sys.exit(1)

if __name__ == '__main__':
  main()
