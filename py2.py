#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coded By : A_Asaker
import os,readline,rlcompleter,threading,time
readline.parse_and_bind('tab: complete')
if "win" in os.sys.platform :
 import colorama
 colorama.init()
print

#Print Date & Time At The Top
#Not Important, Comment This Section If You Want!
def terminal_time():
 while 1:
  time.sleep(.25)
  os.sys.stdout.write("\0337\033[H\033[2K\t\t\033[1;4;44;37m    " + time.asctime(time.localtime())+"  [PYTOHN 2]"+"    \033[0;1;37m\0338")
  os.sys.stdout.flush()
thr=threading.Thread(target=terminal_time,)
thr.daemon=True
thr.start()

#Interactive Interpreter & Shell
cmnd=""
multi_line=('for','while','if','with','try','def','class')
while cmnd != 'exit':
 try:
  in_cmnd=raw_input("\033[0m\nᒯ \033[1;4;33mPy2\033[0mᒬ\n   \033[1;31m ᒻᜭᜭᗎ\033[1;37m ")
  if in_cmnd.strip().startswith(multi_line):
   in_multi=raw_input("    ===> ")
   while (in_multi):
    in_cmnd+=("\n"+in_multi)
    in_multi=raw_input("    ===> ")
#   exec(in_cmnd)
#   continue 
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
    print "\033[94m     ","",
    exec(cmnd)
   except Exception as ex:
    print "\033[0;96m\r",
    os.sys.stdout.flush()
    st_code=os.system(cmnd)
    print "\033[1;91;107m"+str(ex) if st_code else "",
 except : break
print "\033[0m"
