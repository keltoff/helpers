from __future__ import print_function
from eta_timer import EtaTimer


def reported_queue(x, label):
    print(label, end='')
    while len(x) > 0:
        yield x
        print('\r' + label + ': ({} remaining)'.format(len(x)), end='')
    print('\r' + label + ': Done')


def timed_queue(x, label):
    print(label, end='')
    n = len(x)
    timer = EtaTimer(n)
    while len(x) > 0:
        yield x
        timer.update(n - len(x))
        print('\r' + label + ': ({} remaining) {}'.format(len(x), timer), end='')
    print('\r' + label + ': Done')


def reported_condition(x, label, test):
    val = test(x)
    print('\r' + label + ': {}'.format(x), end='')
    return val


def reported_cycle(values, label):
    print(label, end='')
    for i, x in enumerate(values):
        yield x
        print('\r' + label + ': ({}/{})'.format(i+1, len(values)), end='')
    print('\r' + label + ': Done')


def timed_cycle(values, label):
    print(label, end='')
    n = len(values)
    timer = EtaTimer(n)
    for i, x in enumerate(values):
        yield x
        timer.update(i)
        print('\r' + label + ': ({}/{}) {}'.format(i+1, n, timer), end='')
    print('\r' + label + ': Done')
