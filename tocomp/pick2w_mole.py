
import pandas as pd
import numpy as np
import os
from rdkit import Chem
from rdkit.Chem import AllChem

rawdata=pd.read_csv("mole_dup.csv")
data= rawdata.to_numpy()
smis = data[:,0]
smis2w = smis[0:19999]
smis2w.tofile("mol_dup_2w.csv",sep="\n", format="%s")
