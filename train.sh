#!/usr/bin/env bash
export PYTHONPATH=$HOME/neural_wfst:$HOME/neural_wfst/src/python
source ~/anaconda-python
export THEANO_FLAGS='floatX=float32,device=cpu'
~/neural_wfst/train.py $1 $2 $3
