from napalm import get_network_driver

driver = get_network_driver('ios')
ios1921 = driver('192.168.1.2', 'srdjan', 'Srdjan84')
ios1921.open()

outuput = ios1921.get_facts()
print(outuput)