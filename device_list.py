def device_list():
    cisco1 = {
            "host": "192.168.xxx.xxx",
            "username": "XXX",
            "password": "XXX",
            "device_type": "cisco_ios_telnet", # port:23
            }
#     cisco2 = {
#          "host": "192.168.xxx.xxx",
#           "username": "XXX",
#           "password": "XXX",
#           "device_type": "cisco_ios", # port:22
#           }
    deviceList = [cisco1]
    return deviceList
