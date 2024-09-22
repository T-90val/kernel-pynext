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
            print("kernel not found.")
            sys.exit(1)
        print(f"loading kernel")
        clear()
        self.load_kernel()
        self.display_logo()
        self.wait()
        core()


bootloader = bootloader()
bootloader.__init__()
bootloader.load_kernel()