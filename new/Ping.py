#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pythonping import ping
import socket
print('**********************')
print('''
Меню:
help - 0
Ping - 1
Nslookup - 2
Tracert - 3
Exit - 4
''')
print('**********************')
start = True
while start:
    menu = int(input('Пункт меню: '))
    if menu == 0:
        print('''
        Меню:
        help - 0
        Ping - 1
        Nslookup - 2
        Tracert - 3
        Exit - 4''')
        print('**********************')
    if menu == 1:
        while start:
            IP_host = input('Введите адрес хоста / exit - выйти: ')
            if IP_host == 'exit':
                break              
            print(ping(IP_host))
    elif menu == 2:
        while start:
            dns_host = str(input('Введите имя / exit - выйти: '))
            if dns_host == 'exit':
                break
            print(socket.gethostbyname(dns_host))
    elif menu == 4:
        exit()
    
        
        



