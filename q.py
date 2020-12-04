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
def __1__():
    try:
        site = input(Fore.RED + "Pleass Enter You Target Address " + Fore.YELLOW + "==>  ")
        soc = socket.gethostbyname(site)
        print(Fore.GREEN + "Your Ip " + Fore.YELLOW + "==>  "  + Fore.RED + str(soc))
        print(Fore.GREEN + "End " + Fore.YELLOW + ";)")
    except:
        pass
__1__()
