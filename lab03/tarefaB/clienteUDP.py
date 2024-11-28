# SCRIPT: Servidor de sockets UDP modificado para bate-papo do cliente com o servidor

from socket import *

# Configuração do cliente
serverName = 'localhost'  # IP do servidor
serverPort = 61000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Criação do socket UDP

print("Cliente pronto para enviar mensagens. Digite 'sair' para encerrar.")

while 1:
  # Nesse loop, o cliente digita sua mensagem, que é enviada para o servidor. Após receber uma resposta, o loop volta ao início, dando a vez da mensagem ao cliente.

  message = input("Digite sua mensagem para o servidor: ")
  clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
  response, serverAddress = clientSocket.recvfrom(2048)
  print(f"Resposta do servidor: {response.decode('utf-8')}")

clientSocket.close()