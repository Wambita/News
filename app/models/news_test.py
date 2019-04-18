import unittest 
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behavoir of the news class
    '''

    def setUp(self):
        '''
        Set up method will run before every test
        '''
        self.new_news = News("Fana","Fana sheila","Sheila is great","images/sheila"," Sheila has always been great","17-04-2019","https://fanais great.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()