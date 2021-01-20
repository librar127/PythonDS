def isValidateIPAddress(ip_address):
    # calidatafb@gmail.com
    
    if not ip_address:
        return False
    
    if len(ip_address.split('.')) != 4:
        return False
    
    for each in ip_address.split('.'):
        try:
            int_ip_part = int(each)
            if (int_ip_part < 0) or (int_ip_part > 255):
                return False
        except:
            return False
    
    return True


ip_adddess = "127.0.0.b"
ip_adddess = "0.0.0.0"
print(isValidateIPAddress(ip_adddess))