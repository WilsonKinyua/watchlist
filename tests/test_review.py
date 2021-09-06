import unittest
from app.models import Reviews


class TestReview(unittest.TestCase):
    def setUp(self):
        self.new_review = Reviews(  # create new_review
            "This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!",
            "https://www.rottentomatoes.com/m/space_jam/reviews/",
            "https://www.rottentomatoes.com/m/space_jam/posters/300_/space_jam_movie_poster_by_cyberjocky-d5gqgx",
            "https://www.rottentomatoes.com/m/space_jam/reviews/reviews.json?type=top_critics&page=1&limit=40&sort="
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Reviews))
