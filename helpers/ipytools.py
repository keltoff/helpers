from ipywidgets import IntProgress, interact
from IPython.display import display


def progress(iterable):
    f = IntProgress(min=0, max=len(iterable)-1)
    display(f)
    for i, item in enumerate(iterable):
        f.value = i
        yield item


def select_from(values):
    def handler_maker(func):
        def handler(idx):
            func(values[idx])

        interact(handler, idx=(0, len(values)-1))

        return handler

    return handler_maker