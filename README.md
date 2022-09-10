# 郑州大学本科生毕业论文项目
## 有机化学键能和反应数据库的建设
### 课题依据、现状和意义
催化大数据方向主要运用大数据机器学习研究化学反应结构与催化剂性能分析，开发具有高应用价值的催化反应路线。

近年来化学大数据越来越受到化学家的重视，尤其在机器学习领域。

Palton等人通过高精度量化计算构建了均裂键能数据库，并提出了基于图神经网络机器学习模型，能够有效预测键能。

本项目将建设更多的化学数据库，为今后的提出高精度机器学习模型打下基础。
### 主要研究内容和目标

研究内容：从少于9个重原子的化合物中，通过SMILE字符串构建初始立体构象，使用高精度的量化计算，建立化学键异裂键能数据库，自由基氢提取反应、自由基加成反应数据库。

研究目标：化学键异裂键能数据库、自由基反应数据库超过1万条有效数据。

1. Pick 2w molecule from clean molecule csv file.
```
cd premole
python pick2w_mole.py 
```
2. Generate suitable conformer for smiles strings. Store it to a standalone xyz file. 
```
python comp_mole_2w.py

```
3. Divide 2w xyzs to some folders 
```
cd runmol
python pick.py # then pack files to workspace

```
4. Submit calc job to PBS system
```
cd ../../tocomp/mole/
bash precomp.sh 
python run1w.py 

```
5. Check results and work on errors
```
python runcheck.py
ls Error-*  # fix all errors and collect all xyzs tp xyzs folder

```
6. Generate suitable conformer from optimized conformer. Store it to a standalone xyz file.
```
cd ../../prefrag
mkdir INS frag-xyz tmp optxyzs # notice you need put all conformer-optimized xyz files to a folder called "optxyzs"
python split_mole.py # generate instruction files
python genmake.py # run bash script to spilt molecule
make -jN   # N for your core number

```
7. Submit calc job to PBS system
```
cd ../tocomp/frag/
mkdir frag-logs-1 frag-logs-2  xyzs tmp # will receive results store spilt xyz files
python run1w-opt.py


```
8. Check results and work on errors
```
cp check-error.sh ./frag-logs-1
cp check-error.sh ./frag-logs-2
cp runcheck.py ./frag-logs-1
cp runcheck.py ./frag-logs-2
cd frag-logs-1
mkdir worksapce
python runcheck.py
ls Error-*
cd ../frag-logs-2
mkdir worksapce
python runcheck.py
ls Error-*

```
9. Check Topology by xTB WBO 
```
python run_extract_optimized_xyz.py # extract opted xyz files in same folders
python run1w_valence_info.py
python run1w_judge_pick.py

```
10. Do SP Jobs
```
python run1w-sp.py # do SP calc  

```
11. Collect Results
```
cp diff_result_1.txt ../../results
cp diff_result_2.txt ../../results
cd ../../
mv tocomp/mole/logs ./results/mole-logs
mv tocomp/frag/frag-logs-1 ./results
mv tocomp/frag/frag-logs-2 ./results 

```
12. Using scripts to get data from raw files and generate hdf5 file.
```
to do
```

