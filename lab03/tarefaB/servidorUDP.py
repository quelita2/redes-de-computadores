# SCRIPT: Servidor de sockets UDP modificado para bate-papo do cliente com o servidor

from socket import *

# Configuração do servidor
serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # Criação do socket UDP
serverSocket.bind((serverName, serverPort))

print(f"Servidor UDP esperando mensagens na porta {serverPort}...")

while True:
    # Nesse loop, o servidor recebe mensagem do cliente e envia a sua mensagem
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print(f"Mensagem recebida de {clientAddress}: {message}")

    response = input("Digite sua resposta para o cliente: ")
    serverSocket.sendto(response.encode('utf-8'), clientAddress)