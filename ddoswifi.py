
import os
import sys
import time
import socket
import random
#----------------------------------------------------------------------#
def ddos():
    print("")
    print ("    ██████╗░██████╗░░█████╗░░██████╗")
    print ("    ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
    print ("    ██║░░██║██║░░██║██║░░██║╚█████╗░")
    print ("    ██║░░██║██║░░██║██║░░██║░╚═══██╗")
    print ("    ██████╔╝██████╔╝╚█████╔╝██████╔╝")
    print ("    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░")
    print ("")
    print ("MASUKAN IP DARI WIFI YANG ANDA INGIN SERANG")
    print ("")
#----------------------------------------------------------------------#
time.sleep(3)
os.system("clear")
    print("")
    print("DDOS WIFI TOOLS BY YONATHAN GM")
    print("===================================")
    print("TYPE [gas] TO START THE PROGRAM ")
    print("")
    put=input("INPUT : ")
    
    if put == "gas":
        os.system('cls')
        ddos()
        x = input("IP : ")
        print("-------------------------------------------------------------")
        print("MASUKAN PORT WIFI ANDA (CONTOH : 80)")
        print("")
        y = input("PORT : ")
        print("-------------------------------------------------------------")
        print("MASUKAN PAKET YANG ANDA KIRIM KE WIFI TUJUAN (MAXIMAL 1000)")
        print("")
        z = input("PACKET: ")

        os.system("python3 tools.py {x} {y} {z}")
#----------------------------------------------------------------------#
if __name__ == '__main__':
    put()
