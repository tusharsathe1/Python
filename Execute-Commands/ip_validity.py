import sys

def ip_addr_validation(list):
    for ip in list:
        ip_octet = ip.split('.')
        # Check whether the IP address is valid
        if (len(ip_octet) == 4) and (int(ip_octet[0]) != 127) and (int(ip_octet[0]) != 169 or int(ip_octet[1]) != 254) and (1 <= int(ip_octet[0]) <= 223) and (0 <= int(ip_octet[1]) <= 255 and 0 <= int(ip_octet[2]) <= 255 and 0 <= int(ip_octet[3]) <= 255):
            print(ip + " is a valid IP")
            continue
        else:
            print(ip + " is an invalid IP")
            sys.exit()
