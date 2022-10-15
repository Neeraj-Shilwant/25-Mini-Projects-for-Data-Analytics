import datetime
import time
endtime = datetime.datetime(2022,8,5)
site = ["www.facebook.com","www.instagram.com","www.youtube.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:

    if datetime.datetime.now() < endtime:
        print("Start Blocking....")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for web in site:
                if web not in content:
                    host_file.write(redirect + " "+web+"\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(web in lines for web in site):
                    host_file.write(lines)

            host_file.truncate()
        time.sleep(5)