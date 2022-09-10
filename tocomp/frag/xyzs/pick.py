from multiprocessing import Pool
import os
def pick(start,end,folder) :
    os.system("mkdir %s"% folder)
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

        FileName = 'molecule'+ '_'+ num 
        os.system("mkdir %s/%s"% folder, FileName)
        os.system("mv ./%s* %s/%s"% (FileName, folder, FileName) )

start = []
for inf in range(50):
    start.append(inf*200)
end = []
for inf in range(50):
    end.append(inf*200+200)
folder = []
for inf in range(200):
    folder.append(str(inf)+ '-job')

for i in range(50):
    pick(start[i],end[i],folder[i])


