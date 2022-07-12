from machine import Pin as p
from utime import sleep
from binascii import hexlify

led=p(9,p.OUT)# GPIO9 is the laser
dc=0.05
cv='y'

def tbit(a):
    led.value(1)#Start bit
    sleep(1*dc)
    led.value(a)#data bit
    sleep(3*dc)
    led.value(0)
    sleep(1.5*dc)

while cv=='y' or cv=='Y':
    tx_string=input("Enter the text to be transmitted:")
    tx_string+='###'
    tx_blstring=list(bin(int(hexlify(tx_string), 16)))
    tx_blstring=tx_blstring[2:]
    for i in tx_blstring:
        tbit(int(i))
        
    cv='n'
    print("Transmitted succesfully...")
    cv=input("Do you want to transmit more(y/N):")
    

