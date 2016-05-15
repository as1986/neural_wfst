#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[ ]:

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--celex-path', default='./res/celex')
    parser.add_argument('--result-path', default='./results')
    args = parser.parse_args()
    
    import glob
    celex_paths = glob.glob('{}/*'.format(args.celex_path))
    from os.path import basename
    tasks = [basename(x) for x in celex_paths]
    storage_paths = ['{}/{}'.format(args.result_path,x) for x in tasks]
    train_paths = ['{}/0500'.format(x) for x in celex_paths]
    for train_path, storage_path in zip(train_paths, storage_paths):
        # train(train_path, storage_path)
        print train_path
        print storage_path
        import os
        for i in xrange(5):
            os.system('sbatch -n 1 -t 24:00:00 train.sh {} {} {}'.format(train_path, storage_path, i))
