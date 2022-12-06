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

commands = ["configure terminal", "no router eigrp 250", "no vpdn-group 1","no int di 0","end", "wr"]
for oborudovanie in devices_filials_routers:
    try:
        result = send_show_command(ip=oborudovanie, username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
        pprint(result, width=120)
        except:
        print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
# result = send_show_command(ip='10.9.30.1', username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
# pprint(result, width=120)
