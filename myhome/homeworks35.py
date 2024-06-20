from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill

    def run(self):
        global day
        for day in range(1, int(100 / self.skill + 1)):
            n = day * self.skill
            print('Через ', day, 'день/дня/дней осталось ', 100 - n, 'врагов')
        print('Через ', day, 'дней', self.name, 'победил врагов')


knight1 = Knight('Sir_Lancelot', 10)
knight2 = Knight('Sir_ Galahad', 20)

print('На королевство напали враги')

knight1.start()
time.sleep(0.1)
knight2.start()

knight1.join()
knight2.join()

print('Мы победили')
