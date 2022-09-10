#!/usr/bin/bash
job=$1
local=$(pwd)
WHICH_PART=$2
mkdir ${local}/tmp/frag-logs-${WHICH_PART}
cd ${local}/tmp/frag-logs-${WHICH_PART}
mkdir ${job}
cd ${job}
cp  -r ${local}/frag-logs-${WHICH_PART}/${job}/ .

for inf in $(ls mole*|sort);do
    cd ${inf} 
    mkdir tmp 
    for jnf in $(ls *.xyz|sort);do
        cd tmp
        xtb $inf > ${jnf//.xyz/.log}
        lines=$(head -n 1 $jnf)
        echo -e "${jnf//.xyz/.log}\n${lines}"|./xtb2valence${local}  
        cp {jnf//.xyz/.AtomValence} ../
        rm *
        cd ..
    done
    cp *.AtomValence ${local}/frag-logs-${WHICH_PART}/${job}/${inf}
done
cd ${local}