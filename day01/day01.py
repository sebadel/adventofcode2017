#!/usr/bin/env python

def read_puzzle(filename):
  with file(filename, 'r') as f:
    s = f.read()
  return s

def decode(s):
  result = 0
  s = s + s[0]
  while len(s) > 1:
    if s[0] == s[1]:
      result += int(s[0])
    s = s[1:]
  return result

def test():
  print decode('1122')
  print decode('1111')
  print decode('1234')
  print decode('91212129')

def main():
  s = read_puzzle('input.txt')
  print decode(s)

main()