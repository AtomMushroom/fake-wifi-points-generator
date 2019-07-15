#!/usr/bin/python3
from os import system

def monitor_mode_start(interface):
    system('airmon-ng start ' + interface)

def monitor_mode_stop(interface):
    system('airmon-ng stop ' + interface + 'mon')