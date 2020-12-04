# q

from colorama import Fore
print(Fore.RED + """
                               ╔═════╗     ╔═════╗          
                               ║ ███ ║     ║ ███ ║                      
                               ║ ███ ║     ║ ███ ║       
                               ║ ███ ╚═════╝ ███ ║
                               ║ ███████████████ ║   H a c k e r     
                               ║ ███████████████ ║   N w w b  :)
                               ║ ███ ╔═════╗ ███ ║      
                               ║ ███ ║     ║ ███ ║      
                               ║ ███ ║     ║ ███ ║      
                               ╚═════╝     ╚═════╝ 
                  ╔════════════════════════════════════════╗                         
                  ║                                        ║   
                  ║           Name : H A C K E R           ║ 
                  ║                                        ║  
                  ║           Family : N W W B             ║  
                  ║                                        ║
                  ║           Muzic : A M R O F - C O L    ║
                  ║                                        ║
                  ║           Live : M U Z I C             ║
                  ║****                                ****║
                  ║***                                  ***║ 
                  ║**                                    **║
                  ║*                                      *║
                  ╚════════════════════════════════════════╝
                  """)







print("Pleass Enter Your 1 or 2  or 3 ")
print(Fore.RED + "     [1] "+ Fore.GREEN + "Ip WebSite" + Fore.BLUE + " ;) ")
print(Fore.RED + "     [2] "+ Fore.GREEN + "Your Ip" + Fore.BLUE + " ;) ")
print(Fore.RED + "     [3] "+ Fore.GREEN + "Cloud Flare For WebSite" + Fore.BLUE + " ;) ")
n= int(input(Fore.GREEN + "Enter Your Number 1 / 2 / 3 " + Fore.BLUE + "==>  " ))
        

#__________________________________________________________________________________________________________
#==========================================================================================================

# Ip Site Mamole

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

# Ip Carbar

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

# _____________________________________________________________________________________________________
#======================================================================================================

#Cloud Flare
if n == 3:


    import os
    import sys
    import time
    import socket
    from colorama import Fore

    def __3__():
        try:
            site = input(Fore.RED + "Enter Your Address Web Site " + Fore.YELLOW + "==>  ")
            my_list = ["www",'ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
            for item in my_list:
                host = item + "." + site
                bypass = socket.gethostbyname(str(host))
                print(Fore.GREEN + "Your Ip "+ Fore.YELLOW + "==> " + Fore.RED + str(bypass) + Fore.YELLOW + " | " + Fore.RED + str(host))
                time.sleep(2)
        except:
            pass
    __3__()



#_______________________________________________________________________________________________________________________________
# ==============================================================================================================================

# Domain_ 1_
if n == 4 :
  import os
  import sys
  import time
  import requests, builtwith
  from colorama import Fore
  
  def __4__():
      try:
          site = input("Enter Your Address WebSite ==>  ")
          if not "http" in site or not "https" in site:
              site = "http://" + site
          req = builtwith.parse(site)
          for item in req:
              value = ""
              for var in item[str(item)]:
                  item = item.replace("-" , " ")
                  item = item.title()
                  value += str(val)
                  print(item +" : " + value)
      except:
          pass
  __4__()



