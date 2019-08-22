#obicno se od API-a dobija structured data ( dict , list ) ako je dict ,proverti .keys ako je lista len()
# Dictionary in dictionary ( nested dict )

routers = {
    'rtr1': {
        'bgp_peers': ['10.1.1.1', '10.2.2.2', '10.3.3.3', '10.4.4.4'],
        'device_type': 'juniper_junos',
        'ip_addr': '10.1.1.1',
        'password': 'Srdjan84'},

    'rtr2': {
        'bgp_peers': ['10.2.1.1', '10.3.2.2', '10.4.3.3', '10.5.4.4'],
        'device_type': 'cisco_ios',
        'ip_addr': '10.2.2.2',
        'password': 'Srdjan84'},
    'rtr3': {
        'bgp_peers': ['10.5.1.1', '10.5.2.2', '10.5.3.3', '10.10.4.4'],
        'device_type': 'cisco_iosxr',
        'ip_addr': '10.3.3.3',
        'password': 'Srdjan84'}





}

# kako se pristupa elemntima dictionary-ja
#type(routers)    # <class 'dict'>
# routers.keys()        #dict_keys(['rtr1', 'rtr2', 'rtr3'])
# routers['rtr1']  # {'bgp_peers': ['10.1.1.1', '10.2.2.2', '10.3.3.3', '10.4.4.4'], 'device_type': 'juniper_junos', 'ip_addr': '10.1.1.1', 'password': 'Srdjan84'}
# routers['rtr1'].keys()   # dict_keys(['bgp_peers', 'device_type', 'ip_addr', 'password'])
# len(routers['rtr1']['bgp_peers'])   # 4
# routers['rtr1']['bgp_peers']  # ['10.1.1.1', '10.2.2.2', '10.3.3.3', '10.4.4.4']
# routers['rtr1']['bgp_peers'][0]  # '10.1.1.1'
#
#
#
#
#
#
#
#
#
#
#
#