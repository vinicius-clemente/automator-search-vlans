#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################################
#                                                                          #
# NOME - SEARCH VLANS                                                      #
# AUTOR - VINICIUS CLEMENTE                                                #
# DATA - 03/03/21                                                          #
# DESCRIPTION - ESSE ROBO TEM COMO FACILITAR AS TAREFAS COMO VALIDAR       #
# VLANS, AUTOMATIZANDO EM TODO O AMBIENTE DE REDES                         #
#                                                                          #
############################################################################

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException

username = input('Enter your SSH username: ')
password = getpass()
vlan = input('Enter vlan: ')

arquivo_dispositivos = input('Enter devices file name (ex: devices_file_l2): ')

with open(arquivo_dispositivos) as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    if not devices.strip() or devices.startswith('#'):
        continue

    print('\nConnecting to device: ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except AuthenticationException:
        print('Authentication failure: ' + ip_address_of_device)
        continue
    except NetMikoTimeoutException:
        print('Timeout to device: ' + ip_address_of_device)
        continue
    except EOFError:
        print('End of file while attempting device ' + ip_address_of_device)
        continue
    except SSHException:
        print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + str(unknown_error))
        continue

    output = net_connect.send_command('show vlan id ' + vlan)
    print(output)

    net_connect.disconnect()
    print('-' * 40)