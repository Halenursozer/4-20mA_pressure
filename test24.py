import subprocess
import time
import socket

port=3000
IP="192.168.1.122"
"""
subprocess = subprocess.Popen('echo \"\hello \\x01\ -"', stdout=subprocess.PIPE, shell=True)

subprocess_return =subprocess.stdout.read()
#print(subprocess_return)

print(subprocess_return)
"""
while 1:
    subprocess1 = subprocess.Popen("spidev_test -D /dev/spidev1.0  -s 100000 -p \"\\x01\\x80\\x00\" -v", stdout=subprocess.PIPE, shell=True)
    
    subprocess_return =subprocess1.stdout.read()
    
    f=open("/sys/devices/platform/ath79-gpio/gpiochip0/gpio/gpio23/value","r")
    P1=int(f.read(1))
    
    #print(subprocess_return)
    #print(len(subprocess_return))

    #file=open('/etc/spi_w.txt',"w")
    #file.write(subprocess_return)


    #print(subprocess_return[170:183])

    rx=(subprocess_return[175:183])
    file_rx=open('/etc/spi_rx.txt',"w")
    file_rx.write(rx)
    file_rx=open('/etc/spi_rx.txt',"r")
    #file_rx=open('/etc/app.txt',"r")
    hexa=file_rx.read()
    #print(hexa)
    print(hexa)
    d=hexa.replace(" ","")
    decimal=int(d,16)
    print(decimal)



    x=1.0 
    """
    val=4095/x
    #print(round(float((decimal/val)),4))
    A=float((decimal/val))
    print(A)
    """

    y=3.3

    V=(y/4096)*decimal 
    I=((V/2)/20)*1000 
    print(V)
    print(I)

    """
    BAR=(I*x)/78
    print(BAR)
    """

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