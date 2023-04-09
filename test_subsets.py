import unittest

import subsets


class TestGetAlphabetPoint(unittest.TestCase):
  def testCoord(self):
    self.assertEqual(subsets.GetAlphabetPoint(0, 0), 'aa')
    self.assertEqual(subsets.GetAlphabetPoint(0, 1), 'ab')
    self.assertEqual(subsets.GetAlphabetPoint(1, 1), 'bb')

  def testBoundaryCondition(self):
    self.assertEqual(subsets.GetAlphabetPoint(-1, -1), 'zz')
    self.assertEqual(subsets.GetAlphabetPoint(25, 25), 'zz')
    self.assertEqual(subsets.GetAlphabetPoint(26, 26), 'aa')


class TestSquareSubsetSize(unittest.TestCase):
  def testZero(self):
    self.assertEqual(subsets.SquareSubsetSize(0), 1)

  def testOne(self):
    self.assertEqual(subsets.SquareSubsetSize(1), 9)

  def testTwo(self):
    self.assertEqual(subsets.SquareSubsetSize(2), 25)

  def testThree(self):
    self.assertEqual(subsets.SquareSubsetSize(3), 49)

class TestGenerateSquareSubset(unittest.TestCase):
  def testZero(self):
    self.assertEqual(list(subsets.GenerateSquareSubset(0, 0, 0)), [(0, 0)])

  def testOne(self):
    self.assertEqual(len(list(subsets.GenerateSquareSubset(0, 0, 1))), 9)

  def testSameAsSquareSubsetSize(self):
    r = 1
    self.assertEqual(len(list(subsets.GenerateSquareSubset(0, 0, r))), subsets.SquareSubsetSize(r))
    r = 2
    self.assertEqual(len(list(subsets.GenerateSquareSubset(0, 0, r))), subsets.SquareSubsetSize(r))

class TestMakeTopos(unittest.TestCase):
  def mockDistanceFunction(self, x, y, r):
    yield 0, 0

  def testEmpty(self):
    t = subsets.MakeTopos(0, 0, 0, self.mockDistanceFunction)
    self.assertEqual(t, [])

  def testOne(self):
    t = subsets.MakeTopos(1, 1, 0, self.mockDistanceFunction)
    self.assertEqual(t, [{'aa'}])

  def testTwo(self):
    t = subsets.MakeTopos(2, 2, 0, self.mockDistanceFunction)
    self.assertEqual(t, [{'aa'} for _ in range(4)])


if __name__ == '__main__':
  unittest.main()
