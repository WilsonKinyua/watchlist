import unittest
from app.models import Movie


class MovieTest(unittest.TestCase):
    """Unit tests for Movie class."""
    def setUp(self):
        """Set up test database."""
        self.new_movie = Movie(1234, 'Python Must Be Crazy',
                               'A thrilling new Python Series',
                               'https://image.tmdb.org/t/p/w500/khsjha27hbs',
                               8.5, 129993)

    def test_instance(self):
        """Test that instance exists."""
        self.assertTrue(isinstance(self.new_movie, Movie))

    # def test_init(self):
    #     """Test that init is setting proper attributes."""
    #     self.assertEqual(self.new_movie.id, 1234)
    #     self.assertEqual(self.new_movie.title, 'Python Must Be Crazy')
    #     self.assertEqual(self.new_movie.overview,
    #                      'A thrilling new Python Series')
    #     self.assertEqual(self.new_movie.poster_path,
    #                      'https://image.tmdb.org/t/p/w500/khsjha27hbs')
    #     self.assertEqual(self.new_movie.vote_average, 8.5)
    #     self.assertEqual(self.new_movie.vote_count, 129993)
