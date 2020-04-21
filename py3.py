#!/usr/bin/env python3
# Coded By : A_Asaker

import os,readline,rlcompleter,threading,time
readline.parse_and_bind('tab: complete')
if "win" in os.sys.platform :
 import colorama
 colorama.init()
print()

#Print Date & Time At The Top
#Not Important, Comment This Section If You Want!
def terminal_time():
 while 1:
  time.sleep(.25)
  os.sys.stdout.write("\0337\033[H\033[2K\t\t\033[1;4;44;37m    " + time.asctime(time.localtime())+"  [PYTOHN 3]"+"    \033[0;1;37m\0338")
  os.sys.stdout.flush()
threading.Thread(target=terminal_time,daemon=True).start()



#Interactive Interpreter & Shell
cmnd=""
while cmnd != 'exit':
 try:
  in_cmnd=input("\033[0m\n{} \033[1;4;33mPy3\033[0m{}\n   \033[1;31m {}{}{}{}\033[1;37m ".format(chr(5295),chr(5292),chr(5307),chr(5933),chr(5933),chr(5582)))
  cmnds=in_cmnd.split("&&")
  for cmnd in cmnds:
   try:
    cmnd=cmnd.strip()
    if "cd" in cmnd.strip().split():
     s_cmnd=cmnd.strip().split()
     path=s_cmnd[s_cmnd.index('cd')+1]
     os.chdir(path)
     cmnd=cmnd.replace("cd","")
     cmnd=cmnd.replace(path,"")
    print("\033[94m      ",end="")
    exec(cmnd)
   except Exception as ex:
    print("\033[0;96m\r",end="")
    os.sys.stdout.flush()
    st_code=os.system(cmnd)
    print("\033[1;91;107m"+str(ex),end="") if st_code else ""
 except : break
print("\033[0m")
