#!/usr/bin/python3
import random
from os import system

class color:
        Green = '\033[32m'
        Red = '\033[31m'
        Blue = '\033[34m'

symbols = '1234567890ABCDEF'
symbols_countable = '02468ACE'
numbers = '123456789'

ls1 = list(symbols)
ls2 = list(symbols_countable)
ls3 = list(numbers)

def create_access_point(mac, name, channel):
    command = 'airbase-ng -a ' + mac + ' --essid "' + name + '" -c ' + channel + ' wlan0mon'
    system('gnome-terminal -e "' + command + '"')

def main(access_points):
    for point in range(access_points):
        random.shuffle(ls1)
        random.shuffle(ls2)
        random.shuffle(ls3)
        part1 = ''.join([random.choice(ls2) for m in range(2)])
        part2 = ''.join([random.choice(ls1) for m in range(2)])
        part3 = ''.join([random.choice(ls1) for m in range(2)])
        part4 = ''.join([random.choice(ls1) for m in range(2)])
        part5 = ''.join([random.choice(ls1) for m in range(2)])
        part6 = ''.join([random.choice(ls1) for m in range(2)])
        name = ''.join([random.choice(ls1) for n in range(10)])
        channel = ''.join([random.choice(ls3) for c in range(1)])
        mac = part1 + ':' + part2 + ':' + part3 + ':' + part4 + ':' + part5 + ':' + part6
        create_access_point(mac, name, channel)

def killall():
        system('killall airbase-ng')