import yaml

# yaml1.yaml  ( list )
# ---               # pocetak svakog yaml file-a
# - 10.1.1.1        # [0]za kreiranje liste samo -
# - 10.1.1.2        # [1]
# - 10.1.1.3        # [2]

file = 'yaml1.yml'
with open (file) as f:
    out = yaml.load(f)

print(out)  # ['10.1.1.1', '10.1.1.2', '10.1.1.3']   list

#load yaml dict
filename = 'yaml2-dict.yml'
with open(filename) as f:
    output = yaml.load(f)

print(output)  # {'r1': '10.1.5.5', 'r2': '10.2.6.6'}