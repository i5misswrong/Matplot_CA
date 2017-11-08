import random
allBlock=[]

allPeople=[]
for i in range(10):
    for j in range(10):
        P=[i,j]
        allBlock.append(P)
random.shuffle(allBlock)
allPeople=allBlock[:10]
print(allPeople)
print(allBlock)