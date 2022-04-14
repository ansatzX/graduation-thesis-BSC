#!/bin/bash
source /export/home/gongcx/.bashrc 
softload conda
conda activate xchem
#python comp_molecule.py 
nohup python comp_fragments.py &

