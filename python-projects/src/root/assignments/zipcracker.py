'''
Created on Sep 9, 2014

@author: lada
'''
import zipfile
import time

filezip="secretfile.zip"
passfile="passwords.txt"
def crackPassword(file_to_crack, pass_dict):
    fd = zipfile.ZipFile(file_to_crack)
    dict_file = open(pass_dict)
    for password in dict_file.readlines():
        try:
            fd.extractall(pwd=password.strip())
            print "Password found: ", password
        except RuntimeError:
            pass
def main():
    start = time.clock()
    crackPassword(filezip, passfile)
    print "complete"
    stop = time.clock()
    print "Time taken", (stop - start)

if __name__ == '__main__':
    main()