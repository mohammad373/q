# q

from colorama import Fore
print(Fore.RED + """)
        ╔═════╗     ╔═════╗          
        ║ ███ ║     ║ ███ ║                      
        ║ ███ ║     ║ ███ ║       
        ║ ███ ╚═════╝ ███ ║
        ║ ███████████████ ║         
        ║ ███████████████ ║     
        ║ ███ ╔═════╗ ███ ║      
        ║ ███ ║     ║ ███ ║      
        ║ ███ ║     ║ ███ ║      
        ╚═════╝     ╚═════╝ 
                        """)

import os
import socket
import sys
import os
def __1__():
    try:
        site = input(Fore.RED + "Pleass Enter You Target Address " + Fore.YELLOW + "==>  ")
        if not "http" in site or not "https" in site:
            site = ("http://" + site)
        soc = socket.gethostbyname(str(site))
        print(Fore.GREEN + "Your Ip " + Fore.YELLOW + "==>  "  + Fore.RED + str(soc))
        print(Fore.GREEN + "End " + Fore.YELLOW + ";)")
    except:
        pass
__1__()
