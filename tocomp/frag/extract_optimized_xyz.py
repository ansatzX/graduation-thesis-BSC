import sys, os
from rdkit import Chem
import re
PTDic = dict((str(i), Chem.PeriodicTable.GetElementSymbol(Chem.GetPeriodicTable(),i)) for i in range(1,119))

def match_coord(string):
    centNumList = []
    coordObj = re.findall(r'^\s+(\d+)\s+(\d+)\s+\d\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)$', string, flags=re.M)
    if coordObj is not None:
        for centNum in coordObj:
            centNumList.append(eval(centNum[0]))
        # for coord in coordObj[-max(centNumList):]:
        #     f2.write(PTDic[coord[1]] + "\t" + coord[2].rjust(12) + '\t' + coord[3].rjust(12) + "\t" + coord[4].rjust(12)+"\n")
        #     print(PTDic[coord[1]] + "\t" + coord[2].rjust(12) + '\t' + coord[3].rjust(12) + "\t" + coord[4].rjust(12))
        return len(coordObj[-max(centNumList):]), coordObj[-max(centNumList):] 
    else:
        f2.write("Match Coordinates Error"+"\n")
        print("Match Coordinates Error")

FileName = sys.argv[1]
f = open(FileName, 'r')
s = f.read()
words = FileName.split("/")
path = ''
if len(words) != 1:
    words = words[:-1]
    for i in words:
        path = os.path.join(path, i)
if FileName[0] == "/":
    path = "/" + path
XyzName = os.path.join(path, words[-1].split('.')[-2]+"_opt_.xyz") 

if re.search(r'\s+Normal termination of Gaussian', s, flags=re.M) is not None:
    with open(XyzName,"w") as f2 :
        Atom_Num, coords = match_coord(s)
        f2.write(str(Atom_Num)+"\n")
        f2.write("logname : "+FileName.split('\\')[-1].split('.')[0]+"\n")

        for coord in coords:
            f2.write(PTDic[coord[1]] + "\t" + coord[2].rjust(12) + '\t' + coord[3].rjust(12) + "\t" + coord[4].rjust(12)+"\n")
        f2.write("\n")
