#This folder contains the results by PPM, i.e. chemical shift predictions for backbone atoms and siide-chain hydrogens.
#PPM takes as input a centered PDB trajectory (alghouth PPM compensates for potential PBC defects).

#The script ppm_collector.sh assumes the presence of the executable ppm_stable in the folder
#The paths of the TPR and XTC files (from which PDBs are created) are defined at the beginning of the script ppm_collector.sh:
>> path_traj=../../../traj6_fix.xtc
>> path_tpr=../../../topol6_prot.tpr

#The script ppm_collector.sh collects the chemical shift predictions for subtrajectories of 5 ns lenght difference, 
#i.e. for 0ns, 5ns, 10ns, .... The script creates the intermediate subtrajectories and deletes them as it progresses
#in the loop. 

#The input trajectory was processed by removing the first and last residue (NH3 and COO). The line to create the index file is at the beginning of the ppm_collector.sh script. 

#To reproduce results, simply run: 
>> sh ppm_collector.sh
