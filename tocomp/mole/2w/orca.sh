#!/bin/bash

#This script was written by Dr. Tian Lu at Beijing Kein Research Center for Natural Sciences (www.keinsci.com)
#Contact: sobereva@sina.com
#Webpage: http://sobereva.com/422

#Set the number of parallel cores and maximum memory utilized by each core (MB)
nprocs=26
maxcore=2000
#Set calculation level
level=" r2SCAN-3c  "
#Set parameters for other aspects
#  can write noautostart here
numset="tightscf "
#ORCA executable path
# orcapath="/sob/orca/orca"
orcapath=$(which orca)


read atoms derivs charge spin < $2

if [ $derivs == "2" ] ; then
        task="engrad freq"
elif [ $derivs == "1" ] ; then
        task="engrad"
fi

#Create ORCA input file
echo "Generating mol.inp"
cat > mol.inp <<EOF
! $level $numset $task BOHRS notrah nopop
%pal nprocs $nprocs end
%maxcore $maxcore
* xyz $charge $spin
$(sed -n 2,$(($atoms+1))p < $2 | cut -c 1-72)
*
%cpcm
  epsilon 37.781
end
EOF

#Run ORCA
echo "Running ORCA..."
$orcapath mol.inp "--bind-to core --verbose"  > mol.out
echo "ORCA running finished!"

echo "Extracting data from ORCA outputs via extderi"
./extorca $3 $atoms $derivs

mv mol.gbw tmp.gbw -f
rm mol.* mol_* -f
mv tmp.gbw mol.gbw -f
