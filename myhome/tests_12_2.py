import unittest
from runner_ import Runner
from runner_ import Tournament

is_frozen = False


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.us = Runner('Usain', 10)
        self.an = Runner('Andrew', 9)
        self.nic = Runner('Nic', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour(self):
        trn = Tournament(90, self.us, self.nic)
        self.all_results = trn.start()
        self.assertTrue(self.all_results[2] == self.nic)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        trn = Tournament(90, self.an, self.nic)
        self.all_results = trn.start()
        self.assertTrue(self.all_results[2] == self.nic)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        trn = Tournament(90, self.us, self.an, self.nic)
        self.all_results = trn.start()
        self.assertTrue(self.all_results[3] == self.nic)

    def tearDown(self):
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()
