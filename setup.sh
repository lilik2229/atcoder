#!/bin/bash

if [ -e $@ ]; then
    echo $@' is already exist.'
    exit 1
fi

echo 'mkdir -p '$@'/{A,B,C,D}'
mkdir -p $@/{A,B,C,D}

echo 'cp input.txt and code.py'
cp ./code.py $@/A/
cp ./code.py $@/B/
cp ./code.py $@/C/
cp ./code.py $@/D/
cp ./input.txt $@/A/
cp ./input.txt $@/B/
cp ./input.txt $@/C/
cp ./input.txt $@/D/

echo 'done.'
exit 0
