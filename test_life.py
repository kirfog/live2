import unittest
import numpy

from app.life import Life

class TestLive(unittest.TestCase):
    def test_fill_life(self):
        life = Life()
        print (life.fill())
        self.assertEqual(life.fill().all(), numpy.random.randint(1, size=(life.x, life.y)).all())