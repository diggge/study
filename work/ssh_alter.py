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
        short_pause=0.3,
        max_read=100000,
        long_pause=2
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
        timeout=3
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
devices_ID = ["lw401-d0001.se.local","lw401-d0002.se.local","lw401-d0003.se.local","lw401-d0004.se.local","lw401-d0005.se.local","lw401-d0006.se.local","lw401-d0007.se.local","lw401-d0008.se.local","lw401-d0009.se.local","lw401-d0010.se.local","lw401-d0011.se.local","lw401-d0012.se.local","lw401-d0013.se.local","lw401-d0014.se.local","lw401-d0015.se.local","lw401-d0016.se.local","lw401-d0017.se.local","lw401-d0018.se.local","lw401-d0019.se.local","lw401-d0020.se.local","lw401-d0021.se.local","lw401-d0022.se.local","lw401-d0023.se.local","lw401-d0024.se.local","lw401-d0025.se.local","lw401-d0026.se.local","lw401-d0027.se.local","lw401-d0028.se.local","lw401-d0029.se.local","lw401-d0030.se.local","lw401-d0031.se.local","lw401-d0032.se.local","lw401-d0033.se.local","lw401-d0034.se.local","lw401-d0035.se.local","lw401-d0036.se.local","lw401-d0037.se.local","lw401-d0038.se.local","lw401-d0039.se.local","lw401-d0040.se.local","lw401-d0041.se.local","lw401-d0042.se.local","lw401-d0043.se.local","lw401-d0044.se.local","lw401-d0045.se.local","lw401-d0046.se.local","lw401-d0047.se.local","lw401-d0048.se.local","lw401-d0049.se.local","lw401-d0050.se.local","lw401-d0051.se.local","lw401-d0052.se.local","lw401-d0053.se.local","lw401-d0054.se.local","lw401-d0055.se.local","lw401-d0056.se.local","lw401-d0057.se.local","lw401-d0058.se.local","lw401-d0059.se.local","lw401-d0060.se.local","lw401-d0061.se.local","lw401-d0062.se.local","lw401-d0063.se.local","lw401-d0064.se.local","lw401-d0065.se.local","lw401-d0066.se.local","lw401-d0067.se.local","lw401-d0068.se.local","lw401-d0069.se.local","lw401-d0070.se.local","lw401-d0071.se.local","lw401-d0072.se.local","lw401-d0073.se.local","lw401-d0074.se.local","lw401-d0075.se.local","lw401-d0076.se.local","lw401-d0077.se.local","lw401-d0078.se.local","lw401-d0079.se.local","lw401-d0080.se.local","lw401-d0081.se.local","lw401-d0082.se.local","lw401-d0083.se.local","lw401-d0084.se.local","lw401-d0085.se.local","lw401-d0086.se.local","lw401-d0087.se.local","lw401-d0088.se.local","lw401-d0089.se.local","lw401-d0090.se.local","lw401-d0091.se.local","lw401-d0092.se.local","lw401-d0093.se.local","lw401-d0094.se.local","lw401-d0095.se.local","lw401-d0096.se.local","lw401-d0097.se.local","lw401-d0098.se.local","lw401-d0099.se.local","lw401-d0100.se.local"]
devices_ID1 = ["lw401-d0001.se.local"]

devices=devices_ID
print('Устройства, на которых будет выполняться скрипт=', devices)
# devices=['10.77.30.3']
# commands = ['conf ter', 'voice service voip', 'ip address trusted list', 'ipv4 10.0.0.0 255.0.0.0','exit', 'sip', 'bind control source-interface GigabitEthernet0/1.7', 'bind media source-interface GigabitEthernet0/1.7', 'dial-peer voice 103 voip', 'description Anabar', 'destination-pattern 20[5-9].', 'session target ipv4:10.77.175.1', 'dtmf-relay rtp-nte', 'dial-peer voice 104 voip', 'description BelayGora', 'destination-pattern 21[0-4].', 'session target ipv4:10.77.180.1', 'dtmf-relay rtp-nte', 'dial-peer voice 105 voip', 'description Tiksi', 'destination-pattern 21[5-9].', 'session target ipv4:10.77.185.1', 'dtmf-relay rtp-nte', 'dial-peer voice 106 voip', 'description Batagay', 'destination-pattern 22..', 'session target ipv4:10.77.190.1', 'dtmf-relay rtp-nte', 'dial-peer voice 107 voip', 'description Jigansk', 'destination-pattern 23[0-4].', 'session target ipv4:10.77.195.1', 'dtmf-relay rtp-nte', 'dial-peer voice 108 voip', 'description Zyryanka', 'destination-pattern 23[5-9].', 'session target ipv4:10.77.200.1', 'dtmf-relay rtp-nte', 'dial-peer voice 109 voip', 'description Sangar', 'destination-pattern 24[0-4].', 'session target ipv4:10.77.205.1', 'dtmf-relay rtp-nte', 'dial-peer voice 110 voip', 'description Moma', 'destination-pattern 24[5-9].', 'session target ipv4:10.77.210.1', 'dtmf-relay rtp-nte', 'dial-peer voice 111 voip', 'description Nizhnekolyma', 'destination-pattern 25[0-4].', 'session target ipv4:10.77.215.1', 'dtmf-relay rtp-nte', 'dial-peer voice 112 voip', 'description Oimyakon', 'destination-pattern 25[5-9].', 'session target ipv4:10.77.220.1', 'dtmf-relay rtp-nte', 'dial-peer voice 113 voip', 'description Olekma', 'destination-pattern 26[0-4].', 'session target ipv4:10.77.225.1', 'dtmf-relay rtp-nte', 'dial-peer voice 114 voip', 'description Olenek', 'destination-pattern 27[0-4].', 'session target ipv4:10.77.230.1', 'dtmf-relay rtp-nte', 'dial-peer voice 115 voip', 'description Sredkolym', 'destination-pattern 27[5-9].', 'session target ipv4:10.77.235.1', 'dtmf-relay rtp-nte', 'dial-peer voice 116 voip', 'description Chokurdakh', 'destination-pattern 28[0-4].', 'session target ipv4:10.77.240.1', 'dtmf-relay rtp-nte', 'dial-peer voice 117 voip', 'description EvemoByt', 'destination-pattern 28[5-9].', 'session target ipv4:10.77.245.1', 'dtmf-relay rtp-nte', 'dial-peer voice 118 voip', 'description trunk_toDeputats', 'destination-pattern 29..', 'session target ipv4:10.77.250.1', 'dtmf-relay rtp-nte', 'dial-peer voice 5522 voip', 'huntstop', 'destination-pattern 0T', 'session target ipv4:10.77.7.253', 'no session transport udp', 'dtmf-relay rtp-nte', 'end', 'wr']
# commands = ["conf ter", "no archive", "archive", "path ftp://10.77.3.35/$h-$t", "write-memory", "exit", "voice service voip", "sip", "no bind media source-interface GigabitEthernet0/1.7", "exit", "no ip access-list extended MGMT", "ip access-list extended MGMT", "permit tcp any 10.77.0.0 0.0.255.255 eq 22", "permit tcp 10.77.0.0 0.0.255.255 any eq 22", "exit", "no ip access-list extended RDP1C", "ip access-list extended RDP1C", "permit tcp any host 80.73.69.174 eq 3393", "permit tcp any host 80.73.69.174 eq 3396", "permit tcp any host 10.77.3.8 eq 3389", "permit tcp any host 10.77.3.69 eq 3389", "exit", "no ip access-list extended lan_id", "ip access-list extended lan_id", "permit ip 10.77.0.0 0.0.255.255 172.26.0.0 0.0.255.255", "permit ip 10.77.0.0 0.0.255.255 10.0.0.0 0.255.255.255", "exit", "no ip access-list extended yakenergo", "ip access-list extended yakenergo", "permit ip 10.77.0.0 0.0.255.255 172.26.0.0 0.0.255.255", "permit ip 10.77.0.0 0.0.255.255 10.0.0.0 0.255.255.255", "exit", "dial-peer voice 103 voip", "session target ipv4:10.77.175.1", "dial-peer voice 104 voip", "session target ipv4:10.77.180.1", "dial-peer voice 105 voip", "session target ipv4:10.77.185.1", "dial-peer voice 106 voip", "session target ipv4:10.77.190.1", "dial-peer voice 107 voip", "session target ipv4:10.77.195.1", "dial-peer voice 108 voip", "session target ipv4:10.77.200.1", "dial-peer voice 109 voip", "session target ipv4:10.77.205.1", "dial-peer voice 110 voip", "session target ipv4:10.77.210.1", "dial-peer voice 111 voip", "session target ipv4:10.77.215.1", "dial-peer voice 112 voip", "session target ipv4:10.77.220.1", "dial-peer voice 113 voip", "session target ipv4:10.77.225.1", "dial-peer voice 114 voip", "session target ipv4:10.77.230.1", "dial-peer voice 115 voip", "session target ipv4:10.77.235.1", "dial-peer voice 116 voip", "session target ipv4:10.77.240.1", "dial-peer voice 117 voip", "session target ipv4:10.77.245.1", "dial-peer voice 118 voip", "session target ipv4:10.77.250.1", "line vty 0 4", "no access-class 117 in", "access-class 23 in", "exit", "line vty 5 15", "no access-class 117 in", "access-class 23 in", "end", "wr", "exit"]
commands = ["perl -pi -e 's/(è...ÿ)(..¿0)/$1þ$2/g' /opt/master-pdf-editor-5/masterpdfeditor5", 'exit']
# commands = ["sh version"]
# commands = ['conf ter', 'no ntp authentication-key 1 md5 15060E1F10243F34 7', 'no ntp authenticate', 'no ntp trusted-key 1', 'ntp master 14', 'no ntp server 80.73.69.174 prefer', 'ntp server 10.77.30.1 prefer', 'no ip access-list standard ntp_access', 'ip access-list standard ntp_access', 'permit 10.77.0.0 0.0.255.255', 'permit 10.100.0.0 0.0.0.255', 'permit 10.200.0.0 0.0.0.255', 'permit 172.26.160.0 0.0.1.255', 'no ip access-list standard ntp_peers', 'ip access-list standard ntp_peers', 'permit 10.77.0.0 0.0.255.255', 'permit 172.26.160.0 0.0.1.255', 'permit 10.100.0.0 0.0.0.255', 'permit 10.200.0.0 0.0.0.255', 'end', 'wr']
# commands = ["conf ter", "sntp server 10.77.30.1", "sntp broadcast client", "clock timezone +0900 9", "end", "wr"]
# commands = ["conf ter", "service timestamps log datetime localtime", "logging on", "logging buffered informational", "logging buffered 163860", "logging rate-limit 100 except 4", "logging rate-limit all 50", "logging console critical", "logging monitor debugging", "no ip domain-lookup", "archive", "log config", "logging enable", "notify syslog contenttype plaintext", "hidekeys", "no path ftp://172.26.160.22/$h-$t", "path ftp://10.77.3.35/$h-$t", "ip ftp username cisco-backup", "ip ftp password ftpPasswd", "kron occurrence SaveConfigSchedule at 05:09 1 recurring", "policy-list SaveConfig", "kron policy-list SaveConfig", "no cli write", "no cli write", "no cli write", "no cli write", "cli write", "logging trap debugging", "logging 10.77.3.24", "logging host 10.77.3.24", "logging trap debugging", "ip ssh time-out 60", "ip ssh logging events", "ip ssh version 2", "no access-list 117", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any established", "access-list 117 permit tcp 10.77.0.0 0.0.255.255 any log-input", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.100.0.0 0.0.0.255 any log-input", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any established", "access-list 117 permit tcp 10.200.0.0 0.0.0.255 any log-input", "access-list 117 deny ip any any log-input", "line vty 0 4", "access-class 117 in", "line vty 5 15", "access-class 117 in", "end", "wr"]
for oborudovanie in devices:
    try:
        result = send_show_command(ip=oborudovanie, username='root', enable='FknthjcC"1', password='FknthjcC"1', command=commands)
        pprint(result, width=600)
    except:
        print('На данном оборудовании', oborudovanie, 'скрипт отработал неудачно')
