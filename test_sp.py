#!/usr/bin/env python
import transducer_score
import sys
import os

batch = int(sys.argv[1])-1

folds = range(10)

count = 0

for f in folds:
    if count == batch:
        print 'fold: {}'.format(f)
        os.system('mkdir -p /export/a10/kitsing/tmp/ryanout-sp-{}/train'.format(f))
        import glob
        fixed = glob.glob('results/sp-{}*/transducer_fixed.pkl'.format(f))

        if len(fixed) > 0:
            pretrained = max(fixed)
        else:
            unfixed = glob.glob('results/sp-{}*/transducer.pkl'.format(f))
            assert len(unfixed) > 0
            pretrained = max(unfixed)
                dname = os.path.dirname(pretrained)
                os.system('cp {} {}/transducer_fixed.pkl'.format(pretrained, dname))
                pretrained = dname + '/transducer_fixed.pkl'

            results = transducer_score.main(train_fn='res/ryan_splits/sp-10fold/{}/train.uniq'.format(f),
                                            dev_fn='res/ryan_splits/sp-10fold/{}/train.uniq'.format(f),
                                            test_fn='res/ryan_splits/sp-10fold/{}/train.uniq'.format(f), 
                                            folder='results/sp-{}'.format(f),
                                            ryanout='/export/a10/kitsing/tmp/ryanout-sp-{}/train/'.format(f),
                                            pretrained_param_pklfile=pretrained,
                                            nepochs=-1,
                                            perform_training=0,
                                            perform_testing=1,
                                            crunching=1,
                                            )
        count += 1
