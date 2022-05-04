import textfsm
traceroute

with open('traceroute.template') as template:
fsm = textfsm.TextFSM(template)
result = fsm.ParseText(traceroute)
print(fsm.header)
print(result)
