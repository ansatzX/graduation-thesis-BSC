mkdir xyzs
mkdir logs
cp -r ../../../premole/runmol/* ./xyzs 
gfortran extorca.f90 -o extorca
chmod +x orca.sh
chmod +x xtbmd.sh
