import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_search_player(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_search_non_existing_player(self):
        self.assertIsNone(self.statistics.search("Kaapo"))

    def test_team(self):
        self.assertEqual(str(self.statistics.team("PIT")[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_by_points(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.POINTS)[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_by_goals(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.GOALS)[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_by_assists(self):
        self.assertEqual(str(self.statistics.top(2, SortBy.ASSISTS)[1]), "Yzerman DET 42 + 56 = 98")

    def test_top_without_criteria(self):
        self.assertEqual(str(self.statistics.top(1)[0]), "Gretzky EDM 35 + 89 = 124")