#!/usr/bin/bash
job=$(echo $1|awk -F . '{print $1}')
local=$(pwd)
cd ${local}/tmp
mkdir ${job}
cd  ${job}
cp ${local}/optxyzs/$1 . 
cp ${local}/INS/$2 .
cp ${local}/sep_single.sh .
./sep_single.sh $1 $2

rm *.ins
rm sep_single.sh
rm $1

cd ..
cp -r  ${job} ${local}/frag-xyz
rm -rf ${job}
cd ${local}
