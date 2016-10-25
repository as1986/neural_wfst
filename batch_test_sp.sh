cd /export/a10/kitsing/neural_wfst
export PYTHONPATH="$PWD/src/python" 
export THEANO_FLAGS="floatX=float32,mode=FAST_RUN,optimizer_excluding=local_shape_to_shape_i" 
export OMP_NUM_THREADS=1
./test_sp.py $SGE_TASK_ID
