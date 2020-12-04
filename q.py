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



print("Pleass Enter Your 1 or 2 ")
print(Fore.RED + "     [1] "+ Fore.GREEN + "Ip WebSite" + Fore.BLUE + " ;) ")
print(Fore.RED + "     [2] "+ Fore.GREEN + "Your Ip" + Fore.BLUE + " ;) \n\n")
n = int(input(Fore.GREEN + "Enter Your Number 1 / 2 " + Fore.BLUE + "==>  " )
        

#__________________________________________________________________________________________________________
#==========================================================================================================
if n == 1:
        
  import socket
  import time
  def __1__():
      try:
          site = input(Fore.RED + "Pleass Enter You Target Address " + Fore.YELLOW + "==>  ")
          soc = socket.gethostbyname(site)
          time.sleep(0.6)
          print(Fore.GREEN + "Your Web Site " + Fore.YELLOW + "==>  "  + Fore.RED + str(soc))
          time.sleep(1)
          print(Fore.YELLOW + "End " + Fore.GREEN + ";)\n")
      except:
          pass
  __1__()




#_____________________________________________________________________________________________
# ============================================================================================

if n == 2:        

  import os
  import socket
  import sys
  import time
  from colorama import Fore

  def __2__():
    try:
      q = socket.gethostname()
      qq = socket.gethostbyname(q)
      print(Fore.GREEN + "Your Ip " +Fore.YELLOW + "==> " + Fore.RED + qq)
      print(Fore.YELLOW + "End " + Fore.GREEN + ";)\n")
    except:
      pass
  __2__()
