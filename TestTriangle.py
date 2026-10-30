import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Equilateral
    def test01_EquilateralMin(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')

    def test02_EquilateralMax(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be Equilateral')

    # Isosceles - equal pair in each position
    def test03_IsoscelesAB(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be Isoceles')

    def test04_IsoscelesAC(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be Isoceles')

    def test05_IsoscelesBC(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be Isoceles')

    def test06_IsoscelesBoundary(self):
        self.assertEqual(classifyTriangle(200,200,1),'Isoceles','200,200,1 should be Isoceles')

    # Scalene
    def test07_ScaleneA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be Scalene')

    def test08_ScaleneB(self):
        self.assertEqual(classifyTriangle(7,9,5),'Scalene','7,9,5 should be Scalene')

    # Right - longest side in each position
    def test09_RightC(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test10_RightA(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test11_RightB(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def test12_RightLarger(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')

    # Not a triangle - each side too long, plus the a + b == c edge case
    def test13_NotTriangleC(self):
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle','1,2,10 is not a triangle')

    def test14_NotTriangleA(self):
        self.assertEqual(classifyTriangle(10,2,1),'NotATriangle','10,2,1 is not a triangle')

    def test15_NotTriangleB(self):
        self.assertEqual(classifyTriangle(2,10,1),'NotATriangle','2,10,1 is not a triangle')

    def test16_NotTriangleFlat(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is flat, not a triangle')

    # Invalid input - zero, negative, over 200, not an integer
    def test17_ZeroA(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0 is not a valid side')

    def test18_ZeroB(self):
        self.assertEqual(classifyTriangle(1,0,1),'InvalidInput','0 is not a valid side')

    def test19_ZeroC(self):
        self.assertEqual(classifyTriangle(1,1,0),'InvalidInput','0 is not a valid side')

    def test20_Negative(self):
        self.assertEqual(classifyTriangle(-1,2,2),'InvalidInput','negative sides are not valid')

    def test21_Over200A(self):
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201 is over the limit')

    def test22_Over200B(self):
        self.assertEqual(classifyTriangle(1,201,1),'InvalidInput','201 is over the limit')

    def test23_Over200C(self):
        self.assertEqual(classifyTriangle(1,1,201),'InvalidInput','201 is over the limit')

    def test24_Float(self):
        self.assertEqual(classifyTriangle(1.5,2,2),'InvalidInput','1.5 is not an integer')

    def test25_String(self):
        self.assertEqual(classifyTriangle('a',2,2),'InvalidInput','a string is not an integer')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
