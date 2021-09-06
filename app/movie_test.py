import unittest
from models import movie
Movie = movie.Movie



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

    def test_init(self):
        """Test that init is setting proper attributes."""
        self.assertEqual(self.new_movie.id, 1234)
        self.assertEqual(self.new_movie.title, 'Python Must Be Crazy')
        self.assertEqual(self.new_movie.overview,
                         'A thrilling new Python Series')
        self.assertEqual(self.new_movie.poster_path,
                         'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average, 8.5)
        self.assertEqual(self.new_movie.vote_count, 129993)

    # def test_movie_init(self):
    #     """Test that movie is initialized properly."""
    #     self.assertEqual(self.movie.title, 'The Big Lebowski')
    #     self.assertEqual(self.movie.release_year, 1998)
    #     self.assertEqual(self.movie.director, 'The Coen brothers')
    #     self.assertEqual(self.movie.duration, 122)
    #     self.assertEqual(self.movie.rating, 5.0)

    # def test_movie_str(self):
    #     """Test that movie is printed properly."""
    #     self.assertEqual(str(self.movie), 'The Big Lebowski (1998)')

    # def test_movie_repr(self):
    #     """Test that movie is printed properly."""
    #     self.assertEqual(repr(self.movie), '<Movie The Big Lebowski (1998)>')

    # def test_movie_eq(self):
    #     """Test that movie is equal to itself."""
    #     self.assertEqual(self.movie, self.movie)

    # def test_movie_hash(self):
    #     """Test that movie is hashable."""
    #     self.assertEqual(hash(self.movie), hash(self.movie))

    # def test_movie_lt(self):
    #     """Test that movie is less than another."""
    #     self.assertLess(self.movie, Movie(title='The Big Lebowski',
    #                                       release_year=1998,
    #                                       director='The Coen brothers',
    #                                       duration=122,
    #                                       rating=4.5))

    # def test_movie_gt(self):
    #     """Test that movie is greater than another."""
    #     self.assertGreater(self.movie, Movie(title='The Big Lebowski',
    #                                          release_year=1998,
    #                                          director='The Coen brothers',
    #                                          duration=122,
    #                                          rating=4.0))

    if __name__ == '__main__':
        unittest.main()