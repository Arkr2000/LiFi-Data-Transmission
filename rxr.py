from machine import Pin as p
from utime import sleep
from binascii import unhexlify
rx_bstring=''
rx_string=''
flag=True

ldm=p(9,p.IN)
dc=0.05
def rbit():
     global rx_bstring
     if int(ldm.value())==1:
         sleep(2*dc)
         rx_bstring+=str(ldm.value())
         sleep(3*dc)
         
while(flag):
    if rx_bstring.find('001000110010001100100011')>0:
        flag=False
    else:rbit()
    
temp= int(rx_bstring,2)
rx_string=str(unhexlify('%x' % temp))
rx_string=rx_string[2:-4]  #The String is in the form of b'String###'        
print("The msg received: %s" %(rx_string))



