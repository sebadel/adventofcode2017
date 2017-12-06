#!/usr/bin/env python

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    for line in f.readlines():
      return [int(x) for x in line.rstrip().split('\t')]

def _reallocate(blocks):
  max_block = max(blocks)
  cursor = blocks.index(max_block)
  blocks[cursor] = 0
  while max_block > 0:
    cursor = (cursor + 1) % len(blocks)
    blocks[cursor] += 1
    max_block -= 1
  return blocks

def solve(blocks):
  states = []
  found = False
  while blocks not in states:
    states.append(blocks)
    blocks = _reallocate(blocks[:]) # pass the list  by value
  print len(states)

def test():
  solve([0, 2, 7, 0])

def main():
  solve(read_puzzle('input.txt'))

main()