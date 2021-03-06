#!/usr/bin/env python
import transducer_score
import sys
import os

batch = int(sys.argv[1])-1

languages = ['basque', 'english', 'tagalog', 'irish']
folds = range(10)

count = 0

for l in languages:
    for f in folds:
        if count == batch:
            os.system('mkdir -p /export/a10/kitsing/tmp/ryanout-{}-{}'.format(l,f))
            results = transducer_score.main(train_fn='res/wicentowski_split/{}-10fold/{}/train.uniq'.format(l,f),
                                            dev_fn='res/wicentowski_split/{}-10fold/{}/dev.uniq'.format(l,f),
                                            test_fn='res/wicentowski_split/{}-10fold/{}/test.uniq'.format(l,f), 
                                            folder='results/{}-{}'.format(l,f),
                                            ryanout='/export/a10/kitsing/tmp/ryanout-{}-{}'.format(l,f),
                                            )
        count += 1
