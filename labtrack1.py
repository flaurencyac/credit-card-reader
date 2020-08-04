import sys
import re
import math
hexnum = " ".join(sys.argv[1:])
hexnum = hexnum.split()

binary = list()
noParityList = list()
decoded = list()

#makes a binary list

for i in range(len(hexnum)):
    binaryString = ""
    ini_string=hexnum[i]
    res = bin(int(ini_string, 16))[2:].zfill(8)
    binaryString = res
    binary.append(binaryString)
#converts each hex # into binary and appends to the binary list of strings

binary = ''.join(map(str, binary))
#concatentates the entire list of strings into one string

binary = [binary[i:i+7] for i in range(0, len(binary), 7)]
#divides the binary into 7 bit blocks and makes a list of 7-bits strings
    
decoder = {
    "111110":"[ES][LRC]",
    "011111":"[FS]",
    "100100":"[LRC]",
    "100000":"a", 
    "010000":"a",
    "110000":"c",
    "011000":"a",
    "111000":"a",
    "001000":"$",
    "000100":"(",
    "100100":")",
    "101100":"--",
    "011100":".",
    "111100":"/",
    "000010":"0",
    "100010":"1",
    "010010":"2",
    "110010":"3",
    "001010":"4",
    "101010":"5", 
    "011010":"6", 
    "111010":"7", 
    "000110":"8", 
    "100110":"9", 
    "100001":'A',
    "010001":'B',
    "110001":'C',
    "001001":'D',
    "101001":'E',
    "011001":'F',
    "111001":'G',
    "000101":'H',
    "100101":'I',
    "010101":'J',
    "110101":'K',
    "001101":'L',
    "101101":'M',
    "011101":'N',
    "111101":'O', 
    "000011":"P", 
    "100011":"Q", 
    "010011":"R", 
    "110011":"S",
    "001011":"T",
    "101011":"U", 
    "011011":"V", 
    "111011":"W", 
    "000111":"X", 
    "100111":"Y",
    "010111":"Z"   
}


for i in range(len(binary)):
    noParityString = binary[i][0:6]
    noParityList.append(noParityString)
#creates list of binary 6-bits without parity attached to end
    
for i in range(len(noParityList)):
    if noParityList[i]=="000000" and i==0:
        decoded.append("[SS]")
    if noParityList[i] in decoder and i!=0:
        character = decoder[noParityList[i]]
        decoded.append(character)
decodedString = ''.join(map(str, decoded))
print(decodedString)

#and noParityList[i]!="000000"
#don't forget the parity bit! that's why none of it matches the keys
