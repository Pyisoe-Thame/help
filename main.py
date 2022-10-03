
# Online Python - IDE, Editor, Compiler, Interpreter

list1 = []
list2 = []
tempstr = ''

def isInt(n):
    if n >='0' and n <='9':
        return True
    else:
        return False

n=0
ogstring = input()
tempstr = tempstr + ogstring[n] # start adding to tempstr
n = n+1 # now n start from 1
# passed the first loop so that n can conpare with n-1 (the previous char)

while n < len(ogstring): # not n <= bcz out of range
    if ((isInt(ogstring[n]) and (isInt(ogstring[n-1])==False)) or ((isInt(ogstring[n])==False) and isInt(ogstring[n-1]))):
        if(isInt(ogstring[n-1])):
            list1.append(tempstr)
        else:
            list2.append(tempstr)
        # toggleList(currentlist)
        tempstr = '' # flush the tempstr
        # print('we are not the same')
    tempstr = tempstr + ogstring[n]
    n = n+1

# add the final tempstr to the according list
if(isInt(ogstring[n-1])):
    list1.append(tempstr)
else:
    list2.append(tempstr)

#serve the lists
print(list1) 
print(list2)
    