#!/usr/bin/env python3
from multiprocessing import Value
import socket
import os
import json
import yaml

def dnstoip (name):
    try:
        ip_adr = socket.gethostbyname(name)
    except NameError:
        ip_adr = "Имя не отвечает"
    except socket.gaierror:
        ip_adr = "Имя не отвечает"
    return ip_adr

def file_open_write (name):
    fileIp = open('ipsrv.csv', 'w')
    fileIp.close()
    fileIp = open('ipsrv.csv', 'a')
    for key, value in name.items():
        writetofile = key + " " + value + ';'
        fileIp.write(writetofile)
    fileIp.close()
    return

def file_write_json (name):
    fileIp = open('ipsrv.json', 'w')
    listyaml = []
    for key, value in name.items():
        dir={}
        dir[key] = value
        listyaml.append(dir)
    yamlfile = {'site': listyaml}
    json.dump(yamlfile, fileIp, indent=2)
    fileIp.close()
    return  

def file_write_yaml (name):
    fileIp = open('ipsrv.yml', 'w')
    listyaml = []
    for key, value in name.items():
        dir={}
        dir[key] = value
        listyaml.append(dir)
    yamlfile = {'site': listyaml}
    yaml.dump(yamlfile, fileIp, explicit_start=True, explicit_end=True, indent=2)
    fileIp.close()
    return  


DNSdict = {}

if os.path.isfile('ipsrv.csv') == False:
    delfile = open('ipsrv.csv', 'w')
    delfile.close()
else:
    dictfile = open('ipsrv.csv', 'r').read().split(';')
    #print("dictfile ",dictfile)
    for a in dictfile:
        lista = a.split(" ")
        #print(lista[0])
        #print(lista[-1])
        DNSdict[lista[0]] = lista[-1]

address_srv = ['drive.google.com', 'mail.google.com', 'google.com']

for i in address_srv:
    addres_and_ip = dnstoip(i)
    if i in DNSdict.keys():
        if addres_and_ip != DNSdict[i]:
            print(f'[ERROR] {i} IP mismatch: {DNSdict[i]} {addres_and_ip}')
            DNSdict[i] = addres_and_ip
        else:
            print(i + " - " + addres_and_ip)
    else:
        DNSdict[i] = addres_and_ip
        print(i + " - " + addres_and_ip)
del DNSdict[""]
#print(DNSdict)
file_open_write(DNSdict)
file_write_json(DNSdict)
file_write_yaml(DNSdict)