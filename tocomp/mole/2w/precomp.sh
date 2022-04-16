mkdir xyzs
mkdir logs
cp -r ../../../premole/runmol/*-job ./xyzs 
gfortran extorca.f90 -o extorca
chmod +x orca.sh
chmod +x xtbmd.sh
chmod +x orca.sh-zzssc
