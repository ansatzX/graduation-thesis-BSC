import os
with open("makefile", "a+") as f:
    f.write("bindir=/export/home/wjzhang/gcx/data/biyesheji\n")

with open("makefile", "a+") as f:
    f.write("all:")
for inf in range(50):
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
    baseName = 'ymzxm' + num
    with open("makefile","a+") as f:
        f.write("\t%s\t"% baseName)
    if ( inf % 20 ==0):
        with open("makefile","a+") as f:
            f.write("\\\n")


for inf in range(50):
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
    baseName = 'ymzxm' + num
    xyzName = 'molecule'+ '_'+ num + '.xyz'
    insName = 'I_' + num + '.ins'
    with open("makefile","a+") as f:
        f.write("\n%s\t:\n"% baseName)
        f.write("\t${bindir}/runsepxyz.sh\t%s\t%s\n"% (xyzName,insName))


