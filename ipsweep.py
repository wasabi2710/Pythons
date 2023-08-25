import os
import platform
import sys
import subprocess

if (len(sys.argv) < 2):
    print("No IP ...")
    sys.exit(0)

def ping(gateway):
    """
    Returns true if host (str) responds to a ping request
    """
    # option for the number of packets as a function on os
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # building the command
    for x in range(2, 255):
        # build ip with gateway
        ip = gateway + "." + str(x)
        cmd = "ping " + param + " 1 " + ip
        response = os.popen(cmd)
        ip_list = response.readlines()

        for line in ip_list:
            if (line.count("TTL")):
                print(ip, "--> Active")
                break  
    

# run sweep
ping(sys.argv[1])
