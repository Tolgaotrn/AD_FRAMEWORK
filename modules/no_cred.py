import subprocess
from  modules.general.nmap import *
from  modules.general.dc_enemuration import *
class NoCred:
    def __init__(self):
        pass

    def run(self):
        print("\n[+] No Credentials section is starting \n")
        print("1. Networ Discovery - with nmap ")
        print("2. Find DC ip")
        print("3. Anonymous access on SMB shares")

        choice = input("\n Enter your choice:  ")

        if choice == "1":
            target = input("\nTarget IP: ")
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

        elif choice == "2":
           find_dc_ip()
        elif choice == "3":
            self.run_anonymous_access_on_smb_shares()
        else:
            print("\n[-] Invalid option! Please try again.")
            self.run()


    #it could be also in modules for later using for exploit

    def run_anonymous_access_on_smb_shares(self):
        
        ip_range = input("\nPlease provide a ip range: ")
        command = f'nxc smb f{ip_range}'
        if command:
            print(f"\n Running command: {command}")

        try:
            result = subprocess.run(command, shell=True, text=True)
            if result.returncode == 0:
                print("\n[+] Command executed successfully!")
            else:
                print("\n[-] ERROR: Command executed unsuccessfully!")
        except Exception as e:
            print(f"\n[-] Exception: {e}")