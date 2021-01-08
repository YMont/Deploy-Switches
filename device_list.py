def device_list():
    cisco1 = {
            "host": "192.168.94.251",
            "username": "dynasafe",
            "password": "dyna0808",
            "device_type": "cisco_ios_telnet",
        #     "port": "23"
            }
#     cisco2 = {
#             "host": "192.168.45.46",
#             "username": "yue",
#             "password": "123",
#             "device_type": "cisco_ios",
#             }
#     cisco3 = {
#             "host": "192.168.47.49",
#             "username": "john",
#             "password": "123",
#             "device_type": "huawei",
#             }
    deviceList = [cisco1]
    return deviceList