from __future__ import print_function
import numpy as np


def ransac(dataset, solution_fun, eval_fun, sample_no=3, iteration_no=1000, threshold=0.1, silent=False):
    best_samples = None
    best_result = None
    best_support = 0
    dn = dataset.shape[0]
    for it in range(iteration_no):
        samples = dataset[np.random.choice(dn, sample_no, replace=False), :]
        result = solution_fun(samples)
        support = eval_fun(result, dataset, threshold=threshold)
        if support > best_support:
            best_support = support
            best_samples = samples
            best_result = result
            if not silent:
                print('\rIteration {}, Current support: {:.2f}%'.format(it, 100*best_support/dn), end='')

    if not silent:
        print('\rFinal support: {:.2f}%'.format(100*best_support/dn))
    return best_result, best_support, best_support/dn