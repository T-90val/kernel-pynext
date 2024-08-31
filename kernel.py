# pip install wmi
# pip install logging
# pip install keyboard
# pip install numpy
# pip install colorama
# pip install requestsp
import wmi
from os import *
import time
import random
import os
import datetime
import logging
import keyboard
from numpy import exp, array, random, dot
import colorama
from colorama import *
import math
import requests
init()


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

print("kernel pynext")

clear()

nameuserdefault = "User#"
nameuseradmin = "admin$"
dt_now = datetime.datetime.now()

# получение информации  пк
# getting pc information
def infopc():
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]

    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # из килобайт в мегабайт (не точно) # from kilobytes to megabytes (not exact)

    print('CPU: {0}'.format(proc_info.Name))
    time.sleep(0.5)
    print('RAM: {0} GB'.format(system_ram))
    time.sleep(0.5)

# мини ии(это не ии а точный калькулятор)
# mini ai (this is not ai but a precise calculator)
def ai_mini_hi():
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T
    random.seed(1)
    synaptic_weights = 2 * random.random((3, 1)) - 1
    ai_inpute = input("number>>> ")
    ai_inpute = int(ai_inpute)
    for iteration in range(ai_inpute):
        output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    print(1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))

# цикл команд
# command cycle
while True:
    inputp = input(Fore.GREEN + nameuserdefault + " " + Style.RESET_ALL)
    if inputp == "systeminfo":
        print("kernel pynext|version 1.0|")
        infopc()
    if inputp == "aih":
        ai_mini_hi()
    if inputp == "clear":
        clear()
    if inputp == "sudo":
        inputp = input(Fore.RED + nameuseradmin + " " + Style.RESET_ALL)
    if inputp == "help":
        print("systeminfo\naih\nclear\nsudo")
    if inputp == "datatime":
        print(dt_now)