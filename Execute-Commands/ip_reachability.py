import subprocess
import sys

def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")
        # Ping the device IP
        ping_reply = subprocess.call(['ping', '-c 2', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        #Check the reachability
        if ping_reply == 0:
            print(ip + " is reachable")
            continue
        else:
            print(ip + " is unreachable")
            sys.exit()
