import unittest 
from app.models import movie 

class MovieTest(unittest.TestCase):
    """Test Class to test the behaviour of the movie class.
    """
    def setUp(self):
        """setUp method that will run before every test.
        """
        self.new_movie = movie(1234, 'Python Must Be Crazy', 'Athrilling new python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, movie))
     