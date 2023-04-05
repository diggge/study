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
        max_bytes=600000,
        short_pause=1,
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
                    time.sleep(0.3)
                except socket.timeout:
                    break
            result[command] = output
        return result
devices_ID = ["10.77.30.1", "10.77.30.2", "10.77.30.3", "10.77.30.4", "10.77.30.5", "10.77.30.6", "10.77.30.7",
              "10.77.30.8", "10.77.30.9", "10.77.30.10", "10.77.30.11", "10.77.30.12", "10.77.30.13", "10.77.30.14",
              "10.77.30.15", "10.77.30.19", "10.77.30.20", "10.77.30.21", "10.77.30.22",
              "10.77.30.23", "10.77.30.24", "10.77.30.26", "10.77.30.30", "10.77.30.100", "10.77.30.101", "10.77.30.102", "10.77.30.103",
              "10.77.30.104"]
devices_wi_fi = ['10.77.30.100', '10.77.30.101', '10.77.30.102', '10.77.30.103', '10.77.30.104', '10.77.30.105']
devices_filials_routers = ['10.77.176.1',
              '10.77.181.1',
			  '10.77.186.1',
              '10.77.191.1',
              '10.77.196.1',
			  '10.77.201.1',
			  '10.77.206.1',
			  '10.77.211.1',
			  '10.77.216.1',
			  '10.77.221.1',
			  '10.77.226.1',
			  '10.77.231.1',
			  '10.77.236.1',
			  '10.77.241.1',
			  '10.77.246.1',
			  '10.77.251.1']

devices_filials = ["10.77.176.1", "10.77.176.2",
                   '10.77.181.1', '10.77.181.2',
                   '10.77.186.1', '10.77.186.2',
                   '10.77.191.1', '10.77.191.2',
                   '10.77.196.1', '10.77.196.2', '10.77.196.3',
                   '10.77.201.1', '10.77.201.2',
                   '10.77.206.1', '10.77.206.2',
                   '10.77.211.1', '10.77.211.2', '10.77.211.3',
                   '10.77.216.1', '10.77.216.2',
                   '10.77.221.1', '10.77.221.2',
                   '10.77.226.1', '10.77.226.2', '10.77.226.3', '10.77.226.4',
                   '10.77.231.1', '10.77.231.2', '10.77.231.3',
                   '10.77.236.1', '10.77.236.2', '10.77.236.3', '10.77.236.4',
                   '10.77.241.1', '10.77.241.2', '10.77.241.3',
                   '10.77.246.1', '10.77.246.2',
                   '10.77.251.1', '10.77.251.2', '10.77.251.3', '10.77.251.4', '10.77.251.5', '10.77.251.6']
devices=devices_filials_routers
print('Устройства, на которых будет выполняться скрипт=', devices)
# devices=['10.77.30.3']
# commands = ['conf ter', 'voice service voip', 'ip address trusted list', 'ipv4 10.0.0.0 255.0.0.0','exit', 'sip', 'bind control source-interface GigabitEthernet0/1.7', 'bind media source-interface GigabitEthernet0/1.7', 'dial-peer voice 103 voip', 'description Anabar', 'destination-pattern 20[5-9].', 'session target ipv4:10.77.175.1', 'dtmf-relay rtp-nte', 'dial-peer voice 104 voip', 'description BelayGora', 'destination-pattern 21[0-4].', 'session target ipv4:10.77.180.1', 'dtmf-relay rtp-nte', 'dial-peer voice 105 voip', 'description Tiksi', 'destination-pattern 21[5-9].', 'session target ipv4:10.77.185.1', 'dtmf-relay rtp-nte', 'dial-peer voice 106 voip', 'description Batagay', 'destination-pattern 22..', 'session target ipv4:10.77.190.1', 'dtmf-relay rtp-nte', 'dial-peer voice 107 voip', 'description Jigansk', 'destination-pattern 23[0-4].', 'session target ipv4:10.77.195.1', 'dtmf-relay rtp-nte', 'dial-peer voice 108 voip', 'description Zyryanka', 'destination-pattern 23[5-9].', 'session target ipv4:10.77.200.1', 'dtmf-relay rtp-nte', 'dial-peer voice 109 voip', 'description Sangar', 'destination-pattern 24[0-4].', 'session target ipv4:10.77.205.1', 'dtmf-relay rtp-nte', 'dial-peer voice 110 voip', 'description Moma', 'destination-pattern 24[5-9].', 'session target ipv4:10.77.210.1', 'dtmf-relay rtp-nte', 'dial-peer voice 111 voip', 'description Nizhnekolyma', 'destination-pattern 25[0-4].', 'session target ipv4:10.77.215.1', 'dtmf-relay rtp-nte', 'dial-peer voice 112 voip', 'description Oimyakon', 'destination-pattern 25[5-9].', 'session target ipv4:10.77.220.1', 'dtmf-relay rtp-nte', 'dial-peer voice 113 voip', 'description Olekma', 'destination-pattern 26[0-4].', 'session target ipv4:10.77.225.1', 'dtmf-relay rtp-nte', 'dial-peer voice 114 voip', 'description Olenek', 'destination-pattern 27[0-4].', 'session target ipv4:10.77.230.1', 'dtmf-relay rtp-nte', 'dial-peer voice 115 voip', 'description Sredkolym', 'destination-pattern 27[5-9].', 'session target ipv4:10.77.235.1', 'dtmf-relay rtp-nte', 'dial-peer voice 116 voip', 'description Chokurdakh', 'destination-pattern 28[0-4].', 'session target ipv4:10.77.240.1', 'dtmf-relay rtp-nte', 'dial-peer voice 117 voip', 'description EvemoByt', 'destination-pattern 28[5-9].', 'session target ipv4:10.77.245.1', 'dtmf-relay rtp-nte', 'dial-peer voice 118 voip', 'description trunk_toDeputats', 'destination-pattern 29..', 'session target ipv4:10.77.250.1', 'dtmf-relay rtp-nte', 'dial-peer voice 5522 voip', 'huntstop', 'destination-pattern 0T', 'session target ipv4:10.77.7.253', 'no session transport udp', 'dtmf-relay rtp-nte', 'end', 'wr']
# commands = ["conf ter", "no archive", "archive", "path ftp://10.77.3.35/$h-$t", "write-memory", "exit", "voice service voip", "sip", "no bind media source-interface GigabitEthernet0/1.7", "exit", "no ip access-list extended MGMT", "ip access-list extended MGMT", "permit tcp any 10.77.0.0 0.0.255.255 eq 22", "permit tcp 10.77.0.0 0.0.255.255 any eq 22", "exit", "no ip access-list extended RDP1C", "ip access-list extended RDP1C", "permit tcp any host 80.73.69.174 eq 3393", "permit tcp any host 80.73.69.174 eq 3396", "permit tcp any host 10.77.3.8 eq 3389", "permit tcp any host 10.77.3.69 eq 3389", "exit", "no ip access-list extended lan_id", "ip access-list extended lan_id", "permit ip 10.77.0.0 0.0.255.255 172.26.0.0 0.0.255.255", "permit ip 10.77.0.0 0.0.255.255 10.0.0.0 0.255.255.255", "exit", "no ip access-list extended yakenergo", "ip access-list extended yakenergo", "permit ip 10.77.0.0 0.0.255.255 172.26.0.0 0.0.255.255", "permit ip 10.77.0.0 0.0.255.255 10.0.0.0 0.255.255.255", "exit", "dial-peer voice 103 voip", "session target ipv4:10.77.175.1", "dial-peer voice 104 voip", "session target ipv4:10.77.180.1", "dial-peer voice 105 voip", "session target ipv4:10.77.185.1", "dial-peer voice 106 voip", "session target ipv4:10.77.190.1", "dial-peer voice 107 voip", "session target ipv4:10.77.195.1", "dial-peer voice 108 voip", "session target ipv4:10.77.200.1", "dial-peer voice 109 voip", "session target ipv4:10.77.205.1", "dial-peer voice 110 voip", "session target ipv4:10.77.210.1", "dial-peer voice 111 voip", "session target ipv4:10.77.215.1", "dial-peer voice 112 voip", "session target ipv4:10.77.220.1", "dial-peer voice 113 voip", "session target ipv4:10.77.225.1", "dial-peer voice 114 voip", "session target ipv4:10.77.230.1", "dial-peer voice 115 voip", "session target ipv4:10.77.235.1", "dial-peer voice 116 voip", "session target ipv4:10.77.240.1", "dial-peer voice 117 voip", "session target ipv4:10.77.245.1", "dial-peer voice 118 voip", "session target ipv4:10.77.250.1", "line vty 0 4", "no access-class 117 in", "access-class 23 in", "exit", "line vty 5 15", "no access-class 117 in", "access-class 23 in", "end", "wr", "exit"]
#commands = ["conf ter",  "login on-failure log", "login on-success log", "end", "wr"]
commands = ['conf ter', 'no ntp authentication-key 1 md5 15060E1F10243F34 7', 'no ntp authenticate', 'no ntp trusted-key 1', 'ntp master 14', 'no ntp server 80.73.69.174 prefer', 'ntp server 10.77.30.1 prefer', 'no ip access-list standard ntp_access', 'ip access-list standard ntp_access', 'permit 10.77.0.0 0.0.255.255', 'permit 10.100.0.0 0.0.0.255', 'permit 10.200.0.0 0.0.0.255', 'permit 172.26.160.0 0.0.1.255', 'no ip access-list standard ntp_peers', 'ip access-list standard ntp_peers', 'permit 10.77.0.0 0.0.255.255', 'permit 172.26.160.0 0.0.1.255', 'permit 10.100.0.0 0.0.0.255', 'permit 10.200.0.0 0.0.0.255', 'end', 'wr']
# commands = ["conf ter", "sntp server 10.77.30.1", "sntp broadcast client", "clock timezone +0900 9", "end", "wr"]
# commands = ["conf ter", "service timestamps log datetime localtime", "logging on", "logging buffered informational", "logging buffered 163860", "logging rate-limit 100 except 4", "logging rate-limit all 50", "logging console critical", "logging monitor debugging", "no ip domain-lookup", "archive", "log config", "logging enable", "notify syslog contenttype plaintext", "hidekeys", "no path ftp://172.26.160.22/$h-$t", "path ftp://10.77.3.35/$h-$t", "ip ftp username cisco-backup", "ip ftp password ftpPasswd", "kron occurrence SaveConfigSchedule at 05:09 1 recurring", "policy-list SaveConfig", "kron policy-list SaveConfig", "no cli write", "no cli write", "no cli write", "no cli write", "cli write", "logging trap debugging", "logging 10.77.3.24", "logging host 10.77.3.24", "logging trap debugging", "ip ssh time-out 60", "ip ssh logging events", "ip ssh version 2", "no access-list 117", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any established", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any log-input", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any log-input", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any log-input", "access-list 117 deny ip any any log-input", "line vty 0 4", "access-class 117 in", "line vty 5 15", "access-class 117 in", "end", "wr"]
for oborudovanie in devices:
    try:
        result = send_show_command(ip=oborudovanie, username='root', enable="Cf[f'ythuj2104", password="Cf[f'ythuj2104", command=commands)
        pprint(result, width=600)
    except:
        print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
