#!/bin/bash`
export whichjob=$1
cp -r ./logs/${whichjob} ./workspace 
cd workspace/${whichjob}


# pick error and NT
for inf in $(ls -l *.log|awk '{print $9}');do
  export FILENAME=${inf%.*}
  export NT=$(grep "Normal termination" ${inf})
  if [[ "${NT}" != "" ]];then
    echo "$FILENAME----NT" >> NT-${whichjob}
  else
    echo "" >> Error-${whichjob}
    echo "" >> Error-${whichjob}
    echo "****$FILENAME----ERROR****" >> Error-${whichjob}
    tail $FILENAME.log >> Error-${whichjob}
  fi
done

mv NT-${whichjob} ../..
mv Error-${whichjob} ../..
