#full dataframes with d2D predictions using NMR chemical shifts
d2D_AT3_cs.25.sbinlab
d2D_bmr16114_3
d2D_bmr18403_3
d2D_bmr19774_3
d2D_AT3_cs.gary	
d2D_bmr17065_3
d2D_bmr19111_3
d2D_bmr27380_3
d2D_bmr19077_3
d2D_bmr16405_3
d2D_bmr18560_3


#We generated a dataframe including all the d2D predicted helical content
paste <(awk '{print $1,$2,$3}' d2D_AT3_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3_cs.gary) <(awk '{print $2,$3}' d2D_bmr27380_3) <(awk '{print $2,$3}' d2D_bmr16405_3) <(awk '{print $2,$3}' d2D_bmr16114_3) <(awk '{print $2,$3}' d2D_bmr17065_3) <(awk '{print $2,$3}'  d2D_bmr18560_3) <(awk '{print $2,$3}' d2D_bmr18403_3) <(awk '{print $2,$3}' d2D_bmr19111_3) <(awk '{print $2,$3}' d2D_bmr19077_3) <(awk '{print $2,$3}' d2D_bmr19774_3) > dataframe_all_NMR.txt

#We used as a reference the UIM motif defined by PFAM that includes 18 residues to define the UIMs of the different proteins
#We performed an aligment of the UIMs sequences by using Clustal Omega

PFAM                    MDEEEDLQRALAMSMQEM
AT3 UIM1 (Human)    223 DEDEEDLQRALALSRQEI 240
AT3 UIM2 (Human)    243 EDEEADLRRAIQLSMQGS 260
AT3 UIM3 (Human)    334 MSEEDMLQAAVTMSLETV 351
VPS27 UIM1 (E.coli) 257 EDEEELIRKAIELSLKES 274  (E257 not in the construct)
STAM1 UIM (Human)   170 KKEEEDLAKAIELSLKEQ 187
STAM2 UIM (Human)   164 NKEDEDIAKAIELSLQEQ 181
USP25 UIM1 (Human)   96 GDDKDDLQRAIALSLAES 113
USP25 UIM2 (Human)  123 TDEEQAISRVLEASIAEN 140
RAP80 UIM1 (Human)   79 MTEEEQFALALKMSEQEA  96
RAP80 UIM2 (Human)  104 EEEEELLRKAIAESLNSC 121
USP28 UIM (Human)    96 HDNKDDLQAAIALSLLES 113 


>sp|P54252|ATX3_HUMAN.UIM1
DEDEEDLQRALALSRQEI
>sp|P54252|ATX3_HUMAN.UIM2
EDEEADLRRAIQLSMQGS
>sp|P54252|ATX3_HUMAN.UIM3
MSEEDMLQAAVTMSLETV
>sp|P40343|VPS27_YEAST
EDEEELIRKAIELSLKES
>sp|Q92783|STAM1_HUMAN.UIM
KKEEEDLAKAIELSLKEQ
>sp|O75886|STAM2_HUMAN.UIM
NKEDEDIAKAIELSLQEQ
>sp|Q9UHP3|UBP25_HUMAN.UIM1
GDDKDDLQRAIALSLAES
>sp|Q9UHP3|UBP25_HUMAN.UIM2
TDEEQAISRVLEASIAEN
>sp|Q96RL1|UIMC1_HUMAN.UIM1
MTEEEQFALALKMSEQEA
>sp|Q96RL1|UIMC1_HUMAN.UIM2
EEEEELLRKAIAESLNSC
>sp|Q96RU2|UBP28_HUMAN.UIM
HDNKDDLQAAIALSLLES



#Based on the alignment we filtered the dataframes with d2D predictions to include only the values for the UIM
#the filtered d2D data are in the d2D_UIMs folder
#We generated a dataframe dataframe_UIMs_NMR.txt including the d2D predicted helical content for the UIM for the publication
#We generated a dataframe dataframe_AT3_UIMs_NMR.txt including the d2D predicted helical content for the AT-3 UIM
#We generated a dataframe dataframe_all_UIMs_NMR.txt including the d2D predicted helical content for all the UIMs 

paste <(awk '{print $1,$2,$3}' d2D_AT3_UIM1_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3_UIM2_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3_UIM3_cs.gary) <(awk '{print $2,$3}' d2D_VSP27.UIM1_bmr16114_3) <(awk '{print $2,$3}' d2D_STAM1.UIM_bmr17065_3 ) <(awk '{print $2,$3}' d2D_STAM2.UIM_bmr18403_3) <(awk '{print $2,$3}' d2D_USP25.UIM1_bmr19111_3) <(awk '{print $2,$3}' d2D_USP25.UIM2_bmr19111_3) <(awk '{print $2,$3}' d2D_USP28.UIM_bmr19077_3) <(awk '{print $2,$3}' d2D_RAP80.UIM1_bmr19774_3) <(awk '{print $2,$3}' d2D_RAP80.UIM2_bmr19774_3) > dataframe_UIMs_NMR.txt

paste <(awk '{print $1,$2,$3}' d2D_AT3_UIM1_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3.UIM1_bmr16405_3) <(awk '{print $2,$3}' d2D_AT3.UIM1_bmr27380_3) <(awk '{print $2,$3}' d2D_AT3_UIM2_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3.UIM2_bmr16405_3) <(awk '{print $2,$3}' d2D_AT3.UIM2_bmr27380_3) <(awk '{print $2,$3}' d2D_AT3_UIM3_cs.gary) <(awk '{print $2,$3}' d2D_AT3.UIM3_bmr27380_3) > dataframe_AT3_UIMs_NMR.txt

paste <(awk '{print $1,$2,$3}' d2D_AT3_UIM1_cs.25.sbinlab) <(awk '{print $2,$3}' d2D_AT3.UIM1_bmr27380_3) <(awk '{print $2,$3}' d2D_AT3_UIM2_cs.25.sbinlab)  <(awk '{print $2,$3}' d2D_AT3.UIM2_bmr27380_3) <(awk '{print $2,$3}' d2D_AT3_UIM3_cs.gary) <(awk '{print $2,$3}' d2D_AT3.UIM3_bmr27380_3) <(awk '{print $2,$3}' d2D_VSP27.UIM1_bmr16114_3) <(awk '{print $2,$3}' d2D_STAM1.UIM_bmr17065_3 ) <(awk '{print $2,$3}' d2D_STAM2.UIM_bmr18403_3) <(awk '{print $2,$3}' d2D_USP25.UIM1_bmr19111_3) <(awk '{print $2,$3}' d2D_USP25.UIM2_bmr19111_3) <(awk '{print $2,$3}' d2D_USP28.UIM_bmr19077_3) <(awk '{print $2,$3}' d2D_USP28.UIM_bmr18560_3) <(awk '{print $2,$3}' d2D_RAP80.UIM1_bmr19774_3) <(awk '{print $2,$3}' d2D_RAP80.UIM2_bmr19774_3) > dataframe_all_UIMs_NMR.txt

#We then plotted the dataframes using the R script plotting_helix_pop_UIMs.R
