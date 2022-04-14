import os
folder = []
for inf in range(50):
    folder.append(str(inf)+ '-job')

for inf in range(50):
    os.system("./check-error.sh %s"% folder[inf])



