from netmiko import Netmiko
my_dev = {
    'host': 'be-gw',
    'username':'remoteshell',
    'password': 'RSHen2ble#m',
    'device_type': 'huawei'
}

net_conn = Netmiko(**my_dev)
#cfg_commands = ['no ntp server 192.168.1.10']
cfg_list = []                # prazna lista u koju cemo dodati komande
cfg = input('show_command: ')     # ukucamo komandu kad pita
#cfg_set = input('set_command: ')
#cfg_list.append(cfg)         # dodamo je u listu
#output = net_conn.send_config_set(cfg_set)
#output_send_config = net_conn.send_config_set(cfg_set)  # send_config ulazi odmah u enable mod i podesava ruter
#print (output_send_config)
#cfg_comande = []
output_show_command = net_conn.send_command(cfg, use_textfsm=True)  # NE RADI NA HUAWEI   # send_command sluzi za show comande , sa cfg mi radi sa cfg_list ne radi
# da bi radio textfsm : (project1_env) srdjan@srdjan:~/ENV/project1_env$ export NET_TEXTFSM=~/ntc-templates/templates/
# i git clone u /home/srdjan srdjan@srdjan:~$ git clone https://github.com/networktocode/ntc-templates
# TextFSM vraca structured data ( list of dictionary )
print(type(output_show_command))
print(output_show_command)
# [{'protocol': 'Internet', 'address': '91.102.229.241', 'age': '0', 'mac': '0025.9e99.409f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/1'}, {'protocol': 'Internet', 'address': '91.102.229.242', 'age': '-', 'mac': 'b838.6129.a621', 'type': 'ARPA', 'interface': 'GigabitEthernet0/1'}, {'protocol': 'Internet', 'address': '91.102.229.245', 'age': '2', 'mac': '7819.f7d3.5e00', 'type': 'ARPA', 'interface': 'GigabitEthernet0/1'}, {'protocol': 'Internet', 'address': '192.168.1.1', 'age': '8', 'mac': '7819.f7d3.5e00', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.2', 'age': '-', 'mac': 'b838.6129.a620', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.5', 'age': '0', 'mac': '0025.9ed2.ef0b', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.6', 'age': '2', 'mac': '8866.3947.263f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.10', 'age': '37', 'mac': '54ab.3aa5.9128', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.11', 'age': '0', 'mac': '0025.9e99.409f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.12', 'age': '0', 'mac': '0025.9ed2.ef1d', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.13', 'age': '3', 'mac': '0025.9ed3.6259', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.14', 'age': '3', 'mac': '4cf9.5dca.872f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.16', 'age': '1', 'mac': '0425.c5b4.610f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.17', 'age': '0', 'mac': 'c81f.bedd.a11f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}, {'protocol': 'Internet', 'address': '192.168.1.123', 'age': '0', 'mac': 'c81f.bedd.9ecf', 'type': 'ARPA', 'interface': 'GigabitEthernet0/0'}]

#print(output_send_command[0])# {'protocol': 'Internet', 'address': '91.102.229.241', 'age': '0', 'mac': '0025.9e99.409f', 'type': 'ARPA', 'interface': 'GigabitEthernet0/1'

#Slanje vise komandi odjednom
commands = ["dis ip int brief | inc 1146", "dis bgp peer", "dis ospf peer brief"]

command_0 = commands[0]  # dis ip int brief

for command in commands:
    output = net_conn.send_command(command)
    print(output)

