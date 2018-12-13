# Defining class with first extra parameter

# importing inbuilt libraries for ease of utility
import time
import random
import thread
import sys
import logging

class Station(object):
  
<<<<<<< HEAD
  flag = False
  
  # Init method or constructor
  def __init__(self,name,type_id,id): 
    self.name = name 
    self.type_id = type_id
    self.id = id
    
  # Counters play the role in keeping a check that execution shoud occur only after initialization
  
  #cnt1 = 0
  #cnt2 = 0
  
  #function to initialize station
  def init_station(self):
  
    print('Hello, my name is',self.name)
    
    #global cnt1
    #cnt1 += 1
    time.sleep(5)
    self.flag=True
  
  # function taking only integral routine ids from 1,2 or 3   
  def execute_routine(self,routine_id):
    
    #global cnt2
    #cnt2 += 1
    #flag=False
    # Check on station to be initialized before execution  
    if(self.flag == False):
      print("Station not initialized")  
      #logging.warning('%s before you %s', 'Execution', 'Initialization!')
      return
    else:
      # Check on the id of routine  
      if(routine_id<1 or routine_id>3):
        print("routine_id out of bound. Insert integral values 1,2 or 3 only")
    
      # Three different function calls
    
      if(routine_id == 1):
        #print("1")
      
        #function call inside another function
        c.method1()
      
     
      if(routine_id == 2):
        #print("2")
        c.method2()
      

      
      if(routine_id == 3):
        #print("3")
        c.method3()

    # Check that every routine should return an unique response code after a delay of 5 seconds.  
    time.sleep(5)  
    
  # function to reset al the variables  
  def shutdown_station(self): 
    #print("bye")
    print('Hello, what is your type ID',self.type_id)

    #global cnt1
    #cnt1 = 0
    self.flag = False
    #global cnt2
    #cnt2 = 0
    
  time.sleep(5)  
    
=======
  # Init method or constructor
  def __init__(self,name,type_id,id): 
    self.name = name 
    self.type_id = type_id
    self.id = id
    
  # Counters play the role in keeping a check that execution shoud occur only after initialization
  cnt1 = 0
  cnt2 = 0
  
  #function to initialize station
  def init_station(self):
  
    print('Hello, my name is',self.name)
    
    global cnt1
    cnt1 += 1
    
  time.sleep(5)   
    
  # function taking only integral routine ids from 1,2 or 3   
  def execute_routine(self,routine_id):
    
    global cnt2
    cnt2 += 1
    
    # Check on station to be initialized before execution  
    if(cnt2 > cnt1):
      print("Station not initialized")  
      #logging.warning('%s before you %s', 'Execution', 'Initialization!')
      return
      
    # Check on the id of routine  
    if(routine_id<1 or routine_id>3):
      print("routine_id out of bound. Insert integral values 1,2 or 3 only")
    
    # Three different function calls
    
    if(routine_id == 1):
      #print("1")
      
      #function call inside another function
      c.method1()
      
     
    if(routine_id == 2):
      print("2")
      c.method2()
      

      
    if(routine_id == 3):
      #print("3")
      c.method3()

  # Check that every routine should return an unique response code after a delay of 5 seconds.  
  time.sleep(5)  
    
  # function to reset al the variables  
  def shutdown_station(self): 
    print("bye")

    global cnt1
    cnt1 = 0
    
    global cnt2
    cnt2 = 0
    
  time.sleep(5)  
    
>>>>>>> 04f157de3d82d77ce032b7a0f7d6eda24be41ca8
  def method1(self):
    print("1")
    
  def method2(self):
    print("2")    
  
  def method3(self):
    print("3")
    
if __name__ == '__main__':
   
    
  # Heirarchy of function calls
 
  c = Station('Dhwani','2015','01054')
  
<<<<<<< HEAD
  c.execute_routine(4)
=======
>>>>>>> 04f157de3d82d77ce032b7a0f7d6eda24be41ca8
  c.init_station()
  c.execute_routine(1)
  #c.Init_station()
  c.shutdown_station()
<<<<<<< HEAD
  c.execute_routine(2)
=======
  c.execute_routine(2)
>>>>>>> 04f157de3d82d77ce032b7a0f7d6eda24be41ca8
