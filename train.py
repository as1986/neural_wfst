#!/usr/bin/env python

import theano
theano.config.floatX='float32'
import transducer_score

def train(path_prefix, where_to_store, fold):
    scores = []
    path = path_prefix + '/{}/'.format(fold)
    train_fn = path + '/train'
    dev_fn = path + '/dev'
    test_fn = path + '/test'
    folder = where_to_store + '_{}'.format(fold)
    scores.append(transducer_score.main(train_fn=train_fn, dev_fn=dev_fn, test_fn=test_fn, folder=folder))
    return scores

if __name__ == '__main__':
    import sys
    print train(sys.argv[1], sys.argv[2], sys.argv[3])

