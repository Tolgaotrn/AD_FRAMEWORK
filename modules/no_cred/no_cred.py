import subprocess
import sys
import os
from utils.nmap import *
from utils.dc_enumeration import *
from colorama import Fore, Style, init
from core.module_base import ModuleBase

init()

class NoCred(ModuleBase):
    def __init__(self):
        super().__init__()
        self.name = "no_creds"
        self.options = {
            "ip": None,
            "domain": None
        }
        self.actions = {
            "nmap": self.network_discovery,
            "find_dc_ip": find_dc_ip,
            "anon_smb_share": self.run_anonymous_access_on_smb_shares,
            "users_enumeration": self.enumerate_users,
            "bruteforcing_rid": self.bruteforce_users,
            "smb_poisoning": self.smb_poisoning,
            "zone_transfer": self.zone_transfer,
        }

    def prepare(self):
        ip = self.options["IP"]
        if not ip:
            print("[-] Need IP")
            return None
        ip_list = get_input_or_file(ip)
        return ip_list

    def banner(self):
        print(Fore.MAGENTA + f"\n🔥 MODULE {self.name.upper()} 🔥 \n" + Style.RESET_ALL)
        print("\n See options and set a target with 'options'\n")


    ##############

    def network_discovery(self):
        #target = input("\nTarget IP: ")
        target = self.options["ip"] 
        if not target:
            print("\n[-] Target IP cannot be empty!")
            self.run()

        options_check = input("\nDo you have any specific options for nmap? (Y/N): ").strip().upper()

        if options_check == 'Y':
            options = input("Please provide valid options (e.g., -Pn -sC -sV -p- -oA): ")
            if options:
                run_nmap(target=target, options=options)
            else:
                print("\n[-] No options provided. Running with default settings...")
                run_nmap(target=target)
        elif options_check == 'N':
            print("\n[+] Running with default options...")
            run_nmap(target=target)
        else:
            print("\n[-] Invalid option! Please enter Y or N.")
            self.run()

    def run_anonymous_access_on_smb_shares(self):
        #ip_range = input("\nPlease provide an IP range: ").strip()
        ip_range = self.options["ip"]
        if not ip_range:
            print("[-] IP range cannot be empty!")
            return

        command = f'nxc smb {ip_range}'
        print(f"\n🟡 Running command: {command}")

        try:
            result = subprocess.run(command, shell=True, text=True)
            if result.returncode == 0:
                print("\n✅ Command executed successfully!")
            else:
                print("\n❌ ERROR: Command executed unsuccessfully!")
        except Exception as e:
            print(f"\n[-] Exception: {e}")

    def enumerate_users(self):
        #dc_ip = input("\nPlease provide a DC IP: ")
        dc_ip = self.options["ip"]
        if not dc_ip:
            print("[-] DC IP cannot be empty!")
            return

        command = f'nxc smb {dc_ip} --rid-brute 10000'
        try:
            result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                output = result.stdout.strip().split('\n')
                if output:
                    print("\n[+] Enumerated users:")
                    for line in output:
                        print(f"    {line}")
                else:
                    print("\n[-] No users found!")
            else:
                print(f"\n[-] Error: {result.stderr}")
        except Exception as e:
            print(f"\n[-] Exception: {e}")

    def bruteforce_users(self):
        #domain = input("\nPlease provide a domain name: ")
        domain = self.options["domain"]
        #dc_address = input("Domain controller IP address: ")
        dc_address = self.options["domain"]
        userlist_path = input("Please provide a user list file path: ")

        if not (domain and dc_address and userlist_path):
            print("\n[-] ERROR: Please provide a valid domain name, DC IP address, and user list file path.")
            return
        current_dir = os.getcwd()
        userlist = os.path.join(current_dir, userlist_path)
        if not os.path.isfile(path=userlist_path):
            print("\n[-] ERROR: File with given path not found.. ")
            return 
        command = f'kerbrute userenum -d {domain} --dc {dc_address} {userlist}'
        print(f"\n[+] Running command: {command}")

        try:
            result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                print('\n[+] Usernames found successfully!')
                output = result.stdout.strip().split('\n')
                for line in output:
                    print(f"    {line}")
            else:
                print(f'\n[-] Error: {result.stderr}')
        except Exception as e:
            print(f'\n[-] Exception: {e}')

    ##Responder need root priv .. use another tool or add it sudoers 
    def smb_poisoning(self):
        print("\nSMB Poisoning is starting...")
        interface = input("Please provide a interface: ")
        if not interface:
            print(f"\nERROR: Not valid interface name!")
        try:
            # command = f'sudo responder -I {interface}'
            command = ['sudo', 'responder', '-I', interface]

            result = subprocess.run(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print("SMP Posinong is successfull..")
            else:
                print(f'\n[-] ERROR: {result.stderr.decode('utf-8')}')

        except Exception as e:
            print(f'\n[-] Exception: {e}')

    def zone_transfer(self):
        print("\nZone transfer search is starting...")
        ip_range = input("Please provide a ip range: ")
        if not ip_range:
            print("Ip range should be valid")
            return 
        try:
            command = ['nmap', '-p', '88', '--open',ip_range]
            result = subprocess.run(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.decode('utf-8').strip()
                print(f"\n[+] Zone transfers found...\n")
            else:
                error_output = result.stderr.decode('utf-8').strip()

                print(f'\nThere is no zone transfer found...:\n{error_output}')
        except Exception as e:
            print(f'\n[-] Exception: {e}')


