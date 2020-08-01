import sys

from file_validity import file_validity
from ip_validity import ip_addr_validation
from ip_reachability import ip_reach
from ssh_connection import ssh_func

#Save the IP address list from file validity function
ip_final_list = file_validity()

#Validate the IP address
ip_addr_validation(ip_final_list)

#Validate the IP reachability
ip_reach(ip_final_list)

#Open SSH connection to run the commands
for ip in ip_final_list:
    ip = ip.rstrip("\n")
    ssh_func(ip)
