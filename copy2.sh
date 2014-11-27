#!/bin/bash

for i in `ls -1 /directroy`
do
cp $i /newDirectory/$i.`date +%m%d%Y`
done
