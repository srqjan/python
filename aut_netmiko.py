
from netmiko import Netmiko
from getpass import getpass

my_dev = {
    'host': 'srx',
    'username':'srdjan',
    'password': 'Srdjan84',
    'device_type': 'juniper_junos'
}

net_conn = Netmiko(**my_dev)
cfg_commands = ['set system syslog archive size 110k files 3']
output = net_conn.send_config_set(cfg_commands)
print(output)

output = net_conn.commit()
print(output)

#output1 = net_conn.send_command("sh ver", use_textfsm=True)

output = net_conn.exit_config_mode()
output = net_conn.send_command("show configuration")

#print(output1)
