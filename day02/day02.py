#!/usr/bin/env python

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    for line in f.readlines():
      row =  [int(x) for x in line.rstrip().split('\t')]
      rows.append(row)
  return rows

def row_checksum(row):
  return max(row) - min(row)

def my_checksum(rows):
  return sum([row_checksum(row) for row in rows])


def test():
  rows = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
  ]
  print my_checksum(rows)

def main():
  print my_checksum(read_puzzle('input.txt'))

main()