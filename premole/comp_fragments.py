# coding: utf-8

# In[15]:


import pandas as pd 
import numpy as np 
import os
from rdkit import Chem
from rdkit.Chem import AllChem
from multiprocessing import Pool


# In[10]:


rawdata = pd.read_csv("frag_dup.csv")
data= rawdata.to_numpy()
smis = data[:,0]


# In[11]:


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


# In[16]:


len(smis)


# In[36]:



def genxyz(start,end):
    print("gen",start,end)
    for inf in range(start,end): 
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
        fileName = 'fragment_pos_dup'+ '_'+ num + '.xyz'
        try : 
            mol_info = conf_gen(smi=smis[inf], conf_number=400, smi_charge=1)

            f = open(fileName, 'w')
            f.write(mol_info)
            f.close()
            os.system("mv %s fragment_pos_dup_xyz"% fileName)  
        except :
            f = open(wrong_frag_pos_smi, 'a+')
            f.write(inf)
            f.write("\n")
            f.close()


# In[21]:


start = []
for inf in range(103):
    start.append(inf*2000)
    
end = []
for inf in range(103):
    end.append(inf*2000+2000)


# In[ ]:


#end


# In[25]:


start.append(206000)
end.append(206797)


# In[ ]:


#end


# In[29]:


p = Pool(28)


# In[37]:


#genxyz(0,2000)


# In[ ]:



for i in range(104):
    p.apply_async(genxyz,args=(start[i],end[i],))
print("waiting for all subprocesses done")
p.close()
p.join()
print("All subprocess done")

