#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 08:51:38 2021

@author: Matteo Lambrughi
"""

import getopt
import sys
import os
 
def main(argv):   
    pdbFileName = ""
    shiftyFileName = ""
    try:
        opts, args = getopt.getopt(argv,"hp:o:",["pdb=","out="])
    except getopt.GetoptError:
        print ('str2shifty.py -p <pdbFileName> -o <shiftyfilename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('str2shifty.py -p <pdbFileName> -o <shiftyfilename>')
            sys.exit()
        elif opt in ("-p", "--str"):
            pdbFileName = arg
        elif opt in ("-o", "--out"):
            shiftyFileName = arg
    
    residueNames = extractAndShortResidueNamesFromPDB(pdbFileName)
    residueMatrix = residueNames2Matrix(residueNames)
    
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = [f for f in files if '.dat' in f]
    while files != []:
        current = files.pop()
        upper = ''.join(c for c in current if c.isupper())
        cI = lookupSTRSHIFTY(upper)
        
#        with open(current,'r') as c:
#            for idx, l in enumerate(c):
#                l = l.split()
#                #if idx is not l[0]-1 -> a value is missing
#                if(idx != int(l[0].replace('#',''))-1):
#                    residueMatrix[idx][cI] = 0
#                    nJ = nJ + 1
#                residueMatrix[idx+nJ][cI] = l[1]
        c = 0
        with open(current,'r') as currentF:
            for l in currentF:
                l = l.replace('#','').split()
                #JUMP IN THE FILE
                if(c != int(l[0])-1):
                    residueMatrix[c][cI] = 0
                    c = c + 1
                residueMatrix[c][cI] = l[1]
                c = c + 1
                
                    
    toShiftyFile(residueMatrix,shiftyFileName)
        
def toShiftyFile(matrix,shiftyFileName):
    print("-----------------------------------TOFILE----------------------------")
    with open(shiftyFileName,'w+') as f:
        #write index line
        f.write("#NUM AA HA CA CB CO N HN \n")
        #write data
        for idx, l in enumerate(matrix):
            l.insert(0,idx+1)
            l.append("\n")
            listToStr = ' '.join(map(str, l))
            print(listToStr)
            f.write(listToStr)
    return 0   
    
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
    


def extractAndShortResidueNamesFromPDB(pdbFileName):
    resNames = []
    singletons = []
    with open(pdbFileName,'r') as s:
        for line in s:
            #start taking names when ATOM in line
            if 'ATOM' in line:
                splitLine = line.split()
                print("PROCESSING line -->\"{0}\"<-- for residue names".format(line.rstrip()))
                resName = lookup(splitLine[3])
                t = [resName,splitLine[4]]
                if t in singletons:
                    print(" ---- SKIPPED {0} already present".format(t))
                else:
                    print("\n ++++ ADDED {0} \n".format(t))
                    singletons.append(t) 
                    resNames.append(resName)
    
    return resNames

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
