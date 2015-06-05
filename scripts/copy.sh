srcdir="/data"
dstdir="/data"
d=$(date +%m%d%y)

for srcfile in ${srcdir}/*
do
    dstfile=$(basename $srcfile)
    dstfile=${dstfile/\./${d}\.}
    cp $srcfile $dstdir/$dstfile
done
# requires change dstfile to work
