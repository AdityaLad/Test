'''
Created on Sep 8, 2014

@author: lada
'''
def readfile(filename):
    try:
        f = open(filename, 'r')
        for ipaddress in f.readlines():
            print ipaddress
    except:
        return

def main():
    readfile("microsoft_index.txt")
    
if __name__ == '__main__':
    main()
            