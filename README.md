# Automator Search VLANs (L2 Infrastructure Auditor)

Ferramenta de automação desenvolvida em Python para auditoria e varredura de VLANs de Camada 2 (L2) em toda a topologia de switches, verificando portas físicas e lógicas (Port-Channels / Trunks) para identificar se uma VLAN está em uso ou disponível.

## Funcionalidades

- **Varredura L2 em Lote:** Conecta-se via SSH a todos os switches definidos no arquivo de inventário selecionado (ex: switches de acesso, distribuição ou datacenter).
- **Inspeção de Interfaces Físicas e Lógicas:** Consulta o banco de dados de VLANs (`show vlan id`) para mapear portas físicas e agregações lógicas associadas ao ID pesquisado.
- **Auditoria Pre-Decommission:** Valida rapidamente se uma VLAN ainda possui portas ativas antes de executar limpezas ou reaproveitamento de IDs na rede.
- **Resiliência na Execução:** Tratamento completo de exceções SSH (timeouts, falhas de autenticação e erros de protocolo) sem interromper a varredura dos demais equipamentos.

## Tecnologias Utilizadas

- **Python 3.x**
- **Netmiko / Paramiko:** Gerenciamento automatizado de sessões SSH e coleta estruturada de comandos CLI em switches Cisco IOS / NX-OS.

## Como Utilizar

1. Clone o repositório:

       git clone https://github.com/vinicius-clemente/automator-search-vlans.git
       cd automator-search-vlans

2. Instale as dependências:

       pip install -r requirements.txt

3. Preencha o arquivo de inventário (`devices.txt`) com os endereços IP dos switches L2.

4. Execute o script e informe suas credenciais, o ID da VLAN e o nome do arquivo de inventário:

       python search-vlans.py

   *(Ajuste o nome do arquivo `.py` conforme o script principal na pasta).*

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
