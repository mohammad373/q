# q

from colorama import Fore
print(Fore.RED + """
                ╔═════╗     ╔═════╗          
                ║ ███ ║     ║ ███ ║                      
                ║ ███ ║     ║ ███ ║       
                ║ ███ ╚═════╝ ███ ║
                ║ ███████████████ ║   hacker     
                ║ ███████████████ ║   nwwb  :)
                ║ ███ ╔═════╗ ███ ║      
                ║ ███ ║     ║ ███ ║      
                ║ ███ ║     ║ ███ ║      
                ╚═════╝     ╚═════╝ 
                                                """)


import socket
import time
def __1__():
    try:
        site = input(Fore.RED + "Pleass Enter You Target Address " + Fore.YELLOW + "==>  ")
        soc = socket.gethostbyname(site)
        time.sleep(0.6)
        print(Fore.GREEN + "Your Ip " + Fore.YELLOW + "==>  "  + Fore.RED + str(soc))
        time.sleep(1)
        print(Fore.GREEN + "\t\tEnd " + Fore.YELLOW + ";)\n")
    except:
        pass
__1__()

