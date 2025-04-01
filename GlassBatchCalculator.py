import math
import periodictable
import re

# reads how many glass components, returns int
def getgcompcount():
    while True:
        try:
            gcompCount = int(input("How many components does your glass have? "))
            if 1 <= gcompCount <= 10:
                break
            else:
                print("Must be 1 to 10 components")
        except ValueError:
            print("Please enter an integer between 1 and 10 ")
    if gcompCount == 1:
        print("Your glass has "+str(gcompCount)+" component")
    else:
        print("Your glass has "+str(gcompCount)+" components")
    return gcompCount


# GIVE ME THE ELEMENTS!
def E(comp):
    comp = comp
    elementpattern = r'[A-Z][a-z]?'
    wrongpattern = r'[a-z][a-z]'
    check = re.findall(wrongpattern, comp)
    if check != []:
         return "error"
    elist = re.findall(elementpattern, comp)
    rlist = []
    for e in elist:
            if hasattr(periodictable, e):
                rlist.append(e)
            else:
                return "error"
    return "good"
            

def getgcomps(gcc):
    glasscomps = []
    for i in range(gcc):
        while True:
            try:
                compin = input("Glass component "+str(i+1)+": ")
                if E(compin) != "error":
                                        glasscomps.append(compin)
                                        break
            # the next 2 lines are required for it to work but don't ever act
            except ValueError:
                print("Not a valid component, try again ")

    print(f'Glass list: {glasscomps}')
    return glasscomps
        

def getmolperc(gcomps):
    gcomps = gcomps
    molpercs = []
    for i in gcomps:
            while True:
                try:
                        molp = float(input(f'What mol% of {i}? '))
                        molpercs.append(molp)
                        break
                except ValueError:
                        print("Please enter a number between 0 and 100 ")

    # Check if mol% = 100
    moltotalperc = float(0)
     
    for l in molpercs:
          indexa = molpercs.index(l)
          moltotalperc = moltotalperc + float(molpercs[indexa])
    if moltotalperc != 100:
        print("Mol% total doesn't equal 100.")
        getmolperc(gcomps)
    else:
        print('Mol%\s: ')
        for x in gcomps:
            index = gcomps.index(x)
            print(f'{x}: {molpercs[index]}%')
        check = input("Are these correct? Y or N ")
        if check != 'Y':
            getmolperc(gcomps)
        return molpercs

    
def getrmats(count,glist):
    count = count
    glist = glist
    matlist = []
    for i in range(count):
        while True:
            try:
                compin = input("Raw material for "+glist[i]+": ")
                if E(compin) != "error":
                                            matlist.append(compin)
                                            break
            except ValueError:
                    print('Not a valid material, please try again. ')
    print(f'Raw Materials')
    for x in matlist:
      print(f'For {glist[matlist.index(x)]}: {x}')
    check = input("Are these correct? Y or N ")
    if check != 'Y':
          getrmats(count, glist)
          
    return matlist

# Makes compound strings into elements
def Eread(el):
    sym = el
    EL = getattr(periodictable, sym)
    print(EL.mass)
      
            
      
     

    


# Running
compcount = getgcompcount()
gcomplist = getgcomps(compcount)
molpercs = getmolperc(gcomplist)
rmatlist = getrmats(compcount,gcomplist)