# core/console.py

from modules.valid_user_no_pass.no_pass import ValidUser
from modules.no_cred.no_cred import NoCred
from modules.valid_creds.valid_creds import ValidCreds 
from colorama import Fore, Style, init
import readline

init()

MODULES = {
    "valid_user": ValidUser,
    "no_cred": NoCred,
    "valid_creds": ValidCreds,
}

MODULES_COLORS = {
    "valid_user" : Fore.BLUE,
    "no_cred" : Fore.MAGENTA
}


class Shell:
    def __init__(self):
        self.current_module = None
        self.module_instance = None

    def run(self):
        while True:
            color = MODULES_COLORS.get(self.current_module, Fore.CYAN)
            prompt = f"[ProjectSS/[{color}{self.current_module}{Style.RESET_ALL}] > " if self.current_module else "[Project SS] > "
            cmd = input(prompt).strip()

            if cmd in ["exit", "quit"]:
                print("👋 Bye!")
                break

            elif cmd == "modules":
                print("\nAvailable modules:")
                for name in MODULES:
                    print(f"  • {name}")
                print()

            elif cmd.startswith("use "):
                name = cmd.split(" ", 1)[1]
                if name in MODULES:
                    self.module_instance = MODULES[name]()
                    self.current_module = name
                    self.module_instance.banner()
                else:
                    print("[-] Unknown module.")

            elif cmd == "back":
                self.current_module = None
                self.module_instance = None

            elif self.module_instance:
                if cmd == "options":
                    self.module_instance.show_options()
                    self.module_instance.show_actions()
                #elif cmd == "show actions":
                #    self.module_instance.show_actions()
                elif cmd.startswith("set "):
                    try:
                        _, key, value = cmd.split(" ", 2)
                        self.module_instance.set_option(key, value)
                    except:
                        print("Usage: set <option> <value>")
                elif cmd.startswith("run "):
                    action = cmd.split(" ", 1)[1]
                    self.module_instance.run_action(action)
                elif cmd == "run all":
                    self.module_instance.run_all()
                else:
                    print("❓ Unknown command in module. Try: show actions, run <action>, set <opt> <val>, back")
            else:
                print("❓ Unknown command. Try: show modules, use <module>, exit.")
