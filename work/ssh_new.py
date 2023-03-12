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
                    time.sleep(0.1)
                except socket.timeout:
                    break
            result[command] = output
        return result
devices_ID = ["10.77.30.1", "10.77.30.2", "10.77.30.3", "10.77.30.4","10.77.30.5", "10.77.30.6", "10.77.30.7",
              "10.77.30.8", "10.77.30.9", "10.77.30.10", "10.77.30.11", "10.77.30.12", "10.77.30.13", "10.77.30.14",
              "10.77.30.15", "10.77.30.19", "10.77.30.20", "10.77.30.21", "10.77.30.22",
              "10.77.30.23", "10.77.30.24", "10.77.30.26", "10.77.30.30", "10.77.30.100", "10.77.30.101", "10.77.30.102", "10.77.30.103",
              "10.77.30.104"]
devices_wi_fi = ['10.77.30.100','10.77.30.101','10.77.30.102','10.77.30.103','10.77.30.104','10.77.30.105']
devices_filials_routers = ['10.77.176.1',
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
devices_filials = ["10.77.176.1","10.77.176.2",
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
devices=devices_wi_fi
print('Устройства, на которых будет выполняться скрипт=', devices)
# devices=['10.77.30.3']
#commands = ["conf ter", "no vpdn-group 2",'no ip http secure-server','end','wr']
commands = ["conf ter", "sntp server 10.77.30.1", "sntp broadcast client", "clock timezone +0900 9", "end", "wr"]
# commands = ["conf ter", "service timestamps log datetime localtime", "logging on", "logging buffered informational", "logging buffered 163860", "logging rate-limit 100 except 4", "logging rate-limit all 50", "logging console critical", "logging monitor debugging", "no ip domain-lookup", "archive", "log config", "logging enable", "notify syslog contenttype plaintext", "hidekeys", "no path ftp://172.26.160.22/$h-$t", "path ftp://10.77.3.35/$h-$t", "ip ftp username cisco-backup", "ip ftp password ftpPasswd", "kron occurrence SaveConfigSchedule at 05:09 1 recurring", "policy-list SaveConfig", "kron policy-list SaveConfig", "no cli write", "no cli write", "no cli write", "no cli write", "cli write", "logging trap debugging", "logging 10.77.3.24", "logging host 10.77.3.24", "logging trap debugging", "ip ssh time-out 60", "ip ssh logging events", "ip ssh version 2", "no access-list 117", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any established", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any log-input", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any log-input", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any log-input", "access-list 117 deny ip any any log-input", "line vty 0 4", "access-class 117 in", "line vty 5 15", "access-class 117 in", "end", "wr"]
for oborudovanie in devices:
    try:
        result = send_show_command(ip=oborudovanie, username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104",command=commands)
        pprint(result, width=120)
    except:
        print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
