#!/usr/bin/env python

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    instructions = []
    for line in f.readlines():
      instructions.append(int(line.rstrip()))
  return instructions

def solve(instructions):
  idx = 0
  steps = 0
  while idx in range(len(instructions)):
    steps += 1
    offset = instructions[idx]
    instructions[idx] += 1
    idx += offset
  print '%s steps' % steps



def test():
  solve([0, 3, 0, 1, -3])

def main():
  solve(read_puzzle('input.txt'))

main()