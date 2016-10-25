echo "export PREFIX=/export/a10/kitsing/local" >> ~/.bashrc

echo 'export CPLUS_INCLUDE_PATH=$PREFIX/include:$CPLUS_INCLUDE_PATH
export LIBRARY_PATH=$PREFIX/lib:$LIBRARY_PATH
export LIBRARY_PATH=$PREFIX/lib/fst:$LIBRARY_PATH
export LD_LIBRARY_PATH=$PREFIX/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$PREFIX/lib/fst:$LD_LIBRARY_PATH
export PATH=$PREFIX/bin:$PATH
export PYTHONPATH=$PREFIX/lib/python2.7/site-packages:$PYTHONPATH' >> ~/.bashrc
