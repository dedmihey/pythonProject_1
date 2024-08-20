import unittest
import runner
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_run(self):
        runner = Runner('rn')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_walk(self):
        runner_1 = Runner('wl')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_challenge(self):
        runner_2 = Runner('rn_')
        runner_3 = Runner('wl_')
        for _ in range(10):
            runner_2.run()
            runner_3.run()
        self.assertNotEqual(runner_2, runner_3)




rt = RunnerTest()
rt.test_run()
rt.test_walk()
rt.test_challenge()
