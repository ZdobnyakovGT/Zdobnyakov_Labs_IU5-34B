import time


class cm_timer_1:
    def enter(self):
        self.start_time = time.time()
        return self

    def exit(self, type, value, traceback):
        self.end_time = time.time() - self.start_time
        print('time:', self.end_time)


with cm_timer_1():
    time.sleep(5.5)


from contextlib import contextmanager


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    execution_time = time.time() - start_time
    print(execution_time)


with cm_timer_2():
    time.sleep(5.5)