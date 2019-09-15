import numpy as np
import os.path


class Persistent:
    def __init__(self, filename):
        self.state = dict()
        self.file = filename

        if os.path.isfile(self.file):
            self.load()

    def load(self):
        self.state = np.load(self.filename)

    def save(self):
        np.savez(self.file, **self.state)
