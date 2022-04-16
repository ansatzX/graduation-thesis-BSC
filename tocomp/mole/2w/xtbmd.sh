#!/bin/bash
cat  << EOF > md.inp
\$md
   temp= 400 
   time= 100.0 
   dump= 50.0  
   step=  1.0  
   hmass=1  
   shake=1  
\$end
EOF

# run md simulation for next steps, this xyz is preselected by rdkit, I think it can not crash when md start.
xtb $1 --input md.inp --omd --gfn 2
pwd
