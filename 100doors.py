#!/usr/bin/env python 3

#0: opened state
#1: closed state

# list of doors at the beginning
doors=[0]*100

def Toggle():
    '''Function of openning and closing of the appropriate doors.
       i=index '''
    global doors
    for step in range(1,101):
        i=step-1
        while i<len(doors):   
            if doors[i]==0: 
                doors[i]=1
            elif doors[i]==1:
                doors[i]=0
            i+=step

def Print():
    '''Function of printing data in appropriate form.'''
    l=[]
    for i in range(0,100):
        if doors[i]==1:
            l.append(i+1) 
    s=", "   
    print("The following doors are open: ", s.join(str(x) for (x) in l))

Toggle()
Print() 