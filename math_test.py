import unittest
from mathstuff import Math

class TestMathMethods(unittest.TestCase):

    def test_new(self):
        newMath = Math(10, 20)
        self.assertIsNotNone(newMath)
        self.assertEqual(newMath.real, 10)
        self.assertEqual(newMath.unreal, 20)
    

    def test_make_square(self):
        newComplex = Math(1, 2)
        self.assertEqual(type(newComplex.make_square()), Math)
        self.assertEqual(newComplex.make_square().real, -3)
        self.assertEqual(newComplex.make_square().unreal, 4)

    def test_print(self):
        newComplex = Math(1,2)
        self.assertEqual(newComplex.__repr__(), "1+2i")
        newComplex2 = Math(1, -2)
        self.assertEqual(newComplex2.__repr__(), "1-2i")
        newComplex3 = Math(0, 0)
        self.assertEqual(newComplex3.__repr__(), "0")
        newComplex4 = Math(5, 0)
        self.assertEqual(newComplex4.__repr__(), "5")
        newComplex5 = Math(0, 7)
        self.assertEqual(newComplex5.__repr__(), "7i")

    
if __name__ == '__main__':
    unittest.main()