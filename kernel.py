#********************************************
# by t90_val (github)                       *
# v 2.0                                     *
# language: python 3 , bash                 *
#********************************************
# pip install wmi
# pip install logging
# pip install keyboard
# pip install numpy
# pip install colorama
# pip install requests
import wmi
from os import *
import time
import random
import os
import datetime
import logging
import colorama
from colorama import *
import math
import requests
import getpass
import sys
import socket
from settings import *
from pkg_manager import *
from sys_prog.client_server import *
init()

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

clear()

nameuserdefault = "User#"
nameuseradmin = "admin$"
dt_now = datetime.datetime.now()
imptyfs = getpass.getpass



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

# функция которая получает локалный айпи
# function that gets local ip
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)
    return local_ip


# цикл команд
# command cycle
def core():
    while True:

        inputp = input(Fore.GREEN + nameuserdefault + " " + Style.RESET_ALL)
        if inputp == "systeminfo":
            print("based python 3")
            print("kernel pynext|version 2.0|")
            infopc()
        if inputp == "clear":
            clear()
        if inputp == "sudo":
            inputp = input(Fore.RED + nameuseradmin + " " + Style.RESET_ALL)
        if inputp == "help":
            print("systeminfo\nclear\nsudo\nping\nlocal_ip\nstop_kernel\nls\nmkdir\nrm_dir\nserver\nclient\npkg")
        if inputp == "datatime":
            print(dt_now)
        if inputp == "ping":
            inptehttp = input("(example https://google.com)ping_site>>> ")
            reshttp = requests.get(inptehttp)
            print(reshttp)
        if inputp == "local_ip":
            get_local_ip()
        if inputp == "stop_kernel":
            sys.exit()
        if inputp == "ls":
            print(os.getcwd())
        if inputp == "dir":
            print("error: maybe you mean ls?")
        if inputp == "mkdir":
            inpte = input("mkdir_name>>> ")
            os.mkdir(inpte)
        if inputp == "rm_dir":
            inpter = input("rm_dir>>> ")
            os.rmdir(inpter)
        if inputp == "server":
            start_server()
        if inputp == "client":
            start_client()
        if inputp == "pkg":
            pkg_files()

def password_check():
    print("kernel pynext")
    passwordinpte = imptyfs("password>>> ")

    if passwordinpte == password_PATH:
        print("successfully")
        clear()
        core()

    else:
        print("access denied")
        time.sleep(1)
        sys.exit()
