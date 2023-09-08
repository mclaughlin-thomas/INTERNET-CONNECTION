from wireless import Wireless
import os
import time
# By Thomas McLaughlin and Roman Morasco

def connectEspKey():
    hostname = "google.com" #TOBE 192.168.4.1
    isConnected = False
    while isConnected is False:
        time.sleep(15)
        wire = Wireless()
        wire.connect(ssid = 'name', password = '333333')
        time.sleep(5)
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            isConnected = True
    print("Connection Established")

def connectInternet():
    hostname = "google.com"
    isConnected = False
    while isConnected is False:
        time.sleep(15)
        wire = Wireless()
        wire.connect(ssid = 'ARRIS-7ED5', password = '331334300637')
        time.sleep(5)
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            isConnected = True
    print("Connection Established")   


def main():
    time.sleep(0)# increase to around 30 to allow computer to start up
    print("STARTING INITIAL CONNECTION")
    connectEspKey()
    print("STARTING SECOND CONNECTION")
    connectInternet()
#     os.system("rfkill block wifi")
#     time.sleep(1)
#     os.system("rfkill unblock wifi")
#     time.sleep(20)
#     
#     wire = Wireless()
#     time.sleep(10)
#     wire.connect(ssid = 'ARRIS-7ED5-5G', password = '331334300637')
#     print("ending")
#     
#     time.sleep(5)
#     
#     print("starting again")
#     
#     os.system("rfkill block wifi")
#     time.sleep(1)
#     os.system("rfkill unblock wifi")
#     time.sleep(20)
#     
#     wire = Wireless()
#     time.sleep(10)
#     wire.connect(ssid = 'ARRIS-7ED5', password = '331334300637')
#     print("ending again")


  
if __name__=="__main__":
    main()
    
