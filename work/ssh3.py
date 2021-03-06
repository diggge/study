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


commands = ["sh inventory"]
# for oborudovanie in devices_filials_routers:
#     try:
#         result = send_show_command(ip=oborudovanie, username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
#         pprint(result, width=120)
#     except:
#         print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
result = send_show_command(ip='10.77.30.6', username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
pprint(result, width=120)
