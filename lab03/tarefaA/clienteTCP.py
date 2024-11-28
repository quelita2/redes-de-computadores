# SCRIPT: Servidor de sockets TCP modificado para permitir upload e download de arquivos.

from socket import *
import os

# Configuração do cliente
serverName = 'localhost'
serverPort = 61000

while 1:
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))

  try:
    # Solicita o comando ao usuário
    command = input("Digite o comando ('upload <nome_do_arquivo>' ou 'download <nome_do_arquivo>'): ")
    command_parts = command.split(" ")

    if len(command_parts) != 2:
      print("Comando inválido. Use 'upload <nome_do_arquivo>' ou 'download <nome_do_arquivo>'.")
      continue

    action, filename = command_parts

    clientSocket.send(command.encode('utf-8'))

    # Envia o arquivo para o servidor, caso não haja envia uma mensagem de erro
    if action == "upload":
      if os.path.exists(filename):
        with open(filename, 'rb') as file:
          while (chunk := file.read(1024)):
            clientSocket.send(chunk)
        print(f"Arquivo '{filename}' enviado ao servidor.")
      else:
        print(f"Erro: Arquivo '{filename}' não encontrado no cliente.")

    # Recebe a resposta do servidor de um arquivo solicitado e salva o conteúdo recebido, caso não haja envia uma mensagem de erro (baixa arquivo)
    elif action == "download":
      response = clientSocket.recv(1024).decode('utf-8')
      if response.startswith("OK"):
        file_size = int(response.split()[1])
        with open(filename, 'wb') as file:
          bytes_received = 0
          while bytes_received < file_size:
            chunk = clientSocket.recv(1024)
            if not chunk:
              break
            file.write(chunk)
            bytes_received += len(chunk)
        print(f"Arquivo '{filename}' recebido do servidor.")
      else:
        print(response)

    else:
      print("Comando inválido. Use 'upload <nome_do_arquivo>' ou 'download <nome_do_arquivo>'.")

  except Exception as e:
    print(f"Erro: {e}")

  # Encerramento do socket do cliente
  finally:
    clientSocket.close()