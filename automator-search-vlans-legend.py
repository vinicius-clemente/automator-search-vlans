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

# ==============================================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ==============================================================================
from getpass import getpass  # Oculta a digitação da senha no terminal por segurança
from netmiko import ConnectHandler  # Biblioteca principal para conexões SSH em dispositivos de rede
from netmiko.ssh_exception import NetMikoTimeoutException, \
    AuthenticationException  # Tratamento de erros de login e timeout
from paramiko.ssh_exception import SSHException  # Tratamento de falhas no protocolo SSH

# ==============================================================================
# ENTRADA DE DADOS (INPUTS DO OPERADOR)
# ==============================================================================
username = input('Enter your SSH username: ')  # Solicita o usuário de acesso aos switches
password = getpass()  # Solicita a senha de forma segura (sem exibir na tela)
vlan = input('Enter vlan: ')  # Número da VLAN que será consultada em todo o inventário

# Solicita dinamicamente o nome do arquivo de inventário (permite alternar entre L2, Core, Datacenter, etc.)
arquivo_dispositivos = input('Enter devices file name (ex: devices_file_l2): ')

# ==============================================================================
# LEITURA DO INVENTÁRIO DE EQUIPAMENTOS
# ==============================================================================
# Abre o arquivo indicado pelo operador e transforma cada linha (IP) em um item da lista
with open(arquivo_dispositivos) as f:
    devices_list = f.read().splitlines()

# ==============================================================================
# LOOP DE EXECUÇÃO POR EQUIPAMENTO
# ==============================================================================
for devices in devices_list:
    # Ignora linhas vazias ou linhas comentadas com '#' dentro do arquivo de inventário
    if not devices.strip() or devices.startswith('#'):
        continue

    print('\nConnecting to device: ' + devices)
    ip_address_of_device = devices

    # Dicionário com os parâmetros de conexão exigidos pelo Netmiko
    ios_device = {
        'device_type': 'cisco_ios',  # Driver padrão para switches Cisco IOS / Catalyst
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    # ==========================================================================
    # ESTABELECIMENTO DA SESSÃO SSH E TRATAMENTO DE ERROS
    # ==========================================================================
    try:
        net_connect = ConnectHandler(**ios_device)  # Abre a sessão SSH com o switch
    except AuthenticationException:
        print('Authentication failure: ' + ip_address_of_device)  # Credenciais inválidas no equipamento
        continue
    except NetMikoTimeoutException:
        print('Timeout to device: ' + ip_address_of_device)  # Equipamento inacessível ou porta SSH bloqueada
        continue
    except EOFError:
        print(
            'End of file while attempting device ' + ip_address_of_device)  # Sessão encerrada inesperadamente pelo switch
        continue
    except SSHException:
        print(
            'SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)  # Falha na negociação SSH (versão/algoritmo)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + str(unknown_error))  # Captura qualquer outro erro sem interromper a varredura
        continue

    # ==========================================================================
    # CONSULTA DA VLAN E ENCERRAMENTO DA SESSÃO
    # ==========================================================================
    # Envia o comando para verificar a existência, status e portas associadas à VLAN informada
    output = net_connect.send_command('show vlan id ' + vlan)
    print(output)  # Exibe o resultado da consulta diretamente no terminal

    # Encerra a sessão SSH para liberar a linha VTY do switch
    net_connect.disconnect()
    print('-' * 40)  # Separador visual entre a saída de cada equipamento