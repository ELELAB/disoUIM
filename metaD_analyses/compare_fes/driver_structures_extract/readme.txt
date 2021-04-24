We here calculated the rmsd of the mainchain atoms of the AT-3 UIM3 region including residues E336-T350 to the starting structure of the REMD (i.e. with the UIM3 as fully helical conformation) and experimental structures of bound UIMs
We performed this analysis on the metad with charmm22star-tips3p
#For the AT-3 UIM3 we used for the alignment and the calculations the heavy atoms of residue E336-T350 and the side chain heavy atoms of A343
#For the 1Q0W Solution structure of Vps27 amino-terminal UIM-ubiquitin complex we used for the alignment and the calculations the heavy atoms of residue E259-E273 and the side chain heavy atoms of A266
#For the 1YX5 Solution Structure of S5a UIM-1/Ubiquitin Complex we used for the alignment and the calculations the heavy atoms of residue A212-E226 and the side chain heavy atoms of A219
#For the 1YX6 Solution Structure of S5a UIM-2/Ubiquitin Complex we used for the alignment and the calculations the heavy atoms of residue E283-G297 and the side chain heavy atoms of A290
#For the 3A1Q Crystal structure of the mouse RAP80 UIMs in complex with Lys63-linked di-ubiquitin UIM1 we used for the alignment and the calculations the heavy atoms of residue E81-E95 and the side chain heavy atoms of A88


#We calculated the alignment and the rmsd by an in-house python scripts using MDAnalysis, matplotlib, and pandas toolkits
#We extracted conformations from metad using driver2.3 in plumed2.3

#################STEPS######################
#concatenate the two parts of the traj metad charmm22star-tips3p
gmx_mpi trjcat -f ../../metaD.c22star.3u.1MICRO.extend.ANALYSIS/traj.xtc ../../extended/restart.c22s/traj.xtc -o traj_c22s.xtc -settime <<eof
0
c
eof

#filter the concatenated traj to include only the protein
gmx_mpi trjconv -f traj_c22s.xtc -s ../../metaD.c22star.3u.1MICRO.extend.ANALYSIS/sim.tpr -o traj_c22s.prot.xtc <<eof
1
eof

#create an index with mainchain atoms and CB of conserved A in the UIM3
gmx_mpi make_ndx -f ../../extended/restart.c22s/sim.tpr  -o index.3UIM.ndx <<eof
a N CA C O
r 31-45
19 & 20
r 38 & a CB
21 | 22
q
eof

#create a reference pdb file for driver2.3
gmx_mpi trjconv -f traj_c22s.prot.xtc  -s ../../extended/restart.c22s/sim.tpr -o reference.pdb -n index.3UIM.ndx -b 0 -e 0 <<eof
1
eof

#The metaD has been performed with plumed1.3 but driver1.3 gives unsolvable errors so we converted the plumed.dat used from 
#plumed1 format to plumed2 format and used driver2 to extract conformations
#In the folder comparison_plumed1_plumed2 we calculated the alphabeta on the traj_c22s.prot.xtc using plumed2 and saved the values in the COLVAR file. We then compared in the folder ../analysis_COLVAR the COLVAR generated with plumed2 with the original COLVAR generated with plumed1.3. The distribution of the values are nearly identical.
#We selected ranges of alphabeta values and extract conformations with driver2
#We here selected four windows of values defined from visual observations of the 1D FES of alphabeta: I 9-17, II 18-23, III 24-30, IV 31-34
/usr/local/plumed-2.3b/bin/plumed driver --mf_xtc traj_c22s.prot.xtc --plumed plumed.I.dat
/usr/local/plumed-2.3b/bin/plumed driver --mf_xtc traj_c22s.prot.xtc --plumed plumed.II.dat
/usr/local/plumed-2.3b/bin/plumed driver --mf_xtc traj_c22s.prot.xtc --plumed plumed.III.dat
/usr/local/plumed-2.3b/bin/plumed driver --mf_xtc traj_c22s.prot.xtc --plumed plumed.IV.dat

#we converted the gro outputs of driver2 in pdb and filtered them to keep only the UIM3
gmx_mpi trjconv -f fileI.gro -s fileI.gro -o outI.pdb -n index.3UIM.ndx <<eof
23
eof
gmx_mpi trjconv -f fileII.gro -s fileII.gro -o outII.pdb -n index.3UIM.ndx <<eof
23
eof
gmx_mpi trjconv -f fileIII.gro -s fileIII.gro -o outIII.pdb -n index.3UIM.ndx <<eof
23
eof
gmx_mpi trjconv -f fileIV.gro -s fileIV.gro -o outIV.pdb -n index.3UIM.ndx <<eof
23
eof

#We calculated RMSD to AT-3 UIM3 fully-helical starting model for the REMD simulations
cp ../../../remd/AT3_3UIM_model1.B99990004.pdb .

gmx_mpi make_ndx -f AT3_3UIM_model1.B99990004.pdb -o index.AT3.ndx  <<eof
a N CA C O
ri 31-45
10 & 11
ri 38 & a CB
12 | 13
q
eof

#we filtered the pdb
gmx_mpi trjconv -f AT3_3UIM_model1.B99990004.pdb -s AT3_3UIM_model1.B99990004.pdb -o AT3_3UIM_model1.B99990004_filt.pdb -n index.AT3.ndx <<eof
14
eof

#we run the script for analysis of rmsd and plotting
python3 rmsd_AT3.I.py
python3 rmsd_AT3.II.py
python3 rmsd_AT3.III.py
python3 rmsd_AT3.IV.py


###############
#Comparison to experimental structures of UIMs bound to Ub
#We here compared only conformations extracted from the range IV including conformations with values of alaphabeta between 31 and 34

mkdir comparison_to_ub.bound
cd comparison_to_ub.bound

cp ../outIV.pdb .
##############################
#analysis for rmsd to 1Q0W
cp ../../../../pdbs/pdbs_processed/split_chain/1Q0W_clean_AB.pdb .

gmx_mpi make_ndx -f 1Q0W_clean_AB.pdb -o index.1Q0W.ndx  <<eof
a N CA C O
r 259-273
10 & 11
r 266 & a CB
12 | 13
q
eof

#filter the pdb
gmx_mpi trjconv -f 1Q0W_clean_AB.pdb -s 1Q0W_clean_AB.pdb -o 1Q0W_clean_AB_filt.pdb -n index.1Q0W.ndx <<eof
14
eof

#run the script for analysis of rmsd and plotting
python3 rmsd_1q0w.IV.py

##############################
#analysis for rmsd to 1YX5
cp ../../../../pdbs/pdbs_processed/split_chain/1YX5_clean_AB.pdb .

gmx_mpi make_ndx -f 1YX5_clean_AB.pdb -o index.1YX5.ndx  <<eof
a N CA C O
ri 18-32
10 & 11
ri 25 & a CB
12 | 13
q
eof

#filter the pdb
gmx_mpi trjconv -f 1YX5_clean_AB.pdb -s 1YX5_clean_AB.pdb -o 1YX5_clean_AB_filt.pdb -n index.1YX5.ndx <<eof
14
eof

#run the script for analysis of rmsd and plotting
python3 rmsd_1yx5.IV.py

##############################
#analysis for rmsd to 1YX6
cp ../../../../pdbs/pdbs_processed/split_chain/1YX6_clean_AB.pdb .

gmx_mpi make_ndx -f 1YX6_clean_AB.pdb -o index.1YX6.ndx  <<eof
a N CA C O
ri 89-103
10 & 11
ri 96 & a CB
12 | 13
q
eof

#filter the pdb
gmx_mpi trjconv -f 1YX6_clean_AB.pdb -s 1YX6_clean_AB.pdb -o 1YX6_clean_AB_filt.pdb -n index.1YX6.ndx <<eof
14
eof

#run the script for analysis of rmsd and plotting
python3 rmsd_1yx6.IV.py

##############################
#analysis for rmsd to 3A1Q
cp ../../../../pdbs/pdbs_processed/split_chain/3A1Q_clean_ABC.pdb .

gmx_mpi make_ndx -f 3A1Q_clean_ABC.pdb -o index.3A1Q.ndx  <<eof
a N CA C O
ri 154-168
10 & 11
ri 161 & a CB
12 | 13
q
eof

#filter the pdb
gmx_mpi trjconv -f 3A1Q_clean_ABC.pdb -s 3A1Q_clean_ABC.pdb -o 3A1Q_clean_ABC_filt.pdb -n index.3A1Q.ndx <<eof
14
eof

#run the script for analysis of rmsd and plotting
python3 rmsd_3a1q.IV.py

#we prepared the final panels in pymol showing
#frame 147  of AT3 3UIM for 1Q0W saved in the session 1Q0W.pse
#frame 167 of AT3 3UIM for 1YX5 saved in the session 1YX5.pse
#frame 164 of AT3 3UIM for 1YX6 saved in the session 1YX6.pse
#frame 147 of AT3 3UIM for 3A1Q saved in the session 3A1Q.pse
