import pandas as pd 
import numpy as np 
import os
from rdkit import Chem
from rdkit.Chem import AllChem

rawdata1=pd.read_csv("../premole/mole_dup.csv")
rawdata2=pd.read_csv("../premole/rdf_data_190531.csv")
data1= rawdata1.to_numpy()
data2 =rawdata2.to_numpy()

# mole but different index one sorted duped another orign
smis_mole = data1[:,0]
orign_mole = data2[:,1]
orign_frag1 = data2[:,3]
orign_frag2 = data2[:,4]
index =[]


def get_orign_index(smi):
    '''
     source should be numpy array
     smi should be string
    '''
    index = np.argwhere(orign_mole==smi)
    print("get index of your smile")
    return index

def pre_mole(smi):
    '''
    transfer smi to mol and AddHs
    '''
    m = Chem.MolFromSmiles(smi)
    m =Chem.AddHs(m)
    print("pre mole")
    return m
    
def pre_frag(single_index):
    '''
    get frags by index 
    transfer smiles -> mol -> smarts -> mol
    it can be user to search but not AddHs
    '''
    frag1 = orign_frag1[single_index]
    frag2 = orign_frag2[single_index]
    
    m_1 = Chem.MolFromSmarts(Chem.MolToSmarts(Chem.MolFromSmiles(frag1))) 
    m_2 = Chem.MolFromSmarts(Chem.MolToSmarts(Chem.MolFromSmiles(frag2))) 
    print("pre frag")
    return frag1, frag2, m_1, m_2
    
def get_linkage_hydrogen_idx(mol,atomidx):
    '''
    get all Hs on specific atom of molecule
    '''
    other_atom_lists =[]
    # try each bond and fetch H
    for i in range(len(mol.GetAtomWithIdx(atomidx).GetBonds())):
        other_atom = mol.GetAtomWithIdx(atomidx).GetBonds()[i].GetEndAtom()
        other_atom_symbol = other_atom.GetSymbol()
        if other_atom_symbol != 'H':
            other_atom = mol.GetAtomWithIdx(atomidx).GetBonds()[i].GetBeginAtom()    
            other_atom_symbol = other_atom.GetSymbol()
        if other_atom_symbol != 'H':   
            continue

        other_atom_idx = other_atom.GetIdx()
        other_atom_lists.append(other_atom_idx)
        #print("get your h on this atom %s"% atomidx)
    return other_atom_lists
def get_linkage_hydrogen_num(mol,atomidx):
    '''
    get all Hs on specific atom of molecule
    '''
    hs_num =0
    # try each bond and fetch H
    for i in range(len(mol.GetAtomWithIdx(atomidx).GetBonds())):
        other_atom = mol.GetAtomWithIdx(atomidx).GetBonds()[i].GetEndAtom()
        other_atom_symbol = other_atom.GetSymbol()
        if other_atom_symbol != 'H':
            other_atom = mol.GetAtomWithIdx(atomidx).GetBonds()[i].GetBeginAtom()    
            other_atom_symbol = other_atom.GetSymbol()
        if other_atom_symbol != 'H':   
            continue
        hs_num = hs_num + 1
        #print("get your h on this atom %s"% atomidx)
    return hs_num


def get_frag_atomindex_pro(smi):
    '''
    from a specific smiles to a seqence of frags atomindex
    return atoms and use lists 
    use for which frags
    atoms for this frag's atomindex 
    '''
    mol = pre_mole(smi)
    frag_index = get_orign_index(smi)
    unsaturated_atom ='0'
    atomids =[]

    atoms =[]
    who = []
    for i in frag_index:
        atomlists =[]
        frag1, frag2, mol_1, mol_2 = pre_frag(int(i))
        if '[H]'  not in [frag1,frag2]:
            
            use = 0
            if len(frag1) > len(frag2) :
                use = 1
                is_match =mol.HasSubstructMatch(mol_1)
            else :
                use = 2
                is_match =mol.HasSubstructMatch(mol_2)
            if is_match :
                if use == 1 :
                    atomids = mol.GetSubstructMatch(mol_1)
                else :
                    atomids = mol.GetSubstructMatch(mol_2)
            
            else :
                print("nothing match")
            for atom in atomids:
                atomlists.append(atom)


            for j in atomids:
                addHs = get_linkage_hydrogen_idx(mol,j)
                for H in addHs:
                    atomlists.append(H)
        else :
            if frag1 == '[H]':
                use = 2
                mol_H =Chem.MolFromSmiles(frag2)
                
            else :
                use = 1
                mol_H =Chem.MolFromSmiles(frag1)
            #if  not h use it to fetch
            # can't match but we can find unsaturated atom
            atomids =[]
            saturated_atoms =[]
            for atom in range(mol_H.GetNumAtoms()):
                atomids.append(atom)
                atomlists.append(atom)
                saturated_atoms.append(atom)
            # just do it

            for j in range(mol_H.GetNumAtoms()):
                # try each atom but H
                print(i,j,use)
                atom =mol_H.GetAtomWithIdx(j)
                # pick atom
                bonds = atom.GetTotalValence()
                symbol = atom.GetSymbol()
                # infomation of this atom

                
                if symbol == 'C' and bonds == 3:
                    unsaturated_atom = atomids[j]
                    # if  then  mark it 
                    saturated_atoms.remove(unsaturated_atom)
                    break
                if symbol == 'N' and bonds == 2:
                    unsaturated_atom = atomids[j]
                    saturated_atoms.remove(unsaturated_atom)
                    break
                if symbol == 'O' and bonds == 1:
                    unsaturated_atom = atomids[j]
                    saturated_atoms.remove(unsaturated_atom)
                    break
            #index of frags --mapping entire molecule's index 
            ua_mol = get_linkage_hydrogen_num(mol, unsaturated_atom)
            ua_mol_H = get_linkage_hydrogen_num(mol_H, unsaturated_atom)
            print("unsaturated_atom",unsaturated_atom)
            if ua_mol == ua_mol_H:
                atom_sametype = []
                for atomidx in saturated_atoms:
                    atom =mol_H.GetAtomWithIdx(atomidx)
                    if atom.GetSymbol() == symbol:
                        atom_sametype.append(atomidx)
                    # get same type atoms

                for idx in atom_sametype:
                    tmp = get_linkage_hydrogen_num(mol, idx)
                    if (tmp -1)== ua_mol_H:
                        atom_lower1H=idx
                        print(idx)
                saturated_atoms.append(unsaturated_atom)
                unsaturated_atom =atom_lower1H
                saturated_atoms.remove(unsaturated_atom)
        
            for k in saturated_atoms:
                addHs = get_linkage_hydrogen_idx(mol,k)
                for H in addHs:
                    atomlists.append(H)
            unsaturated_Hs = get_linkage_hydrogen_idx(mol,int(unsaturated_atom))
            if len(unsaturated_Hs) != 0:
                unsaturated_Hs.pop()
            for H in unsaturated_Hs:
                atomlists.append(H)
            # add Hs    
       

        atoms.append(atomlists)
        who.append(use)
    return atoms, who

def create_instruction(filename,smi):
    atoms ,who =get_frag_atomindex_pro(smi)
    with open(filename,"w") as f:
        for i in range(len(who)):
            f.write(str(who[i]))
            f.write("\n")
            for j in atoms[i]:
                f.write(str(j))
                f.write(" ")
            f.write("\n")    
for inf in range(20000):
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

    FileName =  'I_'+num + '.ins'
    create_instruction(FileName,smis_mole[inf])
    os.system("mv %s INS"% FileName)