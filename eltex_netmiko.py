from netmiko import Netmiko
my_dev = {
    'host': 'olt',                                    # olt
    'username':'srdjan',
    'password': 'Srdjan84',
    'device_type': 'eltex'
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