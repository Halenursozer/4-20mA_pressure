# 4-20mA_pressure
 In this project, 4-20 mA pressure measurement was carried out.  
 The analog data received from the 4-20 mA sensor were converted to digital with the ADC circuit. These data are stored in the processor. The spi driver is installed on  the processor and insmod spi-gpio-custom bus0=1,14,0,15,0,10000,1 is written to the command system and the installation is completed.  
 
 # Libraries  
import ConfigParser  
import subprocess  
import time  
import socket
 
