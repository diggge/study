import paramiko
import time
import socket
from pprint import pprint
def send_show_command(
        ip,
        username,
        password,
        enable,
        command,
        max_bytes=60000,
        short_pause=2,
        long_pause=5,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.send("enable\n")
        ssh.send(f"{enable}\n")
        time.sleep(short_pause)
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        ssh.recv(max_bytes)
        result = {}
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(1)
            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result[command] = output
        return result
# send_show_command(ip='10.77.30.2',username= 'root', enable="Cf[f'ythuj2104",password="Cf[f'ythuj2104",command=commands)
# if __name__ == "__main__":
#     devices = ["10.77.30.15", "10.77.30.6"]
#     commands = ["conf ter", "s401-th-log", 'timeout 300',"retransmit 100", 'end', 'wr']
#     print(devices)
    # result = send_show_command(ip=devices,username= 'root', enable="Cf[f'ythuj2104",password="Cf[f'ythuj2104",command=commands)
    # pprint(result, width=120)
devices_ID = ["10.77.30.1", "10.77.30.2", "10.77.30.3", "10.77.30.4","10.77.30.5", "10.77.30.6", "10.77.30.7",
              "10.77.30.8", "10.77.30.9", "10.77.30.10", "10.77.30.11", "10.77.30.12", "10.77.30.13", "10.77.30.14",
              "10.77.30.15", "10.77.30.19", "10.77.30.20", "10.77.30.21", "10.77.30.22",
              "10.77.30.23", "10.77.30.24", "10.77.30.24", "10.77.30.30", "10.77.30.100", "10.77.30.101", "10.77.30.102", "10.77.30.103",
              "10.77.30.104"]
devices_filials_routers = [
              '10.3.30.1',
              '10.4.30.1',
			  '10.5.30.1',
              '10.6.30.1',
              '10.7.30.1',
			  '10.8.30.1',
			  '10.9.30.1',
			  '10.10.30.1',
			  '10.10.30.1',
			  '10.11.30.1',
			  '10.12.30.1',
			  '10.13.30.1',
			  '10.14.30.1',
			  '10.15.30.1',
			  '10.16.30.1',
			  '10.17.30.1',
			  '10.18.30.1']
devices_filials = ["10.3.30.1", "10.3.30.2",
              '10.4.30.1','10.4.30.2',
			  '10.5.30.1','10.5.30.2',
              '10.6.30.1','10.6.30.2',
              '10.7.30.1','10.7.30.2','10.7.30.3',
			  '10.8.30.1','10.8.30.2',
			  '10.9.30.1','10.9.30.2',
			  '10.10.30.1','10.10.30.2','10.10.30.3',
			  '10.10.30.1','10.10.30.2',
			  '10.11.30.1','10.11.30.2',
			  '10.12.30.1','10.12.30.2',
			  '10.13.30.1','10.13.30.2','10.13.30.3','10.13.30.4',
			  '10.14.30.1','10.14.30.2',
			  '10.15.30.1','10.15.30.2','10.15.30.3','10.15.30.4',
			  '10.16.30.1','10.16.30.2','10.16.30.3',
			  '10.17.30.1','10.17.30.2',
			  '10.18.30.1','10.18.30.2','10.18.30.3','10.18.30.4','10.18.30.5']
devices=devices_ID+devices_filials
# print(device)
#commands = ["conf ter", "no ip http server",'no ip http secure-server','end','wr']
commands = ["configure terminal", "no router eigrp 250", "no vpdn-group 1","no int di 0","end", "wr"]
for oborudovanie in devices_filials_routers:
    try:
        result = send_show_command(ip=oborudovanie, username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
        pprint(result, width=120)
        except:
        print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
