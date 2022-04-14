import numpy as np
import pandas as pd
import os
from rdkit import Chem
from rdkit.Chem import AllChem 

# load data
rawdata = pd.read_csv("mol_dup_2w.csv",names=["smiles"])
data = rawdata.to_numpy()


# wash it
# 

# smis =?
smis = data
#  confomer gen function
def conf_gen(smi, conf_number, smi_charge):
    m = Chem.MolFromSmiles(smi)
    m = Chem.AddHs(m)
    #print(smi)
    params = AllChem.ETKDGv3()
    cids = AllChem.EmbedMultipleConfs(m, numConfs = conf_number, params = params)
    res = AllChem.MMFFOptimizeMoleculeConfs(m,numThreads=40,mmffVariant="MMFF94")

    #a =[]
    #for atom in m.GetAtoms():
    #     a.append(atom.GetAtomicNum())
    #numbers = np.asarray(a)

    energy_low = min(res)
    label = res.index(energy_low)

    conf_mol = Chem.MolToXYZBlock(m,confId=label)
    return conf_mol




#len(smis)




os.system("rm -rf  mole_2w")
os.system("mkdir mole_2w")
for inf in range(len(smis)):
    mol_info = conf_gen(smi=str(smis[inf])[2:-2], conf_number=400, smi_charge=0)

    if len(str(inf)) == 1:
        num = '00000' + str(inf)
    elif len(str(inf)) == 2:
        num = '0000' + str(inf)
    elif len(str(inf)) == 3:
        num = '000' + str(inf)
    elif len(str(inf)) == 4:
        num = '00' + str(inf)
    elif len(str(inf)) == 5:
        num = '0' + str(inf)
    elif len(str(inf)) == 6:
        num =  str(inf)

    fileName = 'molecule'+ '_'+ num + '.xyz'
    f = open(fileName, 'w')
    f.write(mol_info)
    f.close()
    os.system("mv %s mole_2w"% fileName)

