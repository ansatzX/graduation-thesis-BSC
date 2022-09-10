import os
folder = []
for inf in range(50):
    folder.append(str(inf)+ '-job')
which_part = 1
for inf in range(50):
    cmd = "for inf in $(ls frag-logs-%s/%s/mole*);do\n" % (which_part, folder[inf]) + \
    "   for jnf in $(ls ${inf}/*.log);do\n" + \
    "       python extract_optimized_xyz.py $jnf\n" + \
    "   done\n" + \
    "done\n"
    os.system(cmd)
which_part = 2
for inf in range(50):
    cmd = "for inf in $(ls frag-logs-%s/%s/mole*);do\n" % (which_part, folder[inf]) + \
    "   for jnf in $(ls ${inf}/*.log);do\n" + \
    "       python extract_optimized_xyz.py $jnf\n" + \
    "   done\n" + \
    "done\n"
    os.system(cmd)