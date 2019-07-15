#!/usr/bin/python3

# Fake WIFI points generator
# By AtomMushroom
from core.core import * # main(access_points) | create_access_point(mac, name, channel) | killall()
from core.monitor import * # monitor_mode_start(interface) | monitor_mode_stop(interface)
from os import system

system('reset')

logo = '''                                                                               
      IMMMMMMMMMI                0              IIMMMMMMMMII                    
     7MMMMMMMMMMM7                             IMMMMMMMMMMMM7          1        
   ~~MMM==, ,==NMM==                          ~MMMM+,   =NMMM=                  
   OOMM~       ~MM88                          OMMM~      ~MMM8                  
  =MMM=         ~MMM+            1           =MM=~        ~~MM+                 
  IMMM,     0   ,MMM7                        IMM::   1    ,,MM7                 
  $MMM           NMM8                        ZMM            NM8                 
  8MMM           ZMMM                        8MM       1    ZMM                 
  NMMD     1     ZMMM                        NMD            $MM                 
  OMMM           OMMM      0                 OMM            ZMM                 
  $MMM   0       NMM8                        ZMM            NM8                 
  ?MMM:         ,MMM7                 0      IMM::  0     ,,MM7                 
  :MMM$         7MMM:                        :MM$$        77MM~                 
   OOMM~       ~MM88                          OMMM~      ~MMM8                  
   ~~MMM==, ,==NMM==        1                 ~MMMM+,   =NMMM=        0         
     IMMMMMMMMMMM7                             IMMMMMMMMMMMM7                   
       :??ZDZ?I~                   1   0          ~?ZDDZI~                      
                            1                                                                                                               
    1                                                                         
                      :MMMMMMMMMMMMMMMMMMM:                      0              
        0             :MMMMMMMMMMMMMMMMMMM:                                     
                      :NMMMMMMMMMMMMMMMMMM,

                   FAKE WIFI POINTS GENERATOR
                   By AtomMushroom'''
print(color.Green + logo)
help = '''
1) Enable monitor mode
2) Create fake random WIFI points
3) Create fake WIFI point
4) Disable monitor mode
5) Kill all fake points
6) Exit
'''
print(color.Blue + help)
monitor = False

while True:
    todo = input(' >>> ')
    if todo == '1':
        interface = input('Enter interface name (ex. wlan0)> ')
        monitor_mode_start(interface)
        monitor = True
        print('MONITOR MODE STARTED')
    elif todo == '2':
        if monitor == True:
            access_points = int(input('Enter the number of WIFI points> '))
            main(access_points)
            print('COMPLEATED')
        else:
            print('ERROR! Please, start monitor mode')
    elif todo == '3':
        if monitor == True:
            mac = input('Enter MAC (from 00:00:00:00:00:00 to FF:FF:FF:FF:FF:FF)> ')
            name = input('Enter name of WIFI point> ')
            channel = input('Enter channel of WIFI point (from 1 to 9)> ')
            create_access_point(mac, name, channel)
            print('ACCESS POINT CREATED')
        else:
            print('ERROR! Please, start monitor mode')
    elif todo == '4':
        if monitor == True:
            monitor_mode_stop(interface)
            print('MONITOR MODE STOPPED')
        else:
            print('ERROR! You have not turned on monitor mode to turn it off')
    elif todo == '5':
        killall()
        print('KILLED')
    elif todo == '6':
        print('EXIT ')
        break
    else:
        print(help)