import subprocess
import time
import socket

port=3000
IP="192.168.1.122"

while 1:
    subprocess1 = subprocess.Popen("spidev_test -D /dev/spidev1.0  -s 100000 -p \"\\x01\\x80\\x00\" -v", stdout=subprocess.PIPE, shell=True)
    
    subprocess_return =subprocess1.stdout.read()
    
    f=open("/sys/devices/platform/ath79-gpio/gpiochip0/gpio/gpio23/value","r")
    P1=int(f.read(1))
    

    rx=(subprocess_return[175:183])
    file_rx=open('/etc/spi_rx.txt',"w")
    file_rx.write(rx)
    file_rx=open('/etc/spi_rx.txt',"r")
    hexa=file_rx.read()
    print(hexa)
    d=hexa.replace(" ","")
    decimal=int(d,16)
    print(decimal)
    
    x=1.0 
    y=3.3

    V=(y/4096)*decimal 
    I=((V/2)/20)*1000 
    print(V)
    print(I)

    BAR=(1.0/16.0)*I
    BARx=BAR-0.25
    BARxnew=round(BARx,2)
    print(BARxnew)
    subprocess1.kill()
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP,port))
    message="{"+"'akim':"+str(I)+","+"'bar':"+str(BARxnew)+"}"
    server.send(message.encode())
    server.settimeout(5.0)
    time.sleep(1)
