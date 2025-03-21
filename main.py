import sys

from modules.no_cred import NoCred
# from modules.valid_user import ValidUser



def main():
    print("\n[+] Active Directory Pentest Framework is running...\n")
    print("1. No Cred ")
    print("2. Valid User")

    choice = input("Enter your choice")

    if choice == '1':
        no_cred = NoCred()
        no_cred.run()
    # elif choice == '2':
    #     valid_user = ValidUser()
    #     valid_user.run()
    else:
        print("\n[-] Invalid choice. Please provide valid option...\n")
        main()

if __name__ == '__main__':
    main()