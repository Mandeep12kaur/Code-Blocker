import time
from datetime import datetime as dt

ip_localmachine='127.0.0.1'
website_list=['www.facebook.com','www.instagram.com','instagram.com']
host_path='C:\Windows\System32\drivers\etc\hosts'
star_time='09:0:0'
endtime='18:0:0'

now=dt.now()
current_time=now.strftime('%H:%M:%S')
print(current_time)

while True:
    if star_time<=current_time and current_time<=endtime:
        print('working hours')
        with open(host_path,'r') as file:
            content=file.read()
            for website in website_list:
                pass
            
            else:
                file.write(ip_localmachine+' '+website+'\n')
                
    else:
        print('Not working hours')
        with open(host_path,'r+') as file:
            content=file.readlines()
        file.seek(0) 
        for line in content:
            if not any (website in line for website in website_list):
                file.write(line)
            file.truncate  
      
    time.sleep(10)