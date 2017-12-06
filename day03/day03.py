
class Matrix(object):
  def __init__(self):
    self._cells = {}

  def getCell(self, pos):
    x, y = pos
    if x in self._cells and y in self._cells[x]:
      return self._cells[x][y]
    return False

  def setCell(self, pos, value):
    x, y = pos
    if x not in self._cells:
      self._cells[x] = {}
    self._cells[x][y] = value

class Cursor(object):
  def __init__(self):
    self._matrix = Matrix()
    self.x = 0
    self.y = 0
    self.value = 1
    self.direction = 'D'
    self.directions = 'RULD'

  @property
  def next_direction(self):
    i = self.directions.index(self.direction)
    i = (i + 1) % 4
    return self.directions[i]

  @property
  def moves(self):
    return {
      'U': (self.x, self.y+1),
      'D': (self.x, self.y-1),
      'L': (self.x-1, self.y),
      'R': (self.x+1, self.y)
    }

  @property
  def can_turn_left(self):
    return not self._matrix.getCell(self.moves[self.next_direction])

  def TurnLeft(self):
    self.x, self.y = self.moves[self.next_direction]
    self.direction = self.next_direction

  def MoveOn(self):
    self.x, self.y = self.moves[self.direction]

  def NextCell(self):
    return m

  def Iterate(self):
    self._matrix.setCell((self.x, self.y), self.value)
    self.value += 1
    if self.can_turn_left:
      self.TurnLeft()
    else:
      self.MoveOn()

  def Distance(self):
    return abs(self.x) + abs(self.y)


def solve(i):
  c = Cursor()
  while (c.value < i):
    c.Iterate()
  print ('%s => %s' % (i, c.Distance()))

def test():
  solve(1)
  solve(12)
  solve(23)
  solve(1024)

def main():
  solve(325489)

main()