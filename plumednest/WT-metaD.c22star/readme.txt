#Here we include the files to reproduce the WT-metaD simulation with the CHARMM22star force field (PMID: 21539772) with the TIPS3P (PMID: 24889800) water models associated with the publication Ubiquitin Interacting Motifs: duality between structured and disordered motifs Lambrughi, Papaleo et. al.

#These files are deposited in plumed-nest

#We copied the plumed.dat and tpr from the WT-metaD folder
cp ../../metaD/metaD.c22star.3u.1MICRO.extend.ANALYSIS/plumed.dat .
cp ../../metaD/metaD.c22star.3u.1MICRO.extend.ANALYSIS/sim.tpr .

#We converted plumed.dat in the formalism of plumed 2 in the plumed2.dat
#we tested the plumed2.dat using gromacs 5.1.2 and plumed 2.3

source /usr/local/gromacs-5.1.2_plumed-2.3b/bin/GMXRC.bash
gmx_mpi mdrun -ntomp 2  -s sim.tpr  -plumed plumed2.dat -v -cpi -maxh 0.02 
