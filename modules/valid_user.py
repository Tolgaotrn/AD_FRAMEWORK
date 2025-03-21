import subprocess
import os
from colorama import Fore, Style, init

# Initialize colorama for colored output
init()

class NoCred:
    def __init__(self):
        pass

    # Execute a command and capture the output
    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"[-] Error: {result.stderr.strip()}"
        except Exception as e:
            return f"[-] Exception: {e}"

    # Read a file and return non-empty lines
    def read_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except Exception as e:
            print(f"[-] Error reading {file_path}: {e}")
            return []

    # Handle input as a file or direct value
    def get_input_or_file(self, input_value):
        if os.path.isfile(input_value):
            return self.read_file(input_value)
        return [input_value]

    ######### MODULES ###########

    # Nmap Network Discovery
    def network_discovery(self, target, options=None):
        command = f"nmap {options} {target}" if options else f"nmap {target}"
        print(f"\n[+] Running command: {command}")
        result = self.run_command(command)
        print(result)

    # Find Domain Controller IP
    def find_dc_ip(self):
        command = "nxc smb --find-dc"
        print(f"\n[+] Running command: {command}")
        result = self.run_command(command)
        print(result)

    # Anonymous SMB Share Access
    def anonymous_access_on_smb_shares(self, ip_range):
        command = f"nxc smb {ip_range}"
        print(f"\n[+] Running command: {command}")
        result = self.run_command(command)
        print(result)

    # User Enumeration using RID bruteforce
    def enumerate_users(self, dc_ip):
        command = f"nxc smb {dc_ip} --rid-brute 10000"
        print(f"\n[+] Running command: {command}")
        result = self.run_command(command)
        if result:
            print("\n[+] Enumerated users:")
            for line in result.split("\n"):
                print(f"    {line}")

    # Bruteforce Usernames
    def bruteforce_users(self, domain, dc_address, userlist):
        command = f"kerbrute userenum -d {domain} --dc {dc_address} {userlist}"
        print(f"\n[+] Running command: {command}")
        result = self.run_command(command)
        if result:
            print("\n[+] Usernames found successfully!")
            for line in result.split("\n"):
                print(f"    {line}")

    ######### INTERFACE ##########

    def run(self):
        print(Fore.BLUE + "\n🔥 MODULE NO CRED 🔥\n" + Style.RESET_ALL)
        print("1. Network Discovery - with nmap")
        print("2. Find DC IP")
        print("3. Anonymous access on SMB shares")
        print("4. User Enumeration")
        print("5. Bruteforcing usernames")

        choice = input("\nYour choice (1/2/3/4/5): ").strip()

        if choice == "1":
            target = input("\nTarget IP: ").strip()
            if not target:
                print("[-] Target IP cannot be empty!")
                return
            options_check = input("\nDo you have any specific options for nmap? (Y/N): ").strip().upper()
            options = input("Please provide options (e.g., -Pn -sC -sV): ") if options_check == 'Y' else None
            self.network_discovery(target, options)

        elif choice == "2":
            self.find_dc_ip()

        elif choice == "3":
            ip_range = input("\nPlease provide an IP range: ").strip()
            if not ip_range:
                print("[-] IP range cannot be empty!")
                return
            self.anonymous_access_on_smb_shares(ip_range)

        elif choice == "4":
            dc_ip = input("\nPlease provide a DC IP: ").strip()
            if not dc_ip:
                print("[-] DC IP cannot be empty!")
                return
            self.enumerate_users(dc_ip)

        elif choice == "5":
            domain = input("\nPlease provide a domain name: ").strip()
            dc_address = input("Domain controller IP address: ").strip()
            userlist = input("Please provide a user list file path: ").strip()
            if not (domain and dc_address and userlist):
                print("[-] ERROR: Missing required information.")
                return
            self.bruteforce_users(domain, dc_address, userlist)

        else:
            print("[-] Invalid choice! Please try again.")
            self.run()


if __name__ == "__main__":
    no_cred = NoCred()
    no_cred.run()
