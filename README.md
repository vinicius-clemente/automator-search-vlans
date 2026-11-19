# automator-search-vlans

Automated Python tool to scan Layer 2 switches across physical and logical interfaces (Port-Channels/Trunks) to audit VLAN usage and availability.



\# Automator Search VLANs (L2 Infrastructure Auditor)



Ferramenta de automacao desenvolvida em Python para auditoria e varredura de VLANs de Camada 2 (L2) em toda a topologia de switches, verificando portas fisicas e logicas (Port-Channels / Trunks) para identificar se uma VLAN esta em uso ou disponivel.



\## Funcionalidades



\- \*\*Varredura L2 em Lote:\*\* Conecta-se via SSH a todos os switches definidos no arquivo de inventario selecionado (ex: switches de acesso, distribuicao ou datacenter).

\- \*\*Inspecao de Interfaces Fisicas e Logicas:\*\* Consulta o banco de dados de VLANs (`show vlan id`) para mapear portas fisicas e agregacoes logicas associadas ao ID pesquisado.

\- \*\*Auditoria Pre-Decommission:\*\* Valida rapidamente se uma VLAN ainda possui portas ativas antes de executar limpezas ou reaproveitamento de IDs na rede.

\- \*\*Resiliencia na Execucao:\*\* Tratamento completo de excecoes SSH (timeouts, falhas de autenticacao e erros de protocolo) sem interromper a varredura dos demais equipamentos.



\## Tecnologias Utilizadas



\- \*\*Python 3.x\*\*

\- \*\*Netmiko / Paramiko:\*\* Automacao de conexoes SSH e coleta estruturada de comandos CLI em switches Cisco IOS / NX-OS.



\## Como Utilizar



1\. Clone o repositorio:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/vinicius-master/automator-search-vlans.git](https://github.com/vinicius-master/automator-search-vlans.git)

&#x20;  cd automator-search-vlans

