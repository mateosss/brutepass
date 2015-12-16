#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#ANSI characters
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

args = sys.argv
defaultTags = ["123","1234","admin","root","user",""]
options = ["-h","-t","-s","-w","-o","-d","-i"]

help = False
time = 0
size = 0
#TODO minChars = 1#minimum amount of characters
#TODO isStrong = False#If the passwords must be strong (with symbols, uppercase, lowercase and numbers)
#TODO types = ["basic", "2tags", "3tags"]#Level of agressivity
#TODO has = ["a", "66"]#Strings that the password have
tags = []
output = "passwords.txt"
default = False

passList = []
#-----COMBINATIONS-----#
#BASICS

def capitalize(words):
    res = []
    for i in words:
        if i[0].islower():
            first = i[0].upper()
        else:
            first = i[0].lower()
        word = first + i[1:]
        res.append(word)
    return res



def shift(words):
    res = []
    for i in words:
        word = ""
        for j in i:
            if j.islower():
                word += j.upper()
            else:
                word += j.lower()
        res.append(word)
    return res

def join(words):
    res = []
    for i in words:
        for j in words:
            if j != i:
                il = i.lower()
                jl = j.lower()
                if not jl in il and not il in jl:
                    res.append(i + j)
                    res.append(i + "_" + j)
                    res.append(i + "." + j)
                    res.append(i + "-" + j)
    return res

def split(words):
    res = []
    for i in words:
        if len(i) >= 1:
            if not i[0].lower() in words:
                res.append(i[0].lower())#add first letter word
            if i.isdigit():
                if len(i) >= 2:
                    res.append(i[-2:])#added last two digits
                if len(i)%2 == 0:
                    res.append(i[0:int(len(i)/2)])#added two halfs of the digit
                    res.append(i[int(len(i)/2):])
            if len(i) < 6:
                res.append(i[::-1])
            if i.isalpha() and len(i) >= 5:
                vocals = ["a","A","e","E","i","I","o","O","u","U"]
                wordWOVocals = ""
                for j in i:
                    if not j in vocals:
                        wordWOVocals += j
                if wordWOVocals != "":
                    res.append(wordWOVocals)#added word without vocals
    return res


#-----CORE-----#
def run():
    global tags
    global passList
    res = []

    splitWords = split(tags)
    #p,c,pp,cc
    capWords = capitalize(tags)
    #Pipa, Cuc
    shiftWords = shift(tags)
    #PIPA, CUC
    joinWords = join(tags)
    #pipacuc,cucpipa

    capSplitWords = capitalize(splitWords)
    #P,C,Pp,Cc
    capShiftWords = capitalize(shiftWords)
    #pIPA, cUC
    capJoinWords = capitalize(joinWords)
    #Pipacuc, Cucpipa

    upSplitWords = shift(splitWords)
    #P,C,PP,CC
    upCapWords = shift(capWords)
    #pIPA, cUC
    upJoinWords = shift(joinWords)
    #PIPACUC, CUCPIPA

    allWords = tags + splitWords + capWords + shiftWords + capSplitWords + capShiftWords + upSplitWords + upCapWords

    splitAllWords = split(allWords)
    joinAllWords = join(allWords)

    addWords(allWords)
    addWords(splitAllWords)
    addWords(joinAllWords)

    fileLength = write()
    print ("Done... "+ str(fileLength) + " combinations generated.")

def addWords(words):
    global passList
    passList.extend(words)

def write():
    global passList
    global output
    filteredPassList = list(set(passList))
    target = open(output, 'w')
    for i in filteredPassList:
        target.write(i+"\n")
    target.close()
    return len(filteredPassList)

def getHelp():
    help = """
    Usage Example:
    python brutepass.py -t 3600 -d -s 100 -o pass.txt -w tag1 tag2 tag3 tag4

    Commands:
    -h :\tShow this help.
    -t :\tSpecifies the max time (in seconds) to spend in generating passwords.
    -s :\tSpecifies the max size (in kilobytes) of the file of passwords.
    -w :\tList of tags to make passwords from.
    -o :\tSpecifies the output file in which the passwords will be stored (default: passwords.txt).
    -d :\tTells the program to use the defaults tags (F.e. "1234", "admin", "", "root").
    -i :\tSpecifies an input file with tags to prove.
    """
    return help

#-----EXECUTION-----#
if len(args) > 1:
    for i in range(len(args)):
        if args[i] == "-h":
            print(getHelp())
            exit()
        if args[i] == "-t":
            time = float(args[i+1])
        if args[i] == "-s":
            size = float(args[i+1])
        if args[i] == "-o":
            output = str(args[i+1])
        if args[i] == "-d":
            default = True
        if args[i] == "-i":
            file = open(args[i+1], 'r')
            tags = file.read().splitlines()
        if args[i] == "-w":
            for j in range(i+1, len(args)):
                if args[j] not in options:
                    tags.append(args[j].lower())
                else:
                    break
    if default:
        for i in defaultTags:
            tags.append(i)
    print("help: " + str(help))
    print("time: " + str(time))
    print("size: " + str(size))
    print("output: " + str(output))
    print("default: " + str(default))
    print("words: ",end="")
    print(", ".join(str(i) for i in tags))

    run()
else:
    #TODO Make a terminal menu
    print(getHelp())
