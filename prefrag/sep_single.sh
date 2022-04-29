#!/bin/bash
export insfile=$2
export xyzfile=$1
export FILENAME=${xyzfile//.xyz/-}
cat $insfile |awk 'NR % 2 == 1 {print $0}' > ${FILENAME}temp1.ins
cat $insfile |awk 'NR % 2 == 0 {print $0}' > ${FILENAME}temp2.ins
export bonds=0
for use in $(cat ${FILENAME}temp1.ins );do
  export bonds=$(echo "$bonds+1" |bc)
  # do firts lines of ins
  if [[ $use == 1 ]];then
    export FILE1=${FILENAME}${bonds}-1.xyz
    export FILE2=${FILENAME}${bonds}-2.xyz
    #echo $use $FILE1 $FILE2 $bonds
  elif [[ $use == 2 ]];then
    export FILE1=${FILENAME}${bonds}-2.xyz
    export FILE2=${FILENAME}${bonds}-1.xyz
    #echo $use $FILE1 $FILE2 $bonds
  fi
  numbers=$(sed -n '1p ' ${xyzfile})
  numbers1=$(sed -n "${bonds} p " ${FILENAME}temp2.ins|wc -w)
  numbers2=$(echo "${numbers}-${numbers1}"|bc)
  #echo $numbers1 $numbers2
  echo ${numbers1}  > ${FILE1}
  echo "${FILE1} " >> ${FILE1}

  export numbers3=$(echo "${numbers}-1 "|bc)
  #rm ${FILENAME}temp3.ins
  for line in $(seq 0 ${numbers3});do
    echo $line >> ${FILENAME}temp3.ins
  done

  for line in $(sed -n "${bonds}p " ${FILENAME}temp2.ins);do
    export pick=$(echo "3+$line"|bc)
    sed -n "${pick} p" ${xyzfile} >> ${FILE1}
    export isdel=$(grep -w $line ${FILENAME}temp3.ins)
    if [[ $isdel != "" ]];then
      grep -w  $line ${FILENAME}temp3.ins  -v > ${FILENAME}temp4.ins
      mv  ${FILENAME}temp4.ins ${FILENAME}temp3.ins
    fi
  done

  for line in $(cat ${FILENAME}temp3.ins);do
    export pick=$(echo "3+$line"|bc)
    sed -n "${pick} p" ${xyzfile} >> ${FILE2}
  done

  rm ${FILENAME}temp3.ins
  sed -i "1i ${FILE2}"   ${FILE2}
  sed -i "1i ${numbers2}"  ${FILE2}
done

