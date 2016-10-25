#!/usr/bin/env python
import transducer_score
import sys
import os

batch = int(sys.argv[1])-1

folds = range(10)

count = 0

for f in folds:
    if count == batch:
        os.system('mkdir -p /export/a10/kitsing/tmp/ryanout-sp-{}'.format(f))
        os.system('mkdir -p /export/a10/kitsing/tmp/sp-folds-{}'.format(f))
        results = transducer_score.main(train_fn='res/ryan_splits/sp-10fold/{}/train.uniq'.format(f),
                                        dev_fn='res/ryan_splits/sp-10fold/{}/dev.uniq'.format(f),
                                        test_fn='res/ryan_splits/sp-10fold/{}/test.uniq'.format(f), 
                                        folder='results/sp-{}'.format(f),
                                        ryanout='/export/a10/kitsing/tmp/ryanout-sp-{}'.format(f),
                                        )
    count += 1
