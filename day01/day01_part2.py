#!/usr/bin/env python

def read_puzzle(filename):
  with file(filename, 'r') as f:
    s = f.read()
  return s

def decode(s):
  result = 0
  cursor = 0
  while cursor < len(s):
    if s[cursor] == s[(cursor + (len(s)/2)) % len(s)]:
      result += int(s[cursor])
    cursor += 1
  return result

def test():
  print decode('1212')
  print decode('1221')
  print decode('123425')
  print decode('123123')
  print decode('12131415')

def main():
  s = read_puzzle('input.txt')
  print decode(s)

main()