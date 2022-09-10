import os
folder = []
for inf in range(50):
    folder.append(str(inf)+ '-job')
which_part = 1
for inf in range(50):
    os.system("bash generate_valence_info.sh %s %s"% folder[inf], which_part)
which_part = 2
for inf in range(50):
    os.system("bash generate_valence_info.sh %s %s"% folder[inf], which_part)



