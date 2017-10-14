'''
Created on Sep 11, 2014

@author: lada
'''
'''
Created on Sep 11, 2014

@author: lada
Using decorators
'''
commands = {}
def action(c):
    def populate(f):
        commands[c] = f
    return populate

@action("mkdir")
def create_dir(*args, **kwargs): # mkdir
    print "Creating directories:", args

@action("ls")
def listfiles(*args, **kwargs): # ls
    print "Listing contents of", args

@action("pwd")
def show_dir(*args, **kwargs):  # pwd
    print "/root/Desktop"
    
@action("time")
def show_time(*args, **kwargs):  # date
    from time import ctime
    print ctime()

@action("exit")
def exit_program(*args, **kwargs): # exit
    print "Bye"
    exit(0)

    
def invalid_command(*args, **kwargs):
    print "Invalid command!"

while True:
    cmd = raw_input("Cmd> ")
    args = cmd.split()
    cmd = args.pop(0)
    commands.get(cmd, invalid_command)(*args)
    
    # TBD -> Implement the logic here.
