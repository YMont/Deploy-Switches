
import netmiko
from netmiko import ConnectHandler
from datetime import datetime

from dhcp_server import user_path
from device_list import device_list

def command_list():
    ''' this is a single command sample'''
    # Privilged mode, switch# 
    #ex1: pri_cmd = ["do show run"]
    #ex2: pri_cmd = ["do show version"]

    # global mode,switch(config)#
    # globady_cmd = ["int fa 0/0","speed 100"]
    globady_cmd = ["do show run | in dhcp"]
    return globady_cmd
    # -----------------------------------------
def get_txt_content():
    """ this is for using dhcp_pool's .txt command collect """
    try:
        var_path = user_path()
        with open(r"%s\DHCP_Pool.txt"%var_path,"r") as ff :
            txt_content = ff.read()
            print(txt_content)
    except Exception as exce:
        print("Error:",exce)
    return txt_content

def connetcing_action():
    start_time = datetime.now()
    print("Please wait a memont. SSH Connecting ... \n")
    
    all_device = device_list() # call device_list()
    print(all_device)
    print("-"*20+"Separation"+"-"*20)
    for a_device in all_device:
        try:
            net_connect = ConnectHandler(**a_device)
            print(net_connect)
            # output = net_connect.send_command()
            print(f"\n\n--------- Device {a_device['device_type']} ---------")
            # output = net_connect.send_config_set(config_commands=command_list())
            
            output = net_connect.send_config_set(config_commands=command_list())
            print("Before DHCP:",output)
            
            output = net_connect.send_config_set(config_commands=str(get_txt_content()))
            print(output)
            print("--------- End ---------")

            output = net_connect.send_config_set(config_commands=command_list())
            print("After DHCP:",output)
            
        except Exception as exce:
            print("try connecting error:",exce)
            var_path = user_path()
            with open(r"%s\log.txt"%var_path,"a+") as ff:
                # if len(a) == 1:
                # ff.truncate(0)
                var_time2str = datetime.now()
                ff.write(str(var_time2str)+"--"+str(exce))
                ff.write("\n")

    end_time = datetime.now() 
    total_time = end_time - start_time
    print("Process time:",total_time)
    
def main2():
    connetcing_action()

if __name__ == "__main__":
    try:
        main2()
    except ValueError as vale:
        print("Value:",vale)
    except StopIteration as sto:
        print("Stop:",sto)
    except Exception as exce:
        print("Error:",exce)