from collections import defaultdict
import time
import random
from threading import Thread
FISH = (None, 'плотва', 'окунь', 'лещ')

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)
        # будем проверять в цикле - а не пора ли нам заканчивать?
        self.need_stop = False

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1
            if self.need_stop:
                print(f'{self.name}: Ой, жена ужинать зовет! Сматываем удочки...', flush=True)
                break


vasya = Fisher(name='Вася', worms=100)
vasya.start()
time.sleep(1)
if vasya.is_alive():  # кстати с помощью этого метода можно проверить выполняется ли еще поток?
    vasya.need_stop = True
vasya.join()  # ожидание завершения обязательно - поток может некоторое время финализировать работу

# Подводя итог, нужно сказать, что в мультипоточном программированиии наши линейный код
# перестают быть линейным (СИНХРОННЫМ). Если ранее мы были уверены в последовательности выполнения кода,
# то при использовании потоков (процессов) код может выполняться АСИНХРОННО: нельзя гарантировать
# что за этим блоком кода будет выполняться вот этот.
# Представьте себе спагетти, которые мешают вилкой: где и когда соприкоснуться макаронины никто не знает...
