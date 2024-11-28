# SCRIPT: Servidor de sockets TCP modificado para permitir upload e download de arquivos.

from socket import *
import os

# Configuração do servidor
serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print(f"Servidor TCP esperando conexões na porta {serverPort} ...")

while 1:
  connectionSocket, addr = serverSocket.accept()
  print(f"Cliente {addr} conectado.")

  try:
    # Recebe o comando do cliente
    command = connectionSocket.recv(1024).decode('utf-8')
    print(f"Comando recebido: {command}")
    command_parts = command.split(" ")

    if len(command_parts) != 2:
      response = "Comando inválido. Use 'upload <nome_do_arquivo>' ou 'download <nome_do_arquivo>'."
      connectionSocket.send(response.encode('utf-8'))
      continue

    action, filename = command_parts

    if action == "upload":
      # Recebe o arquivo do cliente
      with open(filename, 'wb') as file:
        while True:
          data = connectionSocket.recv(1024)
          if not data:
            break
          file.write(data)
      response = f"Arquivo '{filename}' recebido e salvo no servidor."
      print(response)

    elif action == "download":
      # Verifica se o arquivo existe
      if os.path.exists(filename):
        connectionSocket.send(f"OK {os.path.getsize(filename)}".encode('utf-8'))
        with open(filename, 'rb') as file:
          while (chunk := file.read(1024)):
              connectionSocket.send(chunk)
        print(f"Arquivo '{filename}' enviado ao cliente.")
      else:
        response = f"Erro: Arquivo '{filename}' não encontrado no servidor."
        connectionSocket.send(response.encode('utf-8'))

    else:
      response = "Comando inválido. Use 'upload <nome_do_arquivo>' ou 'download <nome_do_arquivo>'."
      connectionSocket.send(response.encode('utf-8'))

  except Exception as e:
    print(f"Erro: {e}")
    connectionSocket.send(f"Erro no servidor: {e}".encode('utf-8'))

  finally:
    connectionSocket.close()