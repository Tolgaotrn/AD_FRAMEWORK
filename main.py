#import sys
#from colorama import Fore, Back, Style, init
#from modules.no_cred.no_cred import NoCred
#from modules.valid_user_no_pass.no_pass import ValidUser
#from modules.valid_creds.valid_creds import ValidCreds
from core.console import Shell
from core.console import MODULES




if __name__ == "__main__":
    print("""
    
 █████╗ ██████╗     ██████╗ ███████╗███╗   ██╗████████╗███████╗███████╗████████╗    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗    ██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
███████║██║  ██║    ██████╔╝█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗   ██║       █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██╔══██║██║  ██║    ██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║   ██║       ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║  ██║██████╔╝    ██║     ███████╗██║ ╚████║   ██║   ███████╗███████║   ██║       ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═╝╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                                                                  
    """)
    print("This Framework is based on the Active Directory MindMap made by Orange CyberDefense")




    print("Available modules:\n")
    print("-"*50)
    for module in MODULES:
        print(f"    🟡 {module}")
        print("-"*50)
    print("\nType 'use <module>' to start or 'modules' to show this list\n")


    Shell().run()
