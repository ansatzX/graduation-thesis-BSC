# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import os
from rdkit import Chem
from rdkit.Chem import AllChem


# In[2]:


PTDic =  {'H':'1',
 'He':'2',
 'Li':'3',
 'Be':'4',
 'B':'5',
 'C':'6',
 'N':'7',
 'O':'8',
 'F':'9',
 'Ne':'10',
 'Na':'11',
 'Mg':'12',
 'Al':'13',
 'Si':'14',
 'P':'15',
 'S':'16',
 'Cl':'17',
 'Ar':'18',
 'K':'19',
 'Ca':'20',
 'Sc':'21',
 'Ti':'22',
 'V':'23',
 'Cr':'24',
 'Mn':'25',
 'Fe':'26',
 'Co':'27',
 'Ni':'28',
 'Cu':'29',
 'Zn':'30',
 'Ga':'31',
 'Ge':'32',
 'As':'33',
 'Se':'34',
 'Br':'35',
 'Kr':'36',
 'Rb':'37',
 'Sr':'38',
 'Y':'39',
 'Zr':'40',
 'Nb':'41',
 'Mo':'42',
 'Tc':'43',
 'Ru':'44',
 'Rh':'45',
 'Pd':'46',
 'Ag':'47',
 'Cd':'48',
 'In':'49',
 'Sn':'50',
 'Sb':'51',
 'Te':'52',
 'I':'53',
 'Xe':'54',
 'Cs':'55',
 'Ba':'56',
 'W':'74',
 'Os':'76',
 'Ir':'77',
 'Pt':'78',
 'Au':'79',
 'Hg':'80',
 'Tl':'81',
 'Pb':'82',
 'Bi':'83' }


# In[7]:


rawdata=pd.read_csv("mole_dup.csv")


# In[8]:


data= rawdata.to_numpy()


# In[14]:


smis = data[:,0]


# In[18]:


def conf_gen(smi, conf_number, smi_charge):
    m = Chem.MolFromSmiles(smi)
    m = Chem.AddHs(m)
    #print(smi)
    params = AllChem.ETKDGv3()
    cids = AllChem.EmbedMultipleConfs(m, numConfs = 100 , params = params)
    res = AllChem.MMFFOptimizeMoleculeConfs(m,numThreads=40,mmffVariant="MMFF94")
      
    #a =[]
    #for atom in m.GetAtoms():
    #     a.append(atom.GetAtomicNum())
    #numbers = np.asarray(a) 
    
    energy_low = min(res)
    label = res.index(energy_low)

    conf_mol = Chem.MolToXYZBlock(m,confId=label) 
    return conf_mol


# In[22]:


len(smis)


# In[26]:



for inf in range(4000,6000):
    mol_info = conf_gen(smi=smis[inf], conf_number=400, smi_charge=0)

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

    fileName = 'molecule_dup'+ '_'+ num + '.xyz'
    f = open(fileName, 'w')
    f.write(mol_info)
    f.close()
    os.system("mv %s ../mole_dup_xyz"% fileName)  


# In[ ]:




