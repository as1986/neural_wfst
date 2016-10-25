cd /export/a10/kitsing/neural_wfst
export PYTHONPATH="$PWD/src/python" 
export THEANO_FLAGS="floatX=float32,mode=FAST_RUN,optimizer_excluding=local_shape_to_shape_i" 
echo $SGE_TASK_ID
./train_lang.py $SGE_TASK_ID hungarian
