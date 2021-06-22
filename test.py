import unittest
import main



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.disk = main.YaDisk()





if __name__ == '__main__':
    os.environ['YADISKTOKEN'] = 'AQAAAAAiInFGAAcnrrMWM26pAU06kf9ELT3P3-I'

    unittest.main()
