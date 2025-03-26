import sys
#from colorama import Fore, Back, Style, init
#from modules.no_cred.no_cred import NoCred
#from modules.valid_user_no_pass.no_pass import ValidUser
#from modules.valid_creds.valid_creds import ValidCreds
from core.console import Shell
from core.console import MODULES





def show_help():
    print("\n📌 Available commands:")
    print("  modules         - Show available modules")
    print("  use <module>    - Load a module")
    print("  options         - Show module options and actions (if module is loaded)")
    print("  set <opt> <val> - Set a module option")
    print("  run <action>    - Run a specific action from the loaded module")
    print("  run all         - Run all actions from the loaded module")
    print("  back            - Unload current module")
    print("  exit, quit      - Exit the framework\n")

if __name__ == "__main__":

    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
        sys.exit(0)


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


