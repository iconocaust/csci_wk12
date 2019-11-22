"""
GALEN STEVENSON
CSCI 102 -C
WEEK 11 LABA

GITHUB: github.com/iconocaust/csci_wk12

"""

# PRINT OUTPUT
def PrintOutput(string):
    print("OUTPUT", string)
    
# LOAD FILE
def LoadFile(file):
    f = open(file, "r")
    f.read()
    lines = []
    for line in f:
        lines.append(line.rstrip("\n")
    

# UPDATE STRING
def UpdateString(string, string_add, num):
    string_mod = ""
    for i in range(len(string1)):
        if i == num:
            string_mod += string_add
        else:
            string_mod += string[i]
        
# FIND WORD COUNT
def FindWordCount(mylist, string):
    num = 0
    for s in mylist:
        s = s.split()
        for word in s:
            if word == string:
                num += 1
    
#SCORE FINDER
def ScoreFinder(onelist, twolist, string):
    scores = []
    for p in onelist:
        scores.append(p.lower())
    string = string.lower()
    if string in scores:
        i = scores.index(string)
        print("OUTPUT", twolist[i])
    else:
        print("OUTPUT player not found")
    
# UNION
def Union(onelist, twolist):
    biglist = onelist + twolist
    return biglist

# INTERSECTION
def Intersection(onelist, twolist):
    biglist = []
    for v in onelist:
        if v in twolist:
            biglist.append(v)
    return biglist

# NOT IN
def NotIn(onelist, twolist):
    biglist = []
    for v in onelist:
        if v not in twolist:
            biglist.append(v)
    return biglist

