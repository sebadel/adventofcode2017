#!/usr/bin/env python

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    for line in f.readlines():
      return ','.join([x for x in line.rstrip().split('\t')])

def _reallocate(blocks):
  blocks = [int(x) for x in blocks.split(',')]
  max_block = max(blocks)
  cursor = blocks.index(max_block)
  blocks[cursor] = 0
  while max_block > 0:
    cursor = (cursor + 1) % len(blocks)
    blocks[cursor] += 1
    max_block -= 1
  return ','.join([str(x) for x in blocks])


def solve(blocks):
  states = {}
  cnt = 0
  while blocks not in states.keys():
    states[blocks] = cnt
    blocks = _reallocate(blocks)
    cnt += 1
  print cnt - states[blocks]

def test():
  solve([0, 2, 7, 0])

def main():
  solve(read_puzzle('input.txt'))

main()