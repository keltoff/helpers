from datetime import datetime, timedelta


class Period:
    def __init__(self, d=0, h=0, m=0, s=30, report=None):
        self.interval = timedelta(days=d, hours=h, minutes=m, seconds=s)
        self.last = datetime.now()

        self.text = report

    def __nonzero__(self):
        t = datetime.now()
        if (t - self.last) < self.interval:
            return False
        else:
            self.last = t
            if self.text:
                print t.strftime('\r' + self.text)

            return True
