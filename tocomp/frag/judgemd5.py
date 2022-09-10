from hashlib import md5
import sys
def Gen_MD5(file):
    m =md5()
    with open(file, "r") as f:
        m.update(f.read().encode("utf-8"))
    return m.hexdigest()
file1 = "/home/ubuntu/data/graduation-thesis-BSC/tocomp/frag/tmp/xtblog"
file2 = "/home/ubuntu/data/graduation-thesis-BSC/tocomp/frag/tmp/xtblog1"
def diff(file1, file2):
    m1 = Gen_MD5(file1)
    m2 = Gen_MD5(file2)
    if m1 == m2 :
        return True
    else:
        return False

if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    print(diff(file1, file2))