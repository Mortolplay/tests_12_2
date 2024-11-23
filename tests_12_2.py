import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, k in cls.all_results.items():
            print(k)

    def test_tournament_1(self):
        test1 = Tournament(90, self.runner_1, self.runner_3)
        test1_result = {k: str(v) for k, v in test1.start().items()}
        TournamentTest.all_results['1'] = test1_result
        self.assertTrue(test1_result[2], 'Ник')

    def test_tournament_2(self):
        test1 = Tournament(90, self.runner_2, self.runner_3)
        test1_result = {k: str(v) for k, v in test1.start().items()}
        TournamentTest.all_results['2'] = test1_result
        self.assertTrue(test1_result[2], 'Ник')

    def test_tournament_3(self):
        test1 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        test1_result = {k: str(v) for k, v in test1.start().items()}
        TournamentTest.all_results['3'] = test1_result
        self.assertTrue(test1_result[3], 'Ник')

if __name__ == "__main__":
    unittest.main()












