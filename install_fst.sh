 # Create a prefix directory if one does not yet exist
 cd /export/a10/kitsing
 mkdir -p local
 cd local
 export PREFIX=$PWD
 echo $PREFIX

 # Download OpenFST
 mkdir -p openfst
 cd openfst
 wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.4.1.tar.gz
 tar xzf openfst-1.4.1.tar.gz

 # Build OpenFST
 rm -rf objdir
 mkdir objdir
 cd objdir/
 ../openfst-1.4.1/configure --prefix=$PREFIX \
       --enable-pdt --enable-bin --enable-ngram-fsts
 make -j 8
 make install
