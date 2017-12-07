#!/usr/bin/env python

import re

def read_puzzle(filename):
  rows = []
  with file(filename, 'r') as f:
    for line in f.readlines():
      rows.append(line.rstrip())
  return rows

def parser(line):
  regexp = re.match('([a-z]+)\s\((\d+)\)(\s->\s)?([a-z\,\s]*)?', line)
  if regexp:
    name = regexp.groups()[0]
    stack = [x for x in regexp.groups()[3].split(', ')]
    return name, stack

def solve(towers):
  bottoms = set()
  loads = set()
  for tower in towers:
    name, stack = parser(tower)
    bottoms.add(name)
    loads.update(set(stack))
  print 'bottom: %s' % [b for b in (bottoms - loads)]

def test():
  data = [
    'pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)'
  ]
  solve(data)

def main():
  solve(read_puzzle('input.txt'))

main()