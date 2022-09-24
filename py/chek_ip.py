#!/usr/bin/env python3
import os
def dnstoip (name):
    ipaddres = os.popen('nslookup ' + name).read()
    listns = ipaddres.split('\n')
    return listns[5]

def file_open_write (name):
    fileIp = open('ipsrv.csv', 'a')
    writetofile = name + '/n'
    fileIp.write(writetofile)
    fileIp.close()
    return print(f'данные {name} записаны')

DNSdict = {}


if os.path.isfile('ipsrv.csv') == False:
    delfile = open('ipsrv.csv', 'w')
    delfile.close()
else:
    dictfile = open('ipsrv.csv', 'r').read().split('/n')
    #print("dictfile ",dictfile)
    for a in dictfile:
        lista = a.split(" ")
        #print(lista[0])
        #print(lista[-1])
        DNSdict[lista[0]] = lista[-1]

address_srv = ['drive.google.com', 'googlemail.l.google.com', 'google.com']

print('Прошлые адреса: ',DNSdict)
print('*********************************')
for i in address_srv:
    addres_and_ip = dnstoip(i)
    ip_without_addres = addres_and_ip.replace('Address: ', '')
    if i in DNSdict.keys():
        if ip_without_addres != DNSdict[i]:
            print(f'[ERROR] {i} IP mismatch: {DNSdict[i]} {ip_without_addres}')
            forfile = i + " " + ip_without_addres
            file_open_write(forfile)
        else:
            print(f"IP адрес у {i} не изменился")
    else:
        forfile = i + " " + ip_without_addres
        file_open_write(forfile)

#os.system('echo -n >ipsrv.csv')
