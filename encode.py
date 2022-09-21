from base64 import *
import colorama
from colorama import *
colorama.init()

banner = '''
███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝
█████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  
██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  
███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗
╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                                               
1 : Encode   |   2 : Decode

'''

def cryptmessage(n: str) -> str:
    n = b64encode(n.encode())
    n = b16encode(n)
    n = b32encode(n)
    n = b85encode(n)
    n = b85encode(n)
    n = b16encode(n)
    n = b32encode(n)
    n = b32encode(n)
    n = b85encode(n)
    n = b64encode(n)
    return n
def decryptmessage(n: str) -> str:
    n = b64decode(n)
    n = b85decode(n)
    n = b32decode(n)
    n = b32decode(n)
    n = b16decode(n)
    n = b85decode(n)
    n = b85decode(n)
    n = b32decode(n)
    n = b16decode(n)
    n = b64decode(n)
    return n


print(Fore.BLUE + banner)
print(Fore.RESET)
choice = input("Your choice : ")
if choice == "1":
    message = input("Message to encrypt : ")

    input(cryptmessage(message))
elif choice == '2':
    message = input("Message to decrypt : ")
    input(decryptmessage(message))

