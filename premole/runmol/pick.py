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

        fileName = 'molecule'+ '_'+ num + '.xyz'
        os.system("cp ../mole_2w/%s %s"% (fileName, folder) )

start = []
for inf in range(50):
    start.append(inf*40)

end = []
for inf in range(50):
    end.append(inf*40+40)
folder = []
for inf in range(50):
    folder.append(str(inf)+ '-job')

p = Pool(28)

for i in range(50):
    p.apply_async(pick,args=(start[i],end[i],folder[i]))
print("waiting for all subprocesses done")
p.close()
p.join()
print("All subprocess done")

