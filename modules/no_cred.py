import subprocess
from  modules.general.nmap import *
class NoCred:
    def __init__(self):
        pass

    def run(self):
        print("\n[+] No Credentials section is starting \n")
        print("1. Networ Discovery - with nmap ")
       

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
            return
        else:
            print("\n[-] Invalid option! Please try again.")
            self.run()

