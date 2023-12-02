# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:38:42 2023

@author: Johannes
"""

def FirstNumber(sInput):
    i=0
    for i in range(len(sInput)):
        if sInput[i].isdigit() == True:
            return sInput[i]
        else:
            pass

def LastNumber(sInput):
    i=len(sInput)-1
    while i >= 0:
        if sInput[i].isdigit() == True:
            return sInput[i]
        else:
            i = i-1
                   
def ReplaceNumbers(sInput):
    i=0
    tempStr = ""
    for i in range(len(sInput)):
        tempStr = tempStr + sInput[i]
        if "one" in tempStr:
            tempStr = tempStr.replace("on","1")
        elif "two" in tempStr:
            tempStr = tempStr.replace("tw","2")
        elif "three" in tempStr:
            tempStr = tempStr.replace("thre","3")
        elif "four" in tempStr:
            tempStr = tempStr.replace("four","4")
        elif "five" in tempStr:
            tempStr = tempStr.replace("fiv","5")
        elif "six" in tempStr:
            tempStr = tempStr.replace("six","6")
        elif "seven" in tempStr:
            tempStr = tempStr.replace("seve","7")
        elif "eight" in tempStr:
            tempStr = tempStr.replace("eigh","8")
        elif "nine" in tempStr:
            tempStr = tempStr.replace("nine","9")
        else:
            pass
    return tempStr

PuzzleInput = "PuzzleInput.txt"
f = open(PuzzleInput)
txt = f.readlines()
result = 0
tempResult = 0

for n in txt:
    k = ReplaceNumbers(n)
    tempResult = FirstNumber(k)+LastNumber(k)
    tempResult = int(tempResult)
    result = result + tempResult

print(result)