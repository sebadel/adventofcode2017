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
    weight = regexp.groups()[1]
    stack = [x for x in regexp.groups()[3].split(', ')]
    return name, stack, weight

class Program(object):
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
    self.load = []

  def add_load(self, program):
    self.load.append(program)

  def computed_load(self):
    return self.weight + sum([x.computed_load() for x in self.load])

def solve(towers):
  programs = {}
  for tower in towers:
    name, stack, weight = parser(tower)
    print 'name: %s - weight: %s - stack: %s' % (name, weight, stack)
    if name and name not in programs:
      programs[name] = Program(name, int(weight))
    else:
      programs[name].weight = int(weight)
    for s in stack:
      if not s:
        continue
      if s not in programs:
        programs[s] = Program(s, 0)
      programs[name].add_load(programs[s])
  for n, p in programs.iteritems():
    weights = [l.computed_load() for l in p.load]
    if weights:
      diff = max(weights) - min(weights)
      if diff > 0:
        print 'n: %s' % n
        print 'weight: %s' % p.weight
        print diff
        for l in p.load:
          print ('%s => %s' % (l.name, l.computed_load()))

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