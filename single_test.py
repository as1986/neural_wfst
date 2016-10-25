import transducer_score

results = transducer_score.main(train_fn='res/wicentowski_split/basque-10fold/7/train.uniq',
                                dev_fn='res/wicentowski_split/basque-10fold/7/train.uniq',
                                test_fn='res/wicentowski_split/basque-10fold/7/train.uniq', 
                                folder='results/tmp2',
                                ryanout='/export/a10/kitsing/tmp/ryanout',
                                pretrained_param_pklfile='results/tmp_6/transducer.pkl',
                                nepochs=-1,
                                perform_training=0,
                                perform_testing=1,
                                crunching=1,
                                )
