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
            os.system('mkdir -p /export/a10/kitsing/tmp/ryanout-{}-{}/dev'.format(l,f))
            os.system('mkdir -p /export/a10/kitsing/tmp/pkl-{}-{}'.format(l,f))
            import glob
            pretrained = max(glob.glob('results/{}-{}*/transducer_fixed.pkl'.format(l,f)))
            results = transducer_score.main(train_fn='res/wicentowski_split/{}-10fold/{}/dev.uniq'.format(l,f),
                                            dev_fn='res/wicentowski_split/{}-10fold/{}/dev.uniq'.format(l,f),
                                            test_fn='res/wicentowski_split/{}-10fold/{}/dev.uniq'.format(l,f), 
                                            folder='/export/a10/kitsing/tmp/pkl-{}-{}'.format(l,f),
                                            ryanout='/export/a10/kitsing/tmp/ryanout-{}-{}/dev/'.format(l,f),
                                            pretrained_param_pklfile=pretrained,
                                            nepochs=-1,
                                            perform_training=0,
                                            perform_testing=1,
                                            crunching=1,
                                            )
        count += 1
