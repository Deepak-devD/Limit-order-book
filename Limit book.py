
from tabulate import tabulate
def marketOrder(share,buySell,buy,sell):
    l=[[]]
    
    if buySell==1:
        l=buy
        s=share
        while True:
            x,y=min(l)
            a=[]

            if(s <= y):
                y=y-s
                a.append(x)
                a.append(y)
                del l[len(l)-1]
                l.append(a)
                return tabulate(l,headers=["Price","Ask Size"])
            else:
                if s>y:
                    s=s-y
                    del l[len(l)-1]
    else:
        l=sell
        s=share
        while True:
            x,y=max(l)
            a=[]

            if(s <= y):
                y=y-s
                a.append(x)
                a.append(y)
                del l[len(l)-1]
                l.append(a)
                return tabulate(l[::-1],headers=["Price","Ask Size"])
            else:
                if s>y:
                    s=s-y
                    del l[len(l)-1]
        

def limitOrder(share,buySell,buy,sell,limit):
    if(buySell==1):
        l=[]
        for i in range(len(buy)):
            l.append(buy[i][0])
        
            
        while True:
            if limit in l:
                c=l.index(limit)
                buy[c][1]=buy[c][1]-share
                return tabulate(buy,headers=["Price","Ask Size"])
            else:
                print('Shares are not available at that limit')
                return 0 
                   

    else :
        l=[]
        for i in range(len(sell)):
            l.append(sell[i][0])
        
            
        while True:
            if limit in l:
                c=l.index(limit)
                sell[c][1]=sell[c][1]-share
                return tabulate(sell,headers=["Price","Ask Size"])
            else:
                print('Shares are not available at that limit')
                return 0





if __name__=="__main__":

    # Entering the buy side of the limit book 
    
    b = int(input("Enter the number of levels for buy side of the book : "))
    buy=[]
    print("Enter price and then ask size : ")
    for i in range(b):          
        arr =[]
        for j in range(2):      
            arr.append(float(input()))
        buy.append(arr)
    
    


    
    buy = sorted(buy,key=lambda l:l[0],reverse= True) 


    # Entering the selling side of the book
    
    s = int(input("Enter the number of levels for sell side of the book : "))
    sell=[]
    print("Enter price and then bid size : ")  # in first line price 
    for i in range(s):                         # in next line size of share          
        c =[]
        for j in range(2):      
            c.append(float(input()))
        sell.append(c) 

    

    sell = sorted(sell,key=lambda l:l[0],reverse= False)

    print(tabulate(buy, headers=["Price","Ask Size"]))

    print(tabulate(sell, headers=["Price","Bid Size"]))
    
    share=int(input('Enter the number of shares you want to buy/sell from list :'))
    buySell=int(input('Press 1 to buy, 2 to sell :'))
    order=int(input("1.Market order 2.Limit order :"))
    if(order==1):
        print(marketOrder(share,buySell,buy,sell))
    elif(order==2):
        limit=float(input("Enter limt value :"))
        print(limitOrder(share,buySell,buy,sell,limit))
    
    
