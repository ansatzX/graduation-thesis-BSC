import os
from judgemd5 import *
folder = []
for inf in range(50):
    folder.append(str(inf)+ '-job')
f =open("diff_result_1.txt", "w")
which_part = 1
for inf in range(50):
    
    files = os.listdir(path)
    for xyz in range(inf*200, (inf+1)*200):
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
        FileName = 'molecule'+ '_'+ num 
        path="./frag-logs-/" + str(which_part) + folder[inf] + FileName
        files = os.listdir(path)
        ThisXzys = [s for s in files if s[0:15]==FileName and s[-4:]==".xyz"]
        opts =[s for s in ThisXzys if s[-9:]=="_opt_.xyz"].sort()
        origins =[s for s in ThisXzys if s[-9:]=="-1.xyz" or s[-9:]=="-2.xyz"].sort()
        for id in range(len(origins)):
            result=diff(path + origins(id), path+ opts(id))
            f.write(FileName + " " + "frag-logs-" + which_part + " " + origins(id) + " diff " + opts(id) +  str(result)+"\n")
f.close()
f =open("diff_result_2.txt", "w")
which_part = 2
for inf in range(50):
    path="./frag-logs-/" + str(which_part) + folder[inf]
    files = os.listdir(path)
    for xyz in range(inf*200, (inf+1)*200):
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
        FileName = 'molecule'+ '_'+ num 
        ThisXzys = [s for s in files if s[0:15]==FileName]
        opts =[s for s in ThisXzys if s[-9:]=="_opt_.xyz"].sort()
        origins =[s for s in ThisXzys if s[-9:]=="-1.xyz" or s[-9:]=="-2.xyz"].sort()
        for id in range(len(origins)):
            result=diff(path + origins(id), path+ opts(id))
            f.write(FileName + " " + "frag-logs-" + which_part + " " + origins(id) + " diff " + opts(id) +  str(result)+"\n")
f.close()


