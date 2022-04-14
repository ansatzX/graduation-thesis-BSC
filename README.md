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

1. pick 2w molecule fomr clean molecule csv file.
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
python pick.py

```
4. submit calc job to PBS system
```
cd ../../tocomp/mole/2w
bash precomp.sh 
python run2w.py 

```
