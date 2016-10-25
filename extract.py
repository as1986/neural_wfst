#!/usr/bin/env python


def main():
    from io import open as uopen
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('fname')
    parser.add_argument('idx', default=2, type=int)
    parser.add_argument('--key', default=u'V;1;SG;IND;PST;PFV')
    parser.add_argument('--shuffle', action='store_true')
    parser.add_argument('--folds', default=10, type=int)
    parser.add_argument('--lang', default='sp')
    parser.add_argument('--key-idx', default=3, type=int)
    args = parser.parse_args()
    fh = uopen(args.fname, encoding='utf-8')
    lines = [x.strip().split(u'\t') for x in fh]
    to_extract = [(x[0], x[args.idx]) for x in lines if x[args.key_idx] == args.key]
    if args.shuffle:
        from random import shuffle
        shuffle(to_extract)
    from distutils.dir_util import mkpath
    from sklearn.model_selection import ShuffleSplit
    rs = ShuffleSplit(n_splits=args.folds, test_size=0.2, random_state=42)
    for i, (train_indices, test_indices) in enumerate(rs.split(to_extract)):
        mkpath('res/ryan_splits/{}-10fold/{}'.format(args.lang, i))
        train_fh, dev_fh, test_fh = (uopen('res/ryan_splits/{}-10fold/{}/train.uniq'.format(args.lang, i), mode='w', encoding='utf-8'),
                                     uopen('res/ryan_splits/{}-10fold/{}/dev.uniq'.format(args.lang, i), mode='w', encoding='utf-8'),
                                     uopen('res/ryan_splits/{}-10fold/{}/test.uniq'.format(args.lang, i), mode='w', encoding='utf-8'),
                                     )
        for idx in train_indices:
            train_fh.write(u'{}\t{}\n'.format(to_extract[idx][0], to_extract[idx][1]))

        for j, idx in enumerate(test_indices):
            if j % 2 == 0:
                dev_fh.write(u'{}\t{}\n'.format(to_extract[idx][0], to_extract[idx][1]))
            else:
                test_fh.write(u'{}\t{}\n'.format(to_extract[idx][0], to_extract[idx][1]))


if __name__ == '__main__':
    main()
