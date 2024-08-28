import logging
import unittest
from runner_4 import Runner

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('Willi', -2)
            logging.info('test_walk выполнен успешно')
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            return -1

    def test_run(self):
        try:
            runner_2 = Runner(555)
            logging.info('test_run выполнен успешно')
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except:
            logging.warning('Неверный тип данных для Runner', exc_info=True)
            return -2


if __name__ == '__main__':
    unittest.main()
