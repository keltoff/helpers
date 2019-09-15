import datetime


class EtaTimer:
    def __init__(self, n):
        self.start_time = datetime.datetime.now()
        self.n = n
        self.step_estimate = datetime.timedelta(0)
        self.done = []

    def update(self, i):
        self.done.append(i)
        self.step_estimate = self.time_sofar / len(self.done)

    @property
    def time_sofar(self):
        now = datetime.datetime.now()
        return now - self.start_time

    @property
    def eta(self):
        if self.done:
            dt = self.step_estimate * (self.n - self.done[0] - 1) - self.time_sofar
            return datetime.timedelta(seconds=dt.seconds)
        else:
            return None

    def __str__(self):
        return self.eta.__str__()
        # if self.eta:
        #     return '{:x}'.format(self.eta)  #self.eta.__str__('x')
        # else:
        #     return '???'
