#coding=utf-8 
'''
This example is for multithreading deadlock demo.
'''
import time 
import threading 
class Account: 
    def __init__(self, _id, money, lock): 
        self.id = _id 
        self.money = money 
        self.lock = lock 
    
    def withdraw(self, amount): 
        self.money -= amount 
 
    def deposit(self, amount): 
        self.money = amount 
 
def transfer(_from, to, amount): 
    if _from.lock.acquire():#鎖住自己的賬戶 
        _from.withdraw(amount)
        time.sleep(1)#讓交易時間變長，2個交易執行緒時間上重疊，有足夠時間來產生死鎖
        print('wait for lock...')
    if to.lock.acquire():#鎖住對方的賬戶 
        to.deposit(amount) 
        to.lock.release() 
    _from.lock.release()
    print('finish...')

a = Account('a', 1000, threading.Lock()) 
b = Account('b', 1000, threading.Lock()) 
threading.Thread(target = transfer, args = (a, b, 100)).start() 
threading.Thread(target = transfer, args = (b, a, 200)).start()