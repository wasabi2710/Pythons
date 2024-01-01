import nmap
import sys
import time

nm_scan = nmap.PortScanner()

print('\nRunning... \n')

nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments="-O")

host_ip_up = "The host is: " + nm_scanner['scan'][sys.argv[1]]['status']['state']+"\n"
port_open = "The port 80 is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+"\n"
method_scan = "The method of scanning is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+"\n"
os_match = "There is %s chance that the system is running on %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name']) + "\n"

with open('%s.txt'%sys.argv[1], 'w') as f:
    f.write(host_ip_up+port_open+method_scan+os_match)
    f.write('Report Generated '+time.strftime("%Y-%m-%d_%H-%M-%S GMT", time.gmtime()))

print('\nFinished... \n')