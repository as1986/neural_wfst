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
            print 'language: {} fold: {}'.format(l, f)
            os.system('mkdir -p /export/a10/kitsing/tmp/ryanout-{}-{}/train'.format(l,f))
            import glob
            fixed = glob.glob('results/{}-{}*/transducer_fixed.pkl'.format(l,f))

            if len(fixed) > 0:
                pretrained = max(fixed)
            else:
                unfixed = glob.glob('results/{}-{}*/transducer.pkl'.format(l,f))
                assert len(unfixed) > 0
                pretrained = max(unfixed)
                dname = os.path.dirname(pretrained)
                os.system('cp {} {}/transducer_fixed.pkl'.format(pretrained, dname))
                pretrained = dname + '/transducer_fixed.pkl'

            results = transducer_score.main(train_fn='res/wicentowski_split/{}-10fold/{}/train.uniq'.format(l,f),
                                            dev_fn='res/wicentowski_split/{}-10fold/{}/train.uniq'.format(l,f),
                                            test_fn='res/wicentowski_split/{}-10fold/{}/train.uniq'.format(l,f), 
                                            folder='results/{}-{}'.format(l,f),
                                            ryanout='/export/a10/kitsing/tmp/ryanout-{}-{}/train/'.format(l,f),
                                            pretrained_param_pklfile=pretrained,
                                            nepochs=-1,
                                            perform_training=0,
                                            perform_testing=1,
                                            crunching=1,
                                            )
        count += 1
