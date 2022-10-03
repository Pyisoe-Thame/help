
# Online Python - IDE, Editor, Compiler, Interpreter

digilist = []
non_digilist = []
tempstr = ''

ogstring = input()
tempstr = ogstring[0] # initialise the tempstr with 1st char
n = 1
# n starts from 1 so that n can conpare with n-1 (the previous char)

while n < len(ogstring): # not n <= bcz out of range
    if ogstring[n].isdigit() ^ ogstring[n-1].isdigit():
        if ogstring[n-1].isdigit():
            digilist.append(tempstr)
        else:
            non_digilist.append(tempstr)
        tempstr = '' # flush the tempstr
    tempstr = tempstr + ogstring[n]
    n = n+1

# add the final tempstr to the according list
if ogstring[n-1].isdigit():
    digilist.append(tempstr)
else:
    non_digilist.append(tempstr)

#serve the lists
print(digilist) 
print(non_digilist)
    