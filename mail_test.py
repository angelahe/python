import unittest
from mail import make_email 

class TestMailFunction(unittest.TestCase):

    def test_make_email(larry):
        larry.assertEqual(make_email("Larry", "Shumlich"), "larry.shumlich@evolveu.ca")
        larry.assertEqual(make_email("", ""), None)
        larry.assertEqual(make_email(), None)
        larry.assertEqual(make_email("Larry", ""), "larry@evolveu.ca")
        larry.assertEqual(make_email("", "Shumlich"), "shumlich@evolveu.ca")
        larry.assertEqual(make_email("Larry"), "larry@evolveu.ca")


if __name__ == '__main__':
    unittest.main()