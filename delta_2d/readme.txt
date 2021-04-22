We converted the BMRB entries from NMR-STAR v3 format to SHIFTY format using the python script str2shifty.py

python3 str2shifty.py -s ../bmrb/bmr16114_3.str -o bmr16114_3.shifty
python3 str2shifty.py -s ../bmrb/bmr16405_3.str -o bmr16405_3.shifty
python3 str2shifty.py -s ../bmrb/bmr17065_3.str -o bmr17065_3.shifty
python3 str2shifty.py -s ../bmrb/bmr18185_3.str -o bmr18185_3.shifty
python3 str2shifty.py -s ../bmrb/bmr18403_3.str -o bmr18403_3.shifty
python3 str2shifty.py -s ../bmrb/bmr18560_3.str -o bmr18560_3.shifty
python3 str2shifty.py -s ../bmrb/bmr19077_3.str -o bmr19077_3.shifty
python3 str2shifty.py -s ../bmrb/bmr19111_3.str -o bmr19111_3.shifty
python3 str2shifty.py -s ../bmrb/bmr19774_3.str -o bmr19774_3.shifty
python3 str2shifty.py -s ../bmrb/bmr27380_3.str -o bmr27380_3.shifty

We converted the cs.25.sbinlab  cs_gary dataset to SHIFTY format using the script
cp ../cs.25.sbinlab/*.dat .
cp ../cs.25.sbinlab/*.pdb .
python3 str2shiftySeparatedFiles.py -p AT3_3UIM_model_4C.B99990007.pdb -o AT3_cs.25.sbinlab.shifty
rm *.dat *.pdb

cp ../cs_gary/*.dat .
cp ../cs_gary/*.pdb .
python3 str2shiftySeparatedFiles.py -p template.pdb -o AT3_cs.gary.shifty
rm *.dat *.pdb

We used the output files in the SHIFTY format to the δ2D webserver at http://www-cohsoftware.ch.cam.ac.uk/index.php/d2D
The output from δ2D webserver are included in the d2D folder

We didn't use the entry bmr18185_3.str since it includes only the Backbone 1H and 15N Chemical Shift Assignments of the VHS-UIM domains of STAM2 so d2D gives no predictions
