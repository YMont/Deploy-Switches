
from dhcp_server import main1, user_path
from switch_list import main2
from datetime import datetime

var_path = None

if __name__ == "__main__":
    try:
        main1()
        print("mark1.")
        main2()
        print("mark2.")
        
        print(var_path)
        var_path = user_path()
        print(var_path)
    except ValueError as vale:
        var_path = user_path()
        print(var_path)

        print("Value:",vale)
        with open(r"%s\log.txt"%var_path,"a+") as ff:
            var_time2str = datetime.now()
            ff.write(str(var_time2str)+"--"+str(vale))
            ff.write("\n")
    
    except StopIteration as sto:
        var_path = user_path()
        print(var_path)
        print("Stop:",sto)
        with open(r"%s\log.txt"%var_path,"a+") as ff:
            var_time2str = datetime.now()
            ff.write(str(var_time2str)+"--"+str(sto))
            ff.write("\n")
    
    except Exception as exce:
        var_path = user_path()
        print(var_path)

        print("Error:",exce)
        with open(r"%s\log.txt"%var_path,"a+") as ff:
            var_time2str = datetime.now()
            ff.write(str(var_time2str)+"--"+str(exce))
            ff.write("\n")
