import unittest2 as unittest

class TravisTestCase(unittest.TestCase):
    def test_hello_world(self):
        hw = "hello " + "world"
        self.assertEqual(hw, "hello world", "hello world should be equal")


def main():
    travis_suite = unittest.TestLoader().loadTestsFromTestCase(TravisTestCase)

    return unittest.TestSuite([travis_suite])

if __name__ == "__main__":
    unittest.main()