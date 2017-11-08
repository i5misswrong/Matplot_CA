import Data,Direction
import random
class outDirection():
    def outDirection(self,p,allPeople):

        self.countDefine(p) #计算默认方向收益
        self.isNextNull(p,allPeople)#计算下一点是否有行人
        self.countRandom(p)#count random direction income
        self.addIncome(p)#将所有收益加起来
        self.sortDic(p)#对收益进行排序
        # print(p.allInComeBySort)
    '''将所有收益加起来'''
    def addIncome(self,p):
        v1=[]#收益1：默认方向收益
        v2=[]#收益2：下一点是否有行人
        v3=[]# randow direction income
        '''遍历行人收益 将收益存入列表v1 v2...中'''
        for i in p.defineDirectionIncome.values():#遍历值 获取收益值
            v1.append(i)#将其添加到v1
        for i in p.nextNull.values():
            v2.append(i)
        for i in p.randomIncome.values():
            v3.append(i)
        income = list(map(lambda x, y, z: [x + y + z], v1, v2, v3))#将v1 v2对应元素加起来
        '''将得到的收益总和（列表）转化为字典 添加到p'''

        for key in p.allInCome:
            p.allInCome[key]=income[key-1][0]
    '''对收益排序 降序'''
    def sortDic(self,p):
        '''对字典的值进行排序'''
        dic=sorted(p.allInCome.items(),key=lambda d:d[1],reverse=True)
        '''由于dic的type为 ([],[],[],[])需要将其转换为字典'''
        k=[]#存放key的列表
        v=[]#存放vule的列表
        for i in dic:#遍历dic
            k.append(i[0])#将key存入
            v.append(i[1])#将value存入
        fin=dict(map(lambda x,y:[x,y],k,v))#转化为字典
        p.allInComeBySort=fin#将其存入p





    '''----------收益计算------------------------------------'''
    '''计算随机方向收益'''
    def countRandom(self,p):
        for i in range(1,10):
            p.randomIncome[i]=random.random()
    '''默认方向收益'''
    def countDefine(self,p):
        if p.y>Data.BasicData.ROOM_N/2:
           p.defineDirectionIncome[4]=100
        else:
            p.defineDirectionIncome[6]=100

    '''检测下一是否有行人，如果有，设为-1000'''
    def isNextNull(self,p,allPelple):
        for peo in allPelple:
            if p.x-1==peo.x and p.y+1 ==peo.y:
                p.nextNull[1]=-1000
            elif p.x==peo.x and p.y+1==peo.y:
                p.nextNull[2]=-1000
            elif p.x+1==peo.x and p.y+1==peo.y:
                p.nextNull[3]=-1000
            elif p.x-1==peo.x and p.y==peo.y:
                p.nextNull[4]=-1000
            # elif p.x==peo.x and p.y==peo.y:
            #     p.nextNull[5]=-1000
            elif p.x+1==peo.x and p.y==peo.y:
                p.nextNull[6]=-1000
            elif p.x-1==peo.x and p.y-1==peo.y:
                p.nextNull[7]=-1000
            elif p.x==peo.x and p.y-1==peo.y:
                p.nextNull[8]=-1000
            elif p.x+1==peo.x and p.y-1==peo.y:
                p.nextNull[9]=-1000


