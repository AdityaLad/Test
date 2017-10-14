'''
Created on Sep 11, 2014

@author: lada
'''
from nt import mkdir
def create_dir(*args, **kwargs): # mkdir
    print "Creating directories:", args

def listfiles(*args, **kwargs): # ls
    print "Listing contents of", args

def show_dir(*args, **kwargs):  # pwd
    print "/root/Desktop"

def show_time(*args, **kwargs):  # date
    from time import ctime
    print ctime()

def exit_program(*args, **kwargs): # exit
    print "Bye"
    exit(0)
    
commands = {"mkdir":create_dir,
            "exit":exit_program,
            "pwd":show_dir}
    
def invalid_command(*args, **kwargs):
    print "Invalid command!"

while True:
    cmd = raw_input("Cmd> ")
    args = cmd.split()
    cmd = args.pop(0)
    commands.get(cmd, invalid_command)(*args)
    
    # TBD -> Implement the logic here.
