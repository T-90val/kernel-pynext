#********************************************
# by t90_val (github)                       *
# v3.0                                      *
# language: python 3 , bash                 *
#********************************************
import wmi  
import time
import datetime
from colorama import *
import getpass
import sys
from sys_prog.pkg_manager import *
from sys_prog.client_server import *
import shutil
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

def clear_cache():
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        if os.path.isdir(item) and item == '__pycache__':
            shutil.rmtree(item)
            print('cache has been deleted')


# цикл команд
# command cycle
def core():
    while True:

        inputp = input(Fore.GREEN + nameuserdefault + " " + Style.RESET_ALL)
        if inputp == "systeminfo":
            print("based python 3")
            print("kernel pynext|version 3.0|")
            infopc()
        elif inputp == "clear":
            clear()
        elif inputp == "sudo":
            inputp = input(Fore.RED + nameuseradmin + " " + Style.RESET_ALL)
        elif inputp == "help":
            print("systeminfo\nclear\nsudo\nping\nlocal_ip\nstop_kernel\nls\nmkdir\nrm_dir\nserver\nclient\npkg\nclear_cache")
        elif inputp == "datatime":
            print(dt_now)
        elif inputp == "ping":
            inptehttp = input("(example https://google.com)ping_site>>> ")
            reshttp = requests.get(inptehttp)
            print(reshttp)
        elif inputp == "local_ip":
            get_local_ip()
        elif inputp == "stop_kernel":
            print(Fore.RED +"Warning: ARE YOU SURE?\nIf yes then write yes, if no then write no"+ Style.RESET_ALL)
            stop_kernel_input = input(">>>")
            if stop_kernel_input == "yes":
                sys.exit()
            elif stop_kernel_input == "no":
                print()
        elif inputp == "ls":
            print(os.getcwd())
        elif inputp == "dir":
            print("error: maybe you mean ls?")
        elif inputp == "mkdir":
            inpte = input("mkdir_name>>> ")
            os.mkdir(inpte)
        elif inputp == "rm_dir":
            inpter = input("rm_dir>>> ")
            os.rmdir(inpter)
        elif inputp == "server":
            start_server()
        elif inputp == "client":
            start_client()
        elif inputp == "pkg":
            pkg_files()
        elif inputp ==  "clear_cache":
            clear_cache()
        else:
            print(f'{Fore.RED} not found command {inputp} {Style.RESET_ALL}')

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
