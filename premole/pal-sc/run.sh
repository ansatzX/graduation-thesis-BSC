#!/bin/bash
source ~/.bashrc
cd /export/home/gongcx/data/code/graduation-thesis-BSC/tocomp/pal-sc 
softload conda
conda activate xchem

for inf in *.py;do
  nohup python $inf  &
done

