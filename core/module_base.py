#base pour les autres modules, ils héritent de cette  classe


class ModuleBase:
    def __init__(self):
        self.name = "unnamed_module"
        self.options = {}      
        self.actions = {}      

    def set_option(self, key, value):
        if key in self.options:
            self.options[key] = value
            print(f"[+] {key} set to {value}")
        else:
            print(f"[-] Unknown option: {key}")

    def show_options(self):
        print("\nCurrent Options:")
        for key, val in self.options.items():
            print(f"  {key}: {val}")
        print()

    def show_actions(self):
        print("\nAvailable Actions:")
        for name in self.actions.keys():
            print(f"  • {name}")
        print()

    def run_action(self, action):
        if action in self.actions:
            print(f"\n[>] Running {action}...\n")
            self.actions[action]()
        else:
            print(f"[-] Action '{action}' not found.")

    
    def run_all(self):
        print("\n[🔥] Running all actions...\n")
        for action in self.actions:
            self.actions[action]()
        
