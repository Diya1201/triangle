import unittest     # this makes Python unittest module available

def classifyTriangle(a, b, c):
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a :
        return 'Isosceles'
    elif a != b and b != c and c != a:
        return 'Scalene'
    elif a^2+b^2==c^2:
        return 'Right Triangle'
    else:
        return 'NotATriangle'
def runClassifyTriangle(a, b, c):
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")
class TestTriangles(unittest.TestCase):
     def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(runClassifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

     def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(runClassifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(runClassifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(runClassifyTriangle(10,15,30),'Isoceles','Should be Scalene')

     if __name__ == '__main__':
    # examples of running the code
      runClassifyTriangle(3,4,5)
      runClassifyTriangle(1,1,1)
      runClassifyTriangle(4,5,5)
      runClassifyTriangle(3,4,5)
      runClassifyTriangle(24,24,16)
      unittest.main(exit=True) 