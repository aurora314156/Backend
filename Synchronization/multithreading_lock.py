#coding=utf-8 
'''
This example is for concurrent process operate same data demo.
'''
import concurrent.futures
import time
import threading
  
class DB:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print("Thread ", name , "is reading the DB value")
        self._lock.acquire()
        print("Thread ", name , "has received the lock")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print("Thread ", name ,"has modified the DB value")
        print("Thread ", name, "is releasing the lock")
        self._lock.release()
        
database = DB()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    for index in range(3):
        executor.submit(database.update, index+1)

print("DB Value is", database.value) 