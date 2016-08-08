def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"
gap ("**")

print """
  Other people have written commands that you can bring into your script.
  Many of these come with python, but to save memory they come compressed.
  You must 'unpack' the package using the command 'import package' 
  These imports are always listed on the very first lines of the script.
"""
gap("*")

print """
  The 'os' package contains many useful commands similar to those you would use
  from the command line. The command os.getcwd() = pwd, os.chdir('path') = 
  cd'path' and os.listdir('path') = ls'path' 
"""

import os  #should be at the very top of the script

wd = os.getcwd()
print wd

ls_list = os.listdir(wd)  #os,listdir creates a list without needing brackets
print ls_list

gap("*")

def pwd(): #all def's should be immediately after all imports
  wd = os.getcwd()
  print wd

def ls():
  wd = os.getcwd()
  ls_list = os.listdir(wd)
  for i in range(len(ls_list)):
    print ls_list[i]

pwd() #Here we actually call the created methods(run the commmands)
ls()

gap("&")

def cd(path): #this method requires an argument 'path' because... 
  print "\n"
  os.chdir(path) #oschdir requires an absolute path as an argument.
  pwd()
  ls()

new_path = raw_input("Type an absolute path to see what the directory contains ")
cd(new_path)








