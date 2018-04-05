# -*- coding: UTF-8 -*-
from graphics import *
from button import *
import random

#The demo of the chess--------------------------------------------
def setting():
    win=GraphWin('六子棋',600,400)
    Image(Point(300,200),"background.gif").draw(win)
    for i in range(0,20):
        line=Line(Point(20,i*20),Point(380,i*20))
        line.draw(win)
    for k in range(0,20):
        line=Line(Point(k*20,20),Point(k*20,380))
        line.draw(win)                
    return win
win=setting()
#Defination of the demo
lable1=Text(Point(500,50),"")
lable1.setSize(20)
lable1.setTextColor("red")
lable1.draw(win)
peocombutton=Button(win,Point(500,100),80,40,'Human-Computer')
peopeobutton=Button(win,Point(500,180),80,40,'Human-Human')
huiqibutton=Button(win,Point(500,260),80,40,'Backward')
quitbutton=Button(win,Point(500,340),80,40,'Quit')
zuobiao = [[0 for col in range(22)] for row in range(22)]
step=0
point=Point(1,1)
record=[]
firstclick=point
asureX=[]
asureY=[]

#Reset Function to start over the game---------------------------------------------------------------
def reset(record):
    for i in range(0,len(record)):
        record[i].undraw()
    global zuobiao
    global step
    zuobiao = [[0 for col in range(23)] for row in range(23)]
    step=0
    lable1.setText("")
#End

#Backward function
def huiqi():
    global zuobiao,step,asureX,asureY,record
    m=len(record)
    n=len(asureX)
    p=len(asureY)
    record[m-1].undraw()
    del record[m-1]
    zuobiao[asureX[n-1]][asureY[p-1]]=0
    del asureX[n-1]
    del asureY[p-1]
    step=step-1
#End
#Whether one side has won the game---------------------------------------------------
def calculate(zuobiao):
    cal=0
    judge=0
    m=0
    for i in range(17):
        for j in range(21):
            for k in range(6):
                if zuobiao[i+k][j]!=0:
                    judge=judge+zuobiao[i+k][j]
                    m=m+1
            if judge==6 and m==6:
                return 1                            
            if judge==12 and m==6:
                return 2
            judge=0
            m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(17):
            for k in range(6):
                if zuobiao[i][j+k]!=0:
                    judge=judge+zuobiao[i][j+k]
                    m=m+1
            if judge==6 and m==6:
                return 1
            if judge==12 and m==6:
                return 2
            judge=0
            m=0
    for i in range(21):
        for j in range(21):
            for k in range(6):
                if i+k<19 and j+k<21:
                    if zuobiao[i+k][j+k]!=0:
                        judge=judge+zuobiao[i+k][j+k]
                        m=m+1
            if judge==6 and m==6:
                return 1
            if judge==12 and m==6:
                return 2
            judge=0
            m=0
    #右下到左上
    for i in range(20):
        for j in range(20):
            for k in range(6):
                if i-k>=0 and j+k<21:
                    if zuobiao[i-k][j+k]!=0:
                        judge=judge+zuobiao[i-k][j+k]
                        m=m+1
            if judge==6 and m==6:
                return 1
            if judge==12 and m==6:
                return 2
            judge=0
            m=0
    if(zuobiao[19][19]!=0):
        cat=0
        for pp in range(0,6):
            cal=cal+zuobiao[19-pp][19-pp]
            if(zuobiao[19-pp][19-pp]==1):
                cat=cat+1
        if(cal==6 and cat==6):
            return 1
        if(cal==12):
            return 2
    return 0
#End-----------------------------------------------
def soukon():
    global zuobiao,win,step
    judge=0
    m=0
    for i in range(1,17):
        for j in range(21):
            if(zuobiao[i][j]==1 and zuobiao[i+1][j]==1 and zuobiao[i+2][j]==0 and zuobiao[i+3][j]==1 and zuobiao[i+4][j]==1 and (zuobiao[i+5][j] or zuobiao[i-1][j]==0)):
               circ=Circle(Point((i+2)*20,j*20),10)
               record.append(circ)
               circ.setFill('black')
               circ.draw(win)
               step=step+1
               zuobiao[i+2][j]=2
               return 1
    for i in range(21):
        for j in range(1,17):
            if(zuobiao[i][j]==1 and zuobiao[i][j+1]==1 and zuobiao[i][j+2]==0 and zuobiao[i][j+3]==1 and zuobiao[i][j+4]==1 and (zuobiao[i][j-1]==0 or zuobiao[i][j+5]==0)):
                circ=Circle(Point(i*20,(j+2)*20),10)
                record.append(circ)
                circ.setFill('black')
                circ.draw(win)
                step=step+1
                zuobiao[i][j+2]=2
                return 1
    for i in range(21):
        for j in range(21):
            for k in range(6):
                if(i+k<19 and j+k<21):
                    if(zuobiao[i][j]==1 and zuobiao[i+1][j+1]==1 and zuobiao[i+2][j+2]==0 and zuobiao[i+3][j+3]==1 and zuobiao[i+4][j+4]==1 and (zuobiao[i+5][j+5]==0 or zuobiao[i-1][j-1]==0)):
                        circ=Circle(Point((i+2)*20,(j+2)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        step=step+1
                        zuobiao[i+2][j+2]=2
                        return 1
    for i in range(20):
        for j in range(20):
            for k in range(6):
                if(i-k>=0 and j+k<21):
                    if(zuobiao[i][j]==1 and zuobiao[i-1][j+1]==1 and zuobiao[i-2][j+2]==0 and zuobiao[i-3][j+3]==1 and zuobiao[i-4][j+4]==1 and (zuobiao[i-5][j+5]==0 or zuobiao[i+1][j-1]==0)):
                        circ=Circle(Point((i-2)*20,(j+2)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        step=step+1
                        zuobiao[i-2][j+2]=2
                        return 1
#---------------------------------------------------------------------
def sousuo1():
    global win,zuobiao,step
    judge=0
    m=0
    for i in range(6,15):
        for j in range(6,15):
            if(zuobiao[i][j]==2 and zuobiao[i+1][j+1]==0):
                for  k in range(6):
                    if(zuobiao[i+k][j+k]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point((i+1)*20,(j+1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i+1][j+1]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0

    for i in range(6,14):
        for j in range(4,18):
            if(zuobiao[i][j]==2 and zuobiao[i+1][j]==0):
                for k in range(6):
                    if(zuobiao[i+k][j]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point((i+1)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i+1][j]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0
    for i in range(4,18):
        for j in range(6,14):
            if(zuobiao[i][j]==2 and zuobiao[i][j+1]==0):
                for k in range(6):
                    if(zuobiao[i][j+k]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point(i*20,(j+1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i][j+1]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0
#-------------------------------------------
def sousuo2():
    global win,zuobiao,step
    judge=0
    m=0
    for i in range(21):
        for j in range(21):
            if(zuobiao[i][j]+zuobiao[i+1][j+1]==4 and zuobiao[i+2][j+2]==0):
                for  k in range(6):
                    if(zuobiao[i+k][j+k]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point((i+2)*20,(j+2)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i+2][j+2]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0

    for i in range(17):
        for j in range(21):
            if(zuobiao[i][j]==2 and zuobiao[i+1][j]==2 and zuobiao[i+2][j]==0):
                for k in range(6):
                    if(zuobiao[i+k][j]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point((i+2)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i+2][j]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(17):
            if(zuobiao[i][j]+zuobiao[i][j+1]==4 and zuobiao[i][j+2]==0):
                for k in range(6):
                    if(zuobiao[i][j+k]!=1):
                        m=m+1
                if(m==6):
                    circ=Circle(Point(i*20,(j+2)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    step=step+1
                    zuobiao[i][j+2]=2
                    return 1
            judge=0
            m=0
    judge=0
    m=0

#Algorithm-------------------------------------------------------------------------
def search3(zuobiao):#
    sta1=[]#白
    sta2=[]#黑
    cal=0
    judge=0
    m=0
    for i in range(18):
        for j in range(21):
            for k in range(3):
                if zuobiao[i+k][j]!=0:
                    judge=judge+zuobiao[i+k][j]
                    m=m+1
            if judge==3 and m==3:
                sta1.append([1,i,j,10])                
            if judge==6 and m==3:
                sta2.append([2,i,j,10])                
            judge=0
            m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(18):
            for k in range(3):
                if zuobiao[i][j+k]!=0:
                    judge=judge+zuobiao[i][j+k]
                    m=m+1
            if judge==3 and m==3:
                sta1.append([1,i,j,11])                
            if judge==6 and m==3:
                sta2.append([2,i,j,11])                
            judge=0
            m=0
    for i in range(21):
        for j in range(21):
            for k in range(3):
                if i+k<19 and j+k<21:
                    if zuobiao[i+k][j+k]!=0:
                        judge=judge+zuobiao[i+k][j+k]
                        m=m+1
            if judge==3 and m==3:
                sta1.append([1,i,j,12])               
            if judge==6 and m==3:
                sta2.append([2,i,j,12])                
            judge=0
            m=0
    #右上到左下
    for i in range(20):
        for j in range(20):
            for k in range(3):
                if i-k>=0 and j+k<21:
                    if zuobiao[i-k][j+k]!=0:
                        judge=judge+zuobiao[i-k][j+k]
                        m=m+1
            if judge==3 and m==3:
                sta1.append([1,i-k,j+k,13])                
            if judge==6 and m==3:
                sta2.append([2,i-k,j+k,13])                
            judge=0
            m=0
    if(zuobiao[19][19]!=0):#???
        cat=0
        for pp in range(0,3):
            cal=cal+zuobiao[19-pp][19-pp]
            if(zuobiao[19-pp][19-pp]==1):
                    cat=cat+1
        if(cal==3 and cat==3):
            sta1.append([1,19-pp,19-pp,12])            
        if(cal==6):
            sta2.append([2,19-pp,19-pp,12])    
#----------------End-----------
   #Make decision for computer
    a,b=sta1,sta2#a白棋、b黑棋
    b1s=[]#黑棋胜利下棋位置
    c1s,c1e=[],[]
    c2s,c2e=[],[]#左，上空
    c3s=[]#右，下空
    c4s,c4e=[],[]
    if b!=[]:
        for i in range(len(b)):
            if b[i][2]==10:#横着3子
                if b[i][1]-2>=0:#横坐标大于等于0
                    if zuobiao[b[i][1]-1][b[i][2]]==0 and zuobiao[b[i][1]-2][b[i][2]]==2 and zuobiao[b[i][1]-3][b[i][2]]==2 :#2黑空3黑
                        return[[b[i][1]-1,b[i][2]],[],1]
                                
                if b[i][1]+5<=18:                    
                    if zuobiao[b[i][1]+3][b[i][2]]==0 and zuobiao[b[i][1]+4][b[i][2]]==2 and zuobiao[b[i][1]+5][b[i][2]]==2:#3黑空2黑
                        return[[b[i][1]+3,b[i][2]],[],1]
                    
                if b[i][1]-1>=0 and b[i][1]+3<=18:
                    if zuobiao[b[i][1]-1][b[i][2]]==zuobiao[b[i][1]+3][b[i][2]]==0:#两端都无棋
                        return[[b[i][1]-1,b[i][2]],[b[i][1]+3,b[i][2]],0]                               
                
                elif b[i][1]-1<0:                   
                    if zuobiao[b[i][1]+3][b[i][2]]==0 and zuobiao[b[i][1]+4][b[i][2]]==0:
                        return[[b[i][1]+3,b[i][2]],[b[i][1]+4,b[i][2]],0]            
        
                elif b[i][1]+3>18:               
                    if zuobiao[b[i][1]-1][b[i][2]]==0 and zuobiao[b[i][1]-2][b[i][2]]==0:
                        return[[b[i][1]-1,b[i][2]],[b[i][1]-2,b[i][2]],0]

            elif b[i][3]==11:#竖着3子
                if b[i][2]-3>=0:
                    if zuobiao[b[i][1]][b[i][2]-1]==0 and zuobiao[b[i][1]][b[i][2]-2]==2 and zuobiao[b[i][1]][b[i][2]-3]==2 :
                        return[[b[i][1],b[i][2]-1],[],1]            
            
                if b[i][2]+5<=18:                    
                    if zuobiao[b[i][1]][b[i][2]+3]==0 and zuobiao[b[i][1]][b[i][2]+4]==2 and zuobiao[b[i][1]][b[i][2]+5]==2 :
                        return[[b[i][1],b[i][2]+3],[],1]
                    
                if b[i][2]-1>=0 and b[i][2]+3<=18:
                    if zuobiao[b[i][1]][b[i][2]-1]==zuobiao[b[i][1]][b[i][2]+3]==0:#两端都无棋
                        return[[b[i][1],b[i][2]-1],[b[i][1],b[i][2]+3],0]                             
                
                elif b[i][2]-1<0:                   
                    if zuobiao[b[i][1]][b[i][2]+3]==0 and zuobiao[b[i][1]][b[i][2]+4]==0:
                        return[[b[i][1],b[i][2]+3],[b[i][1],b[i][2]+4],0]            
        
                elif b[i][2]+4>18:               
                    if zuobiao[b[i][1]][b[i][2]-1]==0 and zuobiao[b[i][1]][b[i][2]-2]==0:
                        return[[b[i][1],b[i][2]-1],[b[i][1],b[i][2]-2],0]

            elif b[i][3]==12:#右斜3个子
                if b[i][1]-3>=0 and b[i][2]-3>=0:
                    if zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]-2][b[i][2]-2]==2 and zuobiao[b[i][1]-3][b[i][2]-3]==2:
                        return[b[i][1]-1,b[i][2]-1],[],1
                       
                if b[i][1]+5<=18 and b[i][2]+5<=18:
                    if zuobiao[b[i][1]+3][b[i][2]+3]==0 and zuobiao[b[i][1]+4][b[i][2]+4]==2 and zuobiao[b[i][1]+5][b[i][2]+5]==2:
                        return[b[i][1]+4,b[i][2]+4],[],1                        
                    
                if b[i][1]-1>=0 and b[i][2]-1>=0 and b[i][1]+3<=18 and b[i][2]+3<=18:
                    if zuobiao[b[i][1]-1][b[i][2]-1]==zuobiao[b[i][1]+3][b[i][2]+3]==0:#两端都无棋
                        return[b[i][1]-1,b[i][2]-1],[b[i][1]+3,b[i][2]+3],0
                       
                    elif zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]+3][b[i][2]+3]!=0:#下端是白棋
                        if b[i][1]-2>=0 and b[i][2]-2>=0:
                            if zuobiao[b[i][1]-2][b[i][2]-2]==0:
                                return[b[i][1]-1,b[i][2]-1],[b[i][1]-2,b[i][2]-2],0                               
                    
                    elif zuobiao[b[i][1]+3][b[i][2]+3]==0 and zuobiao[b[i][1]-1][b[i][2]-1]!=0:#上端是白棋
                        if b[i][1]+4<=18 and b[i][2]+4<=18:
                            if zuobiao[b[i][1]+4][b[i][2]+4]==0:
                                return[b[i][1]+3,b[i][2]+3],[b[i][1]+4,b[i][2]+4],0                                
                        
                elif b[i][1]-1<0 or b[i][2]-1<0:#上边在边界
                    if b[i][1]+3<=18 and b[i][2]+3<=18:
                        if b[i][1]+4<=18 and b[i][2]+4<=18:                            
                            if zuobiao[b[i][1]+3][b[i][2]+3]==0 and zuobiao[b[i][1]+4][b[i][2]+4]==0:
                                return[b[i][1]+3,b[i][2]+3],[b[i][1]+4,b[i][2]+4],0
                                                       
                elif b[i][1]+3>18 or b[i][2]+3>18:#下边在边界
                    if b[i][1]-1>=0 and b[i][2]-1>=0:
                        if b[i][1]-2>=0 and b[i][2]-2>=0:
                            if zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]-2][b[i][2]-2]==0:
                                return[b[i][1]-1,b[i][2]-1],[b[i][1]-2,b[i][2]-2],0

            elif b[i][3]==13:#左斜3个子
                if b[i][1]-3>=0 and b[i][2]+3<=18:#判断是否只用下一个子就赢了
                    if zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]-2][b[i][2]+2]==2 and zuobiao[b[i][1]-3][b[i][2]+3]:
                        return[b[i][1]-1,b[i][2]+1],[],1
            
                if b[i][1]+4<=18 and b[i][2]-4>=0:
                    if zuobiao[b[i][1]+3][b[i][2]-3]==0 and zuobiao[b[i][1]+4][b[i][2]-4]==2:
                        return[b[i][1]+3,b[i][2]-3],[],1                        
                    
                if b[i][1]-1>=0 and b[i][2]+1<=18 and b[i][1]+3<=18 and b[i][2]-3>=0:
                    if zuobiao[b[i][1]-1][b[i][2]+1]==zuobiao[b[i][1]+3][b[i][2]-3]==0:#两端都无棋
                        return[b[i][1]-1,b[i][2]+1],[b[i][1]+3,b[i][2]-3],0
                        
                    elif zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]+3][b[i][2]-3]!=0:#上端是白棋
                        if b[i][1]-2>=0 and b[i][2]+2>=0:
                            if zuobiao[b[i][1]-2][b[i][2]+2]==0:
                                return[b[i][1]-1,b[i][2]+1],[b[i][1]-2,b[i][2]+2],0
                                
                    elif zuobiao[b[i][1]+3][b[i][2]-3]==0 and zuobiao[b[i][1]-1][b[i][2]+1]!=0:#下端是白棋
                        if b[i][1]+4<=18 and b[i][2]-4>=0:
                            if zuobiao[b[i][1]+4][b[i][2]-4]==0:
                                return[b[i][1]+3,b[i][2]-3],[b[i][1]+4,b[i][2]-4],0                                
                        
                elif b[i][1]-1<0 or b[i][2]+1>18:#下边在边界
                    if b[i][1]+3<=18 and b[i][2]-3>=0:
                        if b[i][1]+4<=18 and b[i][2]-4>=0:                            
                            if zuobiao[b[i][1]+3][b[i][2]-3]==0 and zuobiao[b[i][1]+4][b[i][2]-4]==0:
                                return[b[i][1]+3,b[i][2]-3],[b[i][1]+4,b[i][2]-4],0
                                                           
                elif b[i][1]+3>18 or b[i][2]-3<0:#上边在边界
                    if b[i][1]-1>=0 and b[i][2]+1<=18:
                        if b[i][1]-2>=0 and b[i][2]+2<=18:
                            if zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]-2][b[i][2]+2]==0:
                                return[b[i][1]-1,b[i][2]+1],[b[i][1]-2,b[i][2]+2],0

    if a!=[]:
        for i in range(len(a)):
            if a[i][3]==10:#横着3个子
                    #print a[i][3]
                if a[i][1]-1>=0 and a[i][1]+3<=18:
                    if zuobiao[a[i][1]-1][a[i][2]]==zuobiao[a[i][1]+3][a[i][2]]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]])
                        c1e.append([a[i][1]+3,a[i][2]])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]]==0 and zuobiao[a[i][1]+3][a[i][2]]==2:#右端是黑棋
                        if a[i][1]-2>=0:
                            if zuobiao[a[i][1]-2][a[i][2]]!=2:
                                c2s.append([a[i][1]-1,a[i][2]])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]]==2 and zuobiao[a[i][1]+3][a[i][2]]==0:#左端是黑棋
                        if a[i][1]+4<=18:
                            if zuobiao[a[i][1]+4][a[i][2]]!=2:
                                c3s.append([a[i][1]+3,a[i][2]])                                    
                            else:pass
                        else:pass
                    else:pass                        
                elif a[i][1]-1<0:#左边在边界
                    if zuobiao[a[i][1]+3][a[i][2]]==0 and zuobiao[a[i][1]+4][a[i][2]]!=2:
                        c3s.append([a[i][1]+4,a[i][2]])                            
                    else:pass
                elif a[i][1]+4>18:#右边在边界
                    if zuobiao[a[i][1]-1][a[i][2]]==0 and zuobiao[a[i][1]-2][a[i][2]]!=2:
                        c2s.append([a[i][1]-1,a[i][2]])                            
                    else:pass
                    

            elif a[i][3]==11:#竖着3个子                    
                if a[i][2]-1>=0 and a[i][2]+3<=18:
                    if zuobiao[a[i][1]][a[i][2]-1]==zuobiao[a[i][1]][a[i][2]+3]==0:#两端都无棋
                        c1s.append([a[i][1],a[i][2]-1])
                        c1e.append([a[i][1],a[i][2]+3])                            
                        break
                    elif zuobiao[a[i][1]][a[i][2]-1]==0 and zuobiao[a[i][1]][a[i][2]+3]==2:#下端是黑棋
                        if a[i][2]-2>=0:
                            if zuobiao[a[i][1]][a[i][2]-2]!=2:
                                c2s.append([a[i][1],a[i][2]-1])                                   
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]][a[i][2]-1]==2 and zuobiao[a[i][1]][a[i][2]+3]==0:#上端是黑棋
                        if a[i][2]+4<=18:
                            if zuobiao[a[i][1]][a[i][2]+4]!=2:
                                c3s.append([a[i][1],a[i][2]+3])                                    
                            else:pass
                        else:pass
                    else:pass#两端都是黑棋
                elif a[i][2]-1<0:#上边在边界
                    if zuobiao[a[i][1]][a[i][2]+3]==0 and zuobiao[a[i][1]][a[i][2]+4]!=2:
                        c3s.append([a[i][1],a[i][2]+3])                            
                    else:
                        pass
                elif a[i][2]+3>18:#下边在边界
                    if zuobiao[a[i][1]][a[i][2]-1]==0 and zuobiao[a[i][1]][a[i][2]-2]!=2:
                        c2s.append([a[i][1],a[i][2]-1])                            
                    else:
                        pass

            elif a[i][3]==12:#右斜3个子                    
                if a[i][1]-1>=0 and a[i][2]-1>=0 and a[i][1]+3<=18 and a[i][2]+3<=18:
                    if zuobiao[a[i][1]-1][a[i][2]-1]==zuobiao[a[i][1]+3][a[i][2]+3]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]-1])
                        c1e.append([a[i][1]+3,a[i][2]+3])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]-1]==0 and zuobiao[a[i][1]+3][a[i][2]+3]==2:#右下端是黑棋
                        if a[i][1]-2>=0 and a[i][2]-2>=0:
                            if zuobiao[a[i][1]-2][a[i][2]-2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]-1])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]-1]==2 and zuobiao[a[i][1]+3][a[i][2]+3]==0:#左上端是黑棋
                        if a[i][1]+4<=18 and a[i][2]+4<=18:
                            if zuobiao[a[i][1]+4][a[i][2]+4]!=2:
                                c3s.append([a[i][1]+3,a[i][2]+3])                                    
                            else:pass
                        else:pass
                    else:pass                        
                elif a[i][1]-1<0 or a[i][2]-1<0:#左上在边界
                    if a[i][1]+3<=18 and a[i][2]+3<=18:
                        if a[i][1]+4<=18 and a[i][2]+4<=18:
                            if zuobiao[a[i][1]+3][a[i][2]+3]==0 and zuobiao[a[i][1]+4][a[i][2]+4]!=2:
                                c3s.append([a[i][1]+3,a[i][2]+3])                                    
                            else:pass
                elif a[i][1]+3>18 or a[i][2]+3>18:#右下在边界
                    if a[i][1]-1>=0 and a[i][2]-1>=0:
                        if a[i][1]-2>=0 and a[i][2]-2>=0:
                            if zuobiao[a[i][1]-1][a[i][2]-1]==0 and zuobiao[a[i][1]-2][a[i][2]-2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]-1])                                    
                            else:pass
                

            elif a[i][3]==13:#左斜3个子                    
                if a[i][1]-1>=0 and a[i][2]+1<=18 and a[i][1]+3<=18 and a[i][2]-3>=0:
                    if zuobiao[a[i][1]-1][a[i][2]+1]==zuobiao[a[i][1]+3][a[i][2]-3]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]+1])
                        c1e.append([a[i][1]+3,a[i][2]-3])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]+1]==0 and zuobiao[a[i][1]+3][a[i][2]-3]==2:#右上端是黑棋
                        if a[i][1]-2>=0 and a[i][2]+2<=18:
                            if zuobiao[a[i][1]-2][a[i][2]+2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]+1])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]+1]==2 and zuobiao[a[i][1]+3][a[i][2]-3]==0:#左下端是黑棋
                        if a[i][1]+4<=18 and a[i][2]-4>=0:
                            if zuobiao[a[i][1]+4][a[i][2]-4]!=2:
                                c3s.append([a[i][1]+3,a[i][2]-3])                                    
                            else:pass
                        else:pass
                    else:
                        pass                            
                elif a[i][1]-1<0 or a[i][2]+1>18:#左下在边界
                    if a[i][1]+3<=18 and a[i][2]-3>=0:
                        if a[i][1]+4<=18 and a[i][2]-4>=0:
                            if zuobiao[a[i][1]+3][a[i][2]-3]==0 and zuobiao[a[i][1]+4][a[i][2]-4]!=2:
                                c3s.append([a[i][1]+3,a[i][2]-3])                                    
                            else:pass
                elif a[i][1]+3>18 or a[i][2]-3<0:#右上在边界
                    if a[i][1]-1>=0 and a[i][2]+1<=18:
                        if a[i][1]-2>=0 and a[i][2]+2<=18:
                            if zuobiao[a[i][1]-1][a[i][2]+1]==0 and zuobiao[a[i][1]-2][a[i][2]+2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]+1])                                    
                            else:pass


    if c1s!=[]:
        return c1s[0],c1e[0],2
    else:
        if len(c2s)==0 and len(c3s)==0:
            return [],[],2
        elif len(c2s)>=1 and len(c3s)>=1:
            return c2s[0],c3s[0],2
        elif len(c2s)==0 and len(c3s)>=1:
            if len(c3s)>=2:
                return c3s[0],c3s[1],2
            else:
                return c3s[0],[],2
        elif len(c3s)==0 and len(c2s)>=1:
            if len(c2s)>=2:
                return c2s[0],c2s[1],2
            else:
                return c2s[0],[],2
#
##识别四连子---------------------------------------------------------------------------
def sousuo4(zuobiao):       
    #编写识别四个子的函数
    sta1=[]
    sta2=[]
    cal=0
    judge=0
    m=0
    for i in range(17):
        for j in range(21):
            for k in range(4):
                if zuobiao[i+k][j]!=0:
                    judge=judge+zuobiao[i+k][j]
                    m=m+1
            if judge==4 and m==4:
                sta1.append([1,i,j,10])                
            if judge==8 and m==4:
                sta2.append([2,i,j,10])                
            judge=0
            m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(17):
            for k in range(4):
                if zuobiao[i][j+k]!=0:
                    judge=judge+zuobiao[i][j+k]
                    m=m+1
            if judge==4 and m==4:
                sta1.append([1,i,j,11])                
            if judge==8 and m==4:
                sta2.append([2,i,j,11])                
            judge=0
            m=0
    for i in range(21):
        for j in range(21):
            for k in range(4):
                if i+k<19 and j+k<21:
                    if zuobiao[i+k][j+k]!=0:
                        judge=judge+zuobiao[i+k][j+k]
                        m=m+1
            if judge==4 and m==4:
                sta1.append([1,i,j,12])                
            if judge==8 and m==4:
                sta2.append([2,i,j,12])                
            judge=0
            m=0
    #右上到左下
    for i in range(20):
        for j in range(20):
            for k in range(4):
                if i-k>=0 and j+k<21:
                    if zuobiao[i-k][j+k]!=0:
                        judge=judge+zuobiao[i-k][j+k]
                        m=m+1
            if judge==4 and m==4:
                sta1.append([1,i-k,j+k,13])                
            if judge==8 and m==4:
                sta2.append([2,i-k,j+k,13])                
            judge=0
            m=0
    if(zuobiao[19][19]!=0):#???
        cat=0
        for pp in range(0,4):
            cal=cal+zuobiao[19-pp][19-pp]
            if(zuobiao[19-pp][19-pp]==1):
                    cat=cat+1
        if(cal==4 and cat==4):
            sta1.append([1,19-pp,19-pp,12])            
        if(cal==8):
            sta2.append([2,19-pp,19-pp,12])            
    
#End
            
#Calculate the position 
    a,b=sta1,sta2#a白棋、b黑棋
    b1s=[]#黑棋胜利下棋位置
    c1s,c1e=[],[]
    c2s,c2e=[],[]#左，上空
    c3s=[]#右，下空
    c4s,c4e=[],[]
    if b!=[]:
        for i in range(len(b)):
            if b[i][3]==10:#横着四子
                if b[i][1]-2>=0:
                    if zuobiao[b[i][1]-1][b[i][2]]==0 and zuobiao[b[i][1]-2][b[i][2]]==2:
                        return[[b[i][1]-1,b[i][2]],[],1]            
            
                if b[i][1]+5<=18:                    
                    if zuobiao[b[i][1]+4][b[i][2]]==0 and zuobiao[b[i][1]+5][b[i][2]]==2:
                        return[[b[i][1]+4,b[i][2]],[],1]
                    
                if b[i][1]-1>=0 and b[i][1]+4<=18:
                    if zuobiao[b[i][1]-1][b[i][2]]==zuobiao[b[i][1]+4][b[i][2]]==0:#两端都无棋
                        return[[b[i][1]-1,b[i][2]],[b[i][1]+4,b[i][2]],0]            
        
                    elif zuobiao[b[i][1]-1][b[i][2]]==0 and zuobiao[b[i][1]+4][b[i][2]]!=0:#下端是白棋
                        if b[i][1]-2>=0:
                            if zuobiao[b[i][1]-2][b[i][2]]==0:
                              return[[b[i][1]-1,b[i][2]],[b[i][1]-2,b[i][2]],0]                    
                
                    elif zuobiao[b[i][1]+4][b[i][2]]==0 and zuobiao[b[i][1]-1][b[i][2]]!=0:#上端是白棋
                        if b[i][1]+5<=18:
                            if zuobiao[b[i][1]+5][b[i][2]]==0:
                                return[[b[i][1]+4,b[i][2]],[b[i][1]+5,b[i][2]],0]                    
                
                elif b[i][1]-1<0:                   
                    if zuobiao[b[i][1]+4][b[i][2]]==0 and zuobiao[b[i][1]+5][b[i][2]]==0:
                        return[[b[i][1]+4,b[i][2]],[b[i][1]+5,b[i][2]],0]            
        
                elif b[i][1]+4>18:               
                    if zuobiao[b[i][1]-1][b[i][2]]==0 and zuobiao[b[i][1]-2][b[i][2]]==0:
                        return[[b[i][1]-1,b[i][2]],[b[i][1]-2,b[i][2]],0]

            elif b[i][3]==11:#竖着四子
                if b[i][2]-2>=0:
                    if zuobiao[b[i][1]][b[i][2]-1]==0 and zuobiao[b[i][1]][b[i][2]-2]==2:
                        return[[b[i][1],b[i][2]-1],[],1]            
            
                if b[i][2]+5<=18:                    
                    if zuobiao[b[i][1]][b[i][2]+4]==0 and zuobiao[b[i][1]][b[i][2]+5]==2:
                        return[[b[i][1],b[i][2]+4],[],1]
                    
                if b[i][2]-1>=0 and b[i][2]+4<=18:
                    if zuobiao[b[i][1]][b[i][2]-1]==zuobiao[b[i][1]][b[i][2]+4]==0:#两端都无棋
                        return[[b[i][1],b[i][2]-1],[b[i][1],b[i][2]+4],0]            
        
                    elif zuobiao[b[i][1]][b[i][2]-1]==0 and zuobiao[b[i][1]][b[i][2]+4]!=0:#下端是白棋
                        if b[i][2]-2>=0:
                            if zuobiao[b[i][1]][b[i][2]-2]==0:
                              return[[b[i][1],b[i][2]-1],[b[i][1],b[i][2]-2],0]                    
                
                    elif zuobiao[b[i][1]][b[i][2]+4]==0 and zuobiao[b[i][1]][b[i][2]-1]!=0:#上端是白棋
                        if b[i][2]+5<=18:
                            if zuobiao[b[i][1]][b[i][2]+5]==0:
                                return[[b[i][1],b[i][2]+4],[b[i][1],b[i][2]+5],0]                    
                
                elif b[i][2]-1<0:                   
                    if zuobiao[b[i][1]][b[i][2]+4]==0 and zuobiao[b[i][1]][b[i][2]+5]==0:
                        return[[b[i][1],b[i][2]+4],[b[i][1],b[i][2]+5],0]            
        
                elif b[i][2]+4>18:               
                    if zuobiao[b[i][1]][b[i][2]-1]==0 and zuobiao[b[i][1]][b[i][2]-2]==0:
                        return[[b[i][1],b[i][2]-1],[b[i][1],b[i][2]-2],0]

            elif b[i][3]==12:#右斜四个子
                if b[i][1]-2>=0 and b[i][2]-2>=0:#判断是否只用下一个子就赢了
                    if zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]-2][b[i][2]-2]==2:
                        return[b[i][1]-1,b[i][2]-1],[],1
                       
                if b[i][1]+5<=18 and b[i][2]+5<=18:
                    if zuobiao[b[i][1]+4][b[i][2]+4]==0 and zuobiao[b[i][1]+5][b[i][2]+5]==2:
                        return[b[i][1]+4,b[i][2]+4],[],1                        
                    
                if b[i][1]-1>=0 and b[i][2]-1>=0 and b[i][1]+4<=18 and b[i][2]+4<=18:#下两个子才赢了
                    if zuobiao[b[i][1]-1][b[i][2]-1]==zuobiao[b[i][1]+4][b[i][2]+4]==0:#两端都无棋
                        return[b[i][1]-1,b[i][2]-1],[b[i][1]+4,b[i][2]+4],0
                       
                    elif zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]+4][b[i][2]+4]!=0:#下端是白棋
                        if b[i][1]-2>=0 and b[i][2]-2>=0:
                            if zuobiao[b[i][1]-2][b[i][2]-2]==0:
                                return[b[i][1]-1,b[i][2]-1],[b[i][1]-2,b[i][2]-2],0                               
                    
                    elif zuobiao[b[i][1]+4][b[i][2]+4]==0 and zuobiao[b[i][1]-1][b[i][2]-1]!=0:#上端是白棋
                        if b[i][1]+5<=18 and b[i][2]+5<=18:
                            if zuobiao[b[i][1]+5][b[i][2]+5]==0:
                                return[b[i][1]+4,b[i][2]+4],[b[i][1]+5,b[i][2]+5],0                                
                        
                elif b[i][1]-1<0 or b[i][2]-1<0:#上边在边界
                    if b[i][1]+4<=18 and b[i][2]+4<=18:
                        if b[i][1]+5<=18 and b[i][2]+5<=18:                            
                            if zuobiao[b[i][1]+4][b[i][2]+4]==0 and zuobiao[b[i][1]+5][b[i][2]+5]==0:
                                return[b[i][1]+4,b[i][2]+4],[b[i][1]+5,b[i][2]+5],0
                                                       
                elif b[i][1]+4>18 or b[i][2]+4>18:#下边在边界
                    if b[i][1]-1>=0 and b[i][2]-1>=0:
                        if b[i][1]-2>=0 and b[i][2]-2>=0:
                            if zuobiao[b[i][1]-1][b[i][2]-1]==0 and zuobiao[b[i][1]-2][b[i][2]-2]==0:
                                return[b[i][1]-1,b[i][2]-1],[b[i][1]-2,b[i][2]-2],0

            elif b[i][3]==13:#左斜四个子
                if b[i][1]-2>=0 and b[i][2]+2<=18:#判断是否只用下一个子就赢了
                    if zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]-2][b[i][2]+2]==2:
                        return[b[i][1]-1,b[i][2]+1],[],1
            
                if b[i][1]+5<=18 and b[i][2]-5>=0:
                    if zuobiao[b[i][1]+4][b[i][2]-4]==0 and zuobiao[b[i][1]+5][b[i][2]-5]==2:
                        return[b[i][1]+4,b[i][2]-4],[],1                        
                    
                if b[i][1]-1>=0 and b[i][2]+1<=18 and b[i][1]+4<=18 and b[i][2]-4>=0:#下两个子才赢了
                    if zuobiao[b[i][1]-1][b[i][2]+1]==zuobiao[b[i][1]+4][b[i][2]-4]==0:#两端都无棋
                        return[b[i][1]-1,b[i][2]+1],[b[i][1]+4,b[i][2]-4],0
                        
                    elif zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]+4][b[i][2]-4]!=0:#上端是白棋
                        if b[i][1]-2>=0 and b[i][2]+2>=0:
                            if zuobiao[b[i][1]-2][b[i][2]+2]==0:
                                return[b[i][1]-1,b[i][2]+1],[b[i][1]-2,b[i][2]+2],0
                                
                    elif zuobiao[b[i][1]+4][b[i][2]-4]==0 and zuobiao[b[i][1]-1][b[i][2]+1]!=0:#下端是白棋
                        if b[i][1]+5<=18 and b[i][2]-5>=0:
                            if zuobiao[b[i][1]+5][b[i][2]-5]==0:
                                return[b[i][1]+4,b[i][2]-4],[b[i][1]+5,b[i][2]-5],0                                
                        
                elif b[i][1]-1<0 or b[i][2]+1>18:#下边在边界
                    if b[i][1]+4<=18 and b[i][2]-4>=0:
                        if b[i][1]+5<=18 and b[i][2]-5>=0:                            
                            if zuobiao[b[i][1]+4][b[i][2]-4]==0 and zuobiao[b[i][1]+5][b[i][2]-5]==0:
                                return[b[i][1]+4,b[i][2]-4],[b[i][1]+5,b[i][2]-5],0
                                                           
                elif b[i][1]+4>18 or b[i][2]-4<0:#上边在边界
                    if b[i][1]-1>=0 and b[i][2]+1<=18:
                        if b[i][1]-2>=0 and b[i][2]+2<=18:
                            if zuobiao[b[i][1]-1][b[i][2]+1]==0 and zuobiao[b[i][1]-2][b[i][2]+2]==0:
                                return[b[i][1]-1,b[i][2]+1],[b[i][1]-2,b[i][2]+2],0

    if a!=[]:
        for i in range(len(a)):
            if a[i][3]==10:#横着四个子
                if a[i][1]-1>=0 and a[i][1]+4<=18:
                    if zuobiao[a[i][1]-1][a[i][2]]==zuobiao[a[i][1]+4][a[i][2]]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]])
                        c1e.append([a[i][1]+4,a[i][2]])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]]==0 and zuobiao[a[i][1]+4][a[i][2]]==2:#右端是黑棋
                        if a[i][1]-2>=0:
                            if zuobiao[a[i][1]-2][a[i][2]]!=2:
                                c2s.append([a[i][1]-1,a[i][2]])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]]==2 and zuobiao[a[i][1]+4][a[i][2]]==0:#左端是黑棋
                        if a[i][1]+5<=18:
                            if zuobiao[a[i][1]+5][a[i][2]]!=2:
                                c3s.append([a[i][1]+4,a[i][2]])                                    
                            else:pass
                        else:pass
                    else:pass                        
                elif a[i][1]-1<0:#左边在边界
                    if zuobiao[a[i][1]+4][a[i][2]]==0 and zuobiao[a[i][1]+5][a[i][2]]!=2:
                        c3s.append([a[i][1]+4,a[i][2]])                            
                    else:pass
                elif a[i][1]+4>18:#右边在边界
                    if zuobiao[a[i][1]-1][a[i][2]]==0 and zuobiao[a[i][1]-2][a[i][2]]!=2:
                        c2s.append([a[i][1]-1,a[i][2]])                            
                    else:pass
                    

            elif a[i][3]==11:#竖着四个子                    
                if a[i][2]-1>=0 and a[i][2]+4<=18:
                    if zuobiao[a[i][1]][a[i][2]-1]==zuobiao[a[i][1]][a[i][2]+4]==0:#两端都无棋
                        c1s.append([a[i][1],a[i][2]-1])
                        c1e.append([a[i][1],a[i][2]+4])                            
                        break
                    elif zuobiao[a[i][1]][a[i][2]-1]==0 and zuobiao[a[i][1]][a[i][2]+4]==2:#下端是黑棋
                        if a[i][2]-2>=0:
                            if zuobiao[a[i][1]][a[i][2]-2]!=2:
                                c2s.append([a[i][1],a[i][2]-1])                                   
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]][a[i][2]-1]==2 and zuobiao[a[i][1]][a[i][2]+4]==0:#上端是黑棋
                        if a[i][2]+5<=18:
                            if zuobiao[a[i][1]][a[i][2]+5]!=2:
                                c3s.append([a[i][1],a[i][2]+4])                                    
                            else:pass
                        else:pass
                    else:pass#两端都是黑棋
                elif a[i][2]-1<0:#上边在边界
                    if zuobiao[a[i][1]][a[i][2]+4]==0 and zuobiao[a[i][1]][a[i][2]+5]!=2:
                        c3s.append([a[i][1],a[i][2]+4])                            
                    else:
                        pass
                elif a[i][2]+4>18:#下边在边界
                    if zuobiao[a[i][1]][a[i][2]-1]==0 and zuobiao[a[i][1]][a[i][2]-2]!=2:
                        c2s.append([a[i][1],a[i][2]-1])                            
                    else:
                        pass

            elif a[i][3]==12:#右斜四个子                    
                if a[i][1]-1>=0 and a[i][2]-1>=0 and a[i][1]+4<=18 and a[i][2]+4<=18:
                    if zuobiao[a[i][1]-1][a[i][2]-1]==zuobiao[a[i][1]+4][a[i][2]+4]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]-1])
                        c1e.append([a[i][1]+4,a[i][2]+4])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]-1]==0 and zuobiao[a[i][1]+4][a[i][2]+4]==2:#右下端是黑棋
                        if a[i][1]-2>=0 and a[i][2]-2>=0:
                            if zuobiao[a[i][1]-2][a[i][2]-2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]-1])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]-1]==2 and zuobiao[a[i][1]+4][a[i][2]+4]==0:#左上端是黑棋
                        if a[i][1]+5<=18 and a[i][2]+5<=18:
                            if zuobiao[a[i][1]+5][a[i][2]+5]!=2:
                                c3s.append([a[i][1]+4,a[i][2]+4])                                    
                            else:pass
                        else:pass
                    else:pass                        
                elif a[i][1]-1<0 or a[i][2]-1<0:#左上在边界
                    if a[i][1]+4<=18 and a[i][2]+4<=18:
                        if a[i][1]+5<=18 and a[i][2]+5<=18:
                            if zuobiao[a[i][1]+4][a[i][2]+4]==0 and zuobiao[a[i][1]+5][a[i][2]+5]!=2:
                                c3s.append([a[i][1]+4,a[i][2]+4])                                    
                            else:pass
                elif a[i][1]+4>18 or a[i][2]+4>18:#右下在边界
                    if a[i][1]-1>=0 and a[i][2]-1>=0:
                        if a[i][1]-2>=0 and a[i][2]-2>=0:
                            if zuobiao[a[i][1]-1][a[i][2]-1]==0 and zuobiao[a[i][1]-2][a[i][2]-2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]-1])                                    
                            else:pass
                

            elif a[i][3]==13:#左斜四个子                    
                if a[i][1]-1>=0 and a[i][2]+1<=18 and a[i][1]+4<=18 and a[i][2]-4>=0:
                    if zuobiao[a[i][1]-1][a[i][2]+1]==zuobiao[a[i][1]+4][a[i][2]-4]==0:#两端都无棋
                        c1s.append([a[i][1]-1,a[i][2]+1])
                        c1e.append([a[i][1]+4,a[i][2]-4])                            
                        break
                    elif zuobiao[a[i][1]-1][a[i][2]+1]==0 and zuobiao[a[i][1]+4][a[i][2]-4]==2:#右上端是黑棋
                        if a[i][1]-2>=0 and a[i][2]+2<=18:
                            if zuobiao[a[i][1]-2][a[i][2]+2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]+1])                                    
                            else:pass
                        else:pass
                    elif zuobiao[a[i][1]-1][a[i][2]+1]==2 and zuobiao[a[i][1]+4][a[i][2]-4]==0:#左下端是黑棋
                        if a[i][1]+5<=18 and a[i][2]-5>=0:
                            if zuobiao[a[i][1]+5][a[i][2]-5]!=2:
                                c3s.append([a[i][1]+4,a[i][2]-4])                                    
                            else:pass
                        else:pass
                    else:
                        pass                            
                elif a[i][1]-1<0 or a[i][2]+1>18:#左下在边界
                    if a[i][1]+4<=18 and a[i][2]-4>=0:
                        if a[i][1]+5<=18 and a[i][2]-5>=0:
                            if zuobiao[a[i][1]+4][a[i][2]-4]==0 and zuobiao[a[i][1]+5][a[i][2]-5]!=2:
                                c3s.append([a[i][1]+4,a[i][2]-4])                                    
                            else:pass
                elif a[i][1]+4>18 or a[i][2]-4<0:#右上在边界
                    if a[i][1]-1>=0 and a[i][2]+1<=18:
                        if a[i][1]-2>=0 and a[i][2]+2<=18:
                            if zuobiao[a[i][1]-1][a[i][2]+1]==0 and zuobiao[a[i][1]-2][a[i][2]+2]!=2:
                                c2s.append([a[i][1]-1,a[i][2]+1])                                    
                            else:pass


    if c1s!=[]:
        return c1s[0],c1e[0],2
    else:
        if len(c2s)==0 and len(c3s)==0:
            return [],[],2
        elif len(c2s)>=1 and len(c3s)>=1:
            return c2s[0],c3s[0],2
        elif len(c2s)==0 and len(c3s)>=1:
            if len(c3s)>=2:
                return c3s[0],c3s[1],2
            else:
                return c3s[0],[],2
        elif len(c3s)==0 and len(c2s)>=1:
            if len(c2s)>=2:
                return c2s[0],c2s[1],2
            else:
                return c2s[0],[],2
##End-----------------------------------------------------------------------
def findmyself5():
    global win
    global step
    cal=0
    judge=0
    m=0
    for i in range(17):
        for j in range(21):
            for k in range(0,5):
                if(zuobiao[i][j]==2):
                    judge=judge+zuobiao[i+k][j]
                    m=m+1
            if (judge==10 and m==5):
                if(zuobiao[i-1][j]==0):
                    circ=Circle(Point((i-1)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-i][j]=2
                    step=step+1
                    return 2
                elif(zuobiao[i+5][j]==0):
                    circ=Circ(Point((i+5)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i+5][j]=2
                    step=step+1
                    return 2
            judge=0
            m=0

    judge=0
    m=0                              
    for i in range(21):
        for j in range(17):
            for k in range(5):
                if(zuobiao[i][j+k]==2):
                    judge=judge+zuobiao[i][j+k]
                    m=m+1
                if(judge==10 and m==5):
                    if(zuobiao[i][j-1]==0):
                        circ=Circle(Point(i*20,(j-1)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        zuobiao[i][j-1]=2
                        step=step+1
                        return 2
                    elif(zuobiao[i][j+5]==0):
                        circ=Circ(Point(i*20,(j+5)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        zuobiao[i][j+5]=2
                        step=step+1
                        return 2
                judge=0
                m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(21):
            for k in range(5):
                if(i+k<19 and j+k<21):
                    if(zuobiao[i+k][j+k]==2):
                        judge=judge+zuobiao[i+k][j+k]
                        m=m+1
            if(judge==10 and m==5):
                if(zuobiao[i-1][j-1]==0):
                    circ=Circle(Point((i-1)*20,(j-1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-1][j-1]=2
                    step=step+1
                    return 2
                elif(zuobiao[i+5][j+5]==0):
                    circ=Circle(Point((i+5)*20,(j+5)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i+5][j+5]=2
                    step=step+1
                    return 2
            judge=0
            m=0
    judge=0
    m=0
    for i in range(21):
        for j in range(21):
            for k in range(5):
                if(i-k>0 and j+k<21):
                    if(zuobiao[i-k][j+k]==2):
                        judge=judge+zuobiao[i-k][j+k]
                        m=m+1
            if(judge==10 and m==5):
                if(zuobiao[i-1][j+1]==0):
                    circ=Circle(Point((i+1)*20,(j-1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-1][j+1]=2
                    step=step+1
                    return 2
                elif(zuobiao[i-5][j+5]==0):
                    circ=Circle(Point((i-5)*20,(j+5)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-5][j+5]=2
                    step=step+1
                    return 2
            judge=0
            m=0
    if(zuobiao[19][19]==2 and zuobiao[14][14]==0):
        cat=0
        for i in range(0,6):
            cal=cal+zuobiao[19-p][19-p]
            if(zuobiao[19-p][19-p]==1):
                cat=cat+1
        if(cal==10 and cat==5 and zuobiao):
            circ=Circle(Point(280,280),10)
            record.append(circ)
            circ.setFill('black')
            circ.draw(win)
            zuobiao[14][14]=2
            step=step+1
            return 2

def find5():
    global win
    global step
    global zuobiao
    cal=0
    judge=0
    for i in range(17):
        for j in range(21):
            m=0
            judge=0
            for k in range(0,5):
                if(zuobiao[i][j]==1 and zuobiao[i+k][j]!=0):
                    judge=judge+zuobiao[i+k][j]
                    m=m+1
            if (judge==5 and m==5):
                if(zuobiao[i-1][j]==0):
                    circ=Circle(Point((i-1)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-1][j]=2
                    step=step+1
                    return 1
                elif(zuobiao[i+5][j]==0):
                    circ=Circle(Point((i+5)*20,j*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i+5][j]=2
                    step=step+1
                    return 1
    for i in range(21):
        for j in range(17):
            judge=0
            m=0
            for k in range(5):
                if(zuobiao[i][j+k]==1 and zuobiao[i][j+k]!=0):
                    judge=judge+zuobiao[i][j+k]
                    m=m+1
                if(judge==5 and m==5):
                    if(zuobiao[i][j-1]==0):
                        circ=Circle(Point(i*20,(j-1)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        zuobiao[i][j-1]=2
                        step=step+1
                        return 1
                    elif(zuobiao[i][j+5]==0):
                        circ=Circle(Point(i*20,(j+5)*20),10)
                        record.append(circ)
                        circ.setFill('black')
                        circ.draw(win)
                        zuobiao[i][j+5]=2
                        step=step+1
                        return 1
    for i in range(21):
        for j in range(21):
            judge=0
            m=0
            for k in range(5):
                if(i+k<19 and j+k<21):
                    if(zuobiao[i+k][j+k]==1 and zuobiao[i+k][j+k]!=0):
                        judge=judge+zuobiao[i+k][j+k]
                        m=m+1
            if(judge==5 and m==5):
                if(zuobiao[i-1][j-1]==0):
                    circ=Circle(Point((i-1)*20,(j-1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-1][j-1]=2
                    step=step+1
                    return 1
                elif(zuobiao[i+5][j+5]==0):
                    circ=Circle(Point((i+5)*20,(j+5)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i+5][j+5]=2
                    step=step+1
                    return 1
    for i in range(21):
        for j in range(21):
            judge=0
            m=0
            for k in range(5):
                if(i-k>0 and j+k<21):
                    if(zuobiao[i-k][j+k]==1 and zuobiao[i-k][j+k]!=0):
                        judge=judge+zuobiao[i-k][j+k]
                        m=m+1
            if(judge==5 and m==5):
                if(zuobiao[i+1][j-1]==0):
                    circ=Circle(Point((i+1)*20,(j-1)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i+1][j-1]=2
                    step=step+1
                    return 1
                elif(zuobiao[i-5][j+5]==0):
                    circ=Circle(Point((i-5)*20,(j+5)*20),10)
                    record.append(circ)
                    circ.setFill('black')
                    circ.draw(win)
                    zuobiao[i-5][j+5]=2
                    step=step+1
                    return 1
            judge=0
            m=0
    if(zuobiao[19][19]==1 and zuobiao[14][14]==0):
        cat=0
        for i in range(0,6):
            cal=cal+zuobiao[19-p][19-p]
            if(zuobiao[19-p][19-p]==1):
                cat=cat+1
        if(cal==5 and cat==5 and zuobiao):
            circ=Circle(Point(280,280),10)
            record.append(circ)
            circ.setFill('black')
            circ.draw(win)
            zuobiao[14][14]=2
            step=step+1
            return 1
##人机对战------------------------------------------------------------------------- 
def people_computer():
    global record
    global point
    global label1
    global step
    circ=Circle(Point(9*20,9*20),10)
    record.append(circ)
    circ.setFill('black')
    circ.draw(win)
    step=1
    zuobiao[9][9]=2
    while(step<361):
        np=step
        if(step%2!=0):
          np=step+1
        np=np/2
        if(np%2!=0):
          stick=win.getMouse()
          a=stick.getX()
          b=stick.getY()          
          xx=int((a-10)/20)+1
          yy=int((b-10)/20)+1          
          if(peocombutton.clicked(Point(a,b))):
              reset(record)
              point=Point(a,b)
              break
          if(peopeobutton.clicked(Point(a,b))):
              reset(record)
              point=Point(a,b)
              break
          if(quitbutton.clicked(Point(a,b))):
              point=Point(a,b)
              break            
        
          if(0<=xx<=19 and 0<=yy<=19 and zuobiao[xx][yy]==0):
              circ=Circle(Point(xx*20,yy*20),10)
              record.append(circ)
              circ.setFill('white')
              circ.draw(win)
              step=step+1
              zuobiao[xx][yy]=1
              if calculate(zuobiao)==1:
                  lable1.setText("game over")
                  break
              continue
            
        if(np%2==0):
            if(findmyself5()):
                lable1.setText("game over")
                break
            aa,bb,cc=sousuo4(zuobiao)
            if (cc==0 and (step+1)%4==0):
                x,y=aa[0],aa[1]
                centre=Point(x*20, y*20)
                chess=Circle(centre,10)
                record.append(chess)
                chess.setFill("black")
                zuobiao[x][y]=2
                chess.draw(win)
                chess2=Circle(Point(bb[0]*20,bb[1]*20),10)
                record.append(chess2)
                chess2.setFill('black')
                chess2.draw(win)
                step+=2
                lable1.setText("game over")
                break
            elif cc==1:
                x,y=aa[0],aa[1]
                centre=Point(x*20, y*20)
                chess=Circle(centre,10)
                record.append(chess)
                chess.setFill("black")
                zuobiao[x][y]=2
                chess.draw(win)
                step+=1
                lable1.setText("game over")
                break
            if(soukon()):
                continue
            if cc==2:
                if aa!=[]:
                    x,y=aa[0],aa[1]
                    centre=Point(x*20, y*20)
                    chess=Circle(centre,10)
                    record.append(chess)
                    chess.setFill("black")
                    zuobiao[x][y]=2
                    chess.draw(win)
                    x,y=10,10
                    step=step+1
                    continue
            qq,nn,pp=search3(zuobiao)
            if(pp==1):
                circ2=Circle(Point(qq[0]*20,qq[1]*20),10)
                record.append(circ2)
                circ.setFill('black')
                circ.draw(win)
                zuobiao[qq[0]][qq[1]]=2
                step=step+1
            if(find5()):
                continue
            
            if(pp!=1 and qq!=[]):
                circ3=Circle(Point(qq[0]*20,qq[1]*20),10)
                record.append(circ3)
                circ3.setFill('black')
                circ3.draw(win)
                zuobiao[qq[0]][qq[1]]=2
                step=step+1
                continue
            if(sousuo2()):
                continue
            if(sousuo1()):
                continue    

#
#
#-----------------------------------------------------------------
while(True):    
    firstclick=win.getMouse()    
    
    if(quitbutton.clicked(firstclick) or quitbutton.clicked(point)):
        break
    
    if(peopeobutton.clicked(firstclick) or peopeobutton.clicked(point)):
        reset(record)
        while(True):
            stick=win.getMouse()
            np=step
            a=stick.getX()
            b=stick.getY()            
            xx=int((a-10)/20)+1
            yy=int((b-10)/20)+1           
            if(1<=xx<=19 and 1<=yy<=19 and zuobiao[xx][yy]==0):
                asureX.append(xx)
                asureY.append(yy)
                circ=Circle(Point(xx*20,yy*20),10)
                record.append(circ)
                if(step%2!=0):
                    np=step+1
                np=np/2
                if(np%2==0):
                    color=circ.setFill('black')
                    zuobiao[xx][yy]=1
                else:
                    color=circ.setFill('white')
                    zuobiao[xx][yy]=2
                step=step+1
                circ.draw(win)
                if(calculate(zuobiao)):
                    lable1.setText("game over")
                    break
            
            if(quitbutton.clicked(Point(a,b))):
                point=Point(a,b)
                break
            if(peopeobutton.clicked(Point(a,b))):
                reset(record)
                point=Point(a,b)
                break
            if(huiqibutton.clicked(Point(a,b))):                
                huiqi()
            if(peocombutton.clicked(Point(a,b))):
               reset(record)
               point=Point(a,b)
               people_computer()

    if(peocombutton.clicked(firstclick) or peocombutton.clicked(point)):
        reset(record)
        people_computer()
    if(peocombutton.clicked(point)):
        reset(record)
        people_computer()
    if(quitbutton.clicked(point)):        
        break
win.close()

