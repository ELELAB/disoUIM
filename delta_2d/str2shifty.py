#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 08:51:38 2021

@author: lambda
"""

import getopt
import sys
 
def main(argv):   
    strFileName = ""
    shiftyFileName = ""
    try:
        opts, args = getopt.getopt(argv,"hs:o:",["str=","out="])
    except getopt.GetoptError:
        print ('str2shifty.py -s <strFile> -o <shiftyfilename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('str2shifty.py -s <strFile> -o <shiftyfilename>')
            sys.exit()
        elif opt in ("-s", "--str"):
            strFileName = arg
        elif opt in ("-o", "--out"):
            shiftyFileName = arg
    
    residueNames,valuesLines = extractAndShortResidueNamesFromSTR(strFileName)
    residueMatrix = residueNames2Matrix(residueNames)
    residueMatrix = processValueLines(residueMatrix,valuesLines)
    toShiftyFile(residueMatrix,shiftyFileName)

def toShiftyFile(matrix,fname):
    with open(fname,'w+') as f:
        #write index line
        f.write("#NUM AA HA CA CB CO N HN \n")
        #write data
        for idx, l in enumerate(matrix):
            l.insert(0,idx+1)
            l.append("\n")
            listToStr = ' '.join(map(str, l))
            print("WRITING TO FILE ------ {0}".format(listToStr))
            f.write(listToStr)
    return 0
        
def processValueLines(matrix, lines):
    
    for l in lines:
        splitl = l.rstrip().split()
        print(l)
        print(splitl)
        #row index @ col 4-5
        #res name @ col 6
        #col index @ col 7
        #val @ col 10
        try:
            columnI = lookupSTRSHIFTY(splitl[7])
        except:
            print("failed on line {0}, \n splitline {1}".format(l,splitl))
            
        rowI = int(splitl[4]) -1
        value = splitl[10]
        #check if lookup gave error
        if columnI != -1:
            matrix[rowI][columnI] = value
#            print ("SET -------> matrix row {0} @ position {1} with val {2}".format(matrix[rowI],columnI,value))
#            print ("NEW ROW  --> {0}".format(matrix[rowI]))
#            print ("-------------------------------------------------------------------------------------")
        
    return matrix

def lookupSTRSHIFTY(i):
    index = -1
    # Dictionary to convert three-letters residue names 
    # to one-letter names
    str2shifty = {
         "AA"  : "AA" , "HA" : "HA",
         "HA2" : "HA" , "CA" : "CA",
         "CB"  : "CB" , "C"  : "CO",
         "N"   : "N"  , "H"  : "HN"}
    
    shiftyIndex = ["AA","HA","CA","CB","CO","N","HN"]
    if i in str2shifty:
        index = shiftyIndex.index(str2shifty[i])
#        print("STR {0} into SHIFTY {1} @ index {2}".format(i,str2shifty[i],index))
#    else:
#        print ("-------------------------------------------------------------------------------------")
#        print("WARNING -> {0} NOT INTO str2shifty conversion, skipping line".format(i))
#        print ("-------------------------------------------------------------------------------------")
        
    return index

def residueNames2Matrix(residueNames):
    matrix = []
    for r in residueNames:
        matrix.append([r,'0.0','0.0','0.0','0.0','0.0','0.0'])
    return matrix
         

def extractAndShortResidueNamesFromSTR(strFile):
    resNames = []
    namesFlag = False
    valuesFlag = False
    valueLines = []
    
    with open(strFile,'r') as s:
        for line in s:
            #start taking names when find _Entity_comp_index.Entity_ID 
            if '_Entity_comp_index.Entity_ID' in line:
                namesFlag = True
            #stop taking names when find stop_    
            if 'stop_' in line and namesFlag:
                namesFlag = False
            
            #start taking values whenfind _Atom_chem_shift.Assigned_chem_shift_list_ID
            if '_Atom_chem_shift.Assigned_chem_shift_list_ID' in line:
                valuesFlag = True
            #stop taking values when find stop_    
            if 'stop_' in line and valuesFlag:
                valuesFlag = False
            
            #checking if i have to take names 
            #AND 
            #if splitline length is > 1 (removes blank lines, start line and stop line)
            splitLine = line.split()
            if namesFlag and  len(splitLine) > 1:
                #print("processing line {0} for residue names".format(line.rstrip()))
                resName = lookup(splitLine[2])
                resNames.append(resName)
                #print("converted {0} -> {1}".format(splitLine[2],resName))
                #print("---------------------------------")
            
            if valuesFlag and len(splitLine) > 1:
                #print("processing line {0} for residue values".format(line.rstrip()))
                #print("{0}".format(splitLine))
                #print("---------------------------------")
                valueLines.append(line.rstrip())

    return resNames, valueLines

def lookup(resNameLong):
    
    # Dictionary to convert three-letters residue names 
    # to one-letter names
    three2one = {"ALA" : "A", "ARG" : "R", \
             "ASN" : "N", "ASP" : "D", \
             "CYS" : "C", "GLY" : "G", \
             "GLU" : "E", "GLN" : "Q", \
             "HIS" : "H", "ILE" : "I", \
             "LEU" : "L", "LYS" : "K", \
             "MET" : "M", "PHE" : "F", \
             "PRO" : "P", "SER" : "S", \
             "THR" : "T", "TRP" : "W", \
             "TYR" : "Y", "VAL" : "V"}
       
    return three2one[resNameLong]

if __name__ == "__main__":
    main(sys.argv[1:])