import periodictable
import re

def mmcalc(compound):
    c = compound
    epat = r'[A-Z][a-z]?'
    ncheck = r'[a-z][a-z]'
    test = re.findall(ncheck, c)
    if test != []:
         return "error"
    els = re.findall(epat, c)
    rlist = []
    for e in els:
            if hasattr(periodictable, e):
                rlist.append(e)
            else:
                return "error"
   
    coescrapr = r'[A-Z][a-z]?'
    coelist = re.split(coescrapr, c)    
    pairedlist = []
    if len(coelist) >= len(rlist):
        llength = len(coelist)
    else:
        llength = len(rlist)
    for k in range(llength):
        try:
            pairedlist.append(coelist[k])
        except IndexError:
            pass
        try:
            pairedlist.append(rlist[k])
        except IndexError:
            pass
    pairedlist = [item for item in pairedlist if item]
    #print(pairedlist)

    parenlist = []
    for n in pairedlist:
        indcount = 0
        lastind = '*'
        for b in n:
            if lastind == pairedlist.index(n):
                indcount += 1

            if b == '(':
                #templist.insert(pairedlist.index(n)+indshift,'(')
                parenlist.append(pairedlist.index(n)+indcount)
                lastind = pairedlist.index(n)
                #indshift += 1
            if b == ')':
                #templist.insert(pairedlist.index(n)+indshift,')')
                parenlist.append(pairedlist.index(n)+indcount)
                lastind = pairedlist.index(n)
                #indshift += 1
        
    print('next 3')
    print(pairedlist)
    print(parenlist)
    lincount = 1
    counter = 0 
    lastf= -1
    for f in parenlist:
        if lastf != f:
            if counter % 2 != 0:
                pairedlist.insert(f+1,')')
            else:
                pairedlist.insert(f+1,'(')
            counter += 1
        else: 
            if counter % 2 != 0:
                pairedlist.insert(f+2,'3*')
            else:
                pairedlist.insert(f+2,'4*')
            counter += 1
        lastf = f
        

    #rincount = 1
    #for d in rparenlist:
        
    #    pairedlist.insert(d+rincount,')')
     #   rincount += 1 
    #print(pairedlist)
    for q in pairedlist:
        storestr = ''
        storestr2 = ''
        for w in q:
            if w != '(' and len(pairedlist[pairedlist.index(q)]) != 1:
                storestr2 = storestr + w
                storestr = storestr2
        if len(pairedlist[pairedlist.index(q)]) != 1:
            pairedlist[pairedlist.index(q)] = storestr
    for q in pairedlist:
        storestr = ''
        storestr2 = ''
        for w in q:
            if w != ')' and len(pairedlist[pairedlist.index(q)]) != 1:
                storestr2 = storestr + w
                storestr = storestr2
        if len(pairedlist[pairedlist.index(q)]) != 1:
            pairedlist[pairedlist.index(q)] = storestr
    print(pairedlist)
    colist = []
    elemlist = []
    for i in pairedlist:
        if hasattr(periodictable, i) == True:
            elemlist.append(i)
            try:
                colist.append(float(pairedlist[pairedlist.index(i)+1]))
            except ValueError:
                colist.append(float(1))
        elif i == '(':
            elemlist.append(i)
            colist.append(float(-1))
        elif i == ')':
            elemlist.append(i)
            try:
                colist.append(float(pairedlist[pairedlist.index(i)+1]))
            except ValueError:
                colist.append(float(1))
    print(elemlist)
    print(colist)
    for t in range(len(colist)):
        if hasattr(periodictable, (elemlist[t])) == True:
            elemlist[t] = (getattr(periodictable, elemlist[t]).mass)*(colist[t])
    print(elemlist)
    sumlist = []
    lparenlist = []
    rparenlist = []
    
    for b in range(len(elemlist)):
        if elemlist[b] == '(':
            lparenlist.append(b)
        if elemlist[b] == ')':
            rparenlist.append(b)
    print(lparenlist)
    print(rparenlist)
    for p in lparenlist:
        addr = float(0)
        for k in elemlist[p:rparenlist[lparenlist.index(p)]]:
            addr = addr + k
        sumlist.append(addr*elemlist[p+1])
    print("LOOK HERE: ")
    print(sumlist)





    for y in elemlist:
        if y == '(':
            
            parlist = []
            addr = float(0)
            for u in elemlist[elemlist.index(y)+1:]:
                if u != ')' and u != '(':
                    parlist.append(u)
                    #print(u)
                if u == '(' or u ==')':
                    break
            print(parlist)
            for o in parlist:
                addr = o+addr
            sumlist.append(addr*colist[elemlist.index(u)])

        elif y != ')':
            sumlist.append(y)
    print(sumlist)
    rmass = 0
    for s in sumlist:
        rmass = rmass + s
    return rmass

    
print('mmcalc returns ' + str(mmcalc('Mg2.5(OH)2(NN)')))
