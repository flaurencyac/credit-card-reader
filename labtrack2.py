import sys
import re
import math
hexnum = " ".join(sys.argv[1:])
hexnum = hexnum.split()

binary = list()
noParityList = list()
decoded = list()

for i in range(len(hexnum)):
    binaryString = ""
    ini_string=hexnum[i]
    res = bin(int(ini_string, 16))[2:].zfill(8)
    binaryString = res
    binary.append(binaryString)
    
binary = ''.join(map(str, binary))

binary = [binary[i:i+5] for i in range(6, len(binary), 5)]

for i in range(len(binary)):
    noParityString = binary[i][0:4]
    if i > 0:
        MSB = ''.join(reversed(noParityString))
        noParityList.append(MSB)
    else:
        noParityList.append(noParityString)

for i in range(len(noParityList)):
    if i==0:
        decoded.append("[SS]")
    if noParityList[i]=="1101":
        decoded.append("[FS]")
    if noParityList[i]=="1111":
        decoded.append("[ES]")
    if i!=0 and len(noParityList[i])==4:
        integer=int(noParityList[i],2)
        decoded.append(str(integer))
decodedString = ''.join(map(str, decoded))
print(decodedString)