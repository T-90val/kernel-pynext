from kernel import *
import pyfiglet

class bootloader:
    def __init__(self):
        self.path_kernel = 'kernel.py'
        self.boot_timeout = 3

    def wait(self):
        time.sleep(self.boot_timeout)

    def display_logo(self):
        self.logo_text = 'py-next'
        self.ascii_logo = pyfiglet.figlet_format(self.logo_text, font='Big_Money-ne')
        print(self.ascii_logo)

    def load_kernel(self):
        if not os.path.exists(self.path_kernel):
            print(Fore.RED + "kernel not found." + Style.RESET_ALL)
            time.sleep(2)
            sys.exit(1)
        else:
            print(f"loading kernel")
            clear()
            self.display_logo()
            self.wait()
            password_check()


bootloader = bootloader()
bootloader.__init__()
bootloader.load_kernel()
