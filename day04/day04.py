#!/usr/bin/env python

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    for line in f.readlines():
      rows.append(line.strip())
  return rows

def is_valid(passphrase):
  words = passphrase.split(' ')
  buf = {}
  for word in words:
    if word in buf:
      return False
    else:
      buf[word] = 1
  return True

def main():
  valid = 0
  passphrases = read_puzzle('input.txt')
  for passphrase in passphrases:
    if is_valid(passphrase):
      valid += 1
  print '%s out of %d are valid' % (valid, len(passphrases))

main()