import os
folder = []
for inf in range(10,20):
    folder.append(str(inf)+ '-job')

for inf in range(10):
    os.system("./subzzsc %s"% folder[inf])



