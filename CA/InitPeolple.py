import random
import Data,Block
class InitPeople():
    def creatPeople(self):
        allBlock=[]
        allPeople=[]
        for i in range(1,Data.BasicData.ROOM_M):
            for j in range(1,Data.BasicData.ROOM_N):
                b=Block.Block(1)
                b.x=i
                b.y=j
                if j>Data.BasicData.ROOM_N/2:
                    b.type=False
                else:
                    b.type=True
                allBlock.append(b)
        random.shuffle(allBlock)
        allPeople=allBlock[:10]
        return allPeople

    def creatAppointPeo(self):
        allPeople=[]
        b1=Block.Block(1)
        b1.x=3
        b1.y=5
        b1.type=True
        allPeople.append(b1)

        b2=Block.Block(1)
        b2.x=4
        b2.y=5
        b2.type=False
        allPeople.append(b2)

        b3 = Block.Block(1)
        b3.x = 5
        b3.y = 5
        b3.type = False
        allPeople.append(b3)

        b4 = Block.Block(1)
        b4.x = 6
        b4.y = 5
        b4.type = False
        allPeople.append(b4)

        return allPeople

    def creatWall(self):
        allWall=[]
        for i in range(5):
            D=[i,0]
            U=[i,2]
            allWall.append(D)
            allWall.append(U)
        return allWall
    def creatExit(self):
        allExit=[]
        for i in range(3):
            L=[0,i]
            R=[4,i]
            allExit.append(L)
            allExit.append(R)
        return allExit



