#!usr/bin/python

import sys
import re

def main():
  names = []
  filename = "/home/bhuvan/tmp/google-python-exercises/babynames/baby1990.html"
  f = open(filename, 'r')
  text = f.read()
  names.append(re.findall(r'<td>([a-zA-Z]+)</td>', text))
  return(names)

if __name__ == '__main__':
  main()
