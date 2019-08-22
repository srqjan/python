
def print_ip(ip_addr, username='admin', password='Cisco'):
    print(f"My IP address is {ip_addr}")                      # My IP address is 10.1.1.1
    print(username)                                           # srdjan
    print(password)                                           # Srdjan84

list = ['10.1.1.1', 'srdjan', 'Srdjan84']

# passing list to the function with * ( gleda pojedinacne elemnete liste i uparuje u funkciju sa argumentima

print_ip(*list)   # ip_addr=10.1.1.1 ; username=srdjan ; password=Srdjan84;

# Passing dictionary to function with **  ( key maust match parametar name - ip_addr = ip.addr

dict = {
    'ip_addr':'172.31.255.32',
    'username':'dise',
    'password':'Lortud',
}

print_ip(**dict)   # My IP address is 172.31.255.32 ; dise ; Lortud