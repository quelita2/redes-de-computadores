# Laboratório 3 - Prática com Sockets

Este laboratório aborda a criação de aplicações baseadas em **Sockets TCP e UDP** para implementar funcionalidades de transferência de arquivos e comunicação em tempo real. A prática é dividida em duas tarefas principais.

## **Material da Prática**
[Material de Sockets - DCA/UFRN](https://www.dca.ufrn.br/~viegas/disciplinas/DCA0130/files/Sockets/)

---

## **Tarefa A: Sistema de Transferência de Arquivos**

Crie uma aplicação utilizando sockets TCP na qual o cliente pode receber e enviar arquivos de/para o servidor. 
O cliente deve enviar os comandos: 

`upload nome_do_arquivo ou download nome_do_arquivo`

1. No caso de upload, o arquivo deve ser enviado ao servidor e armazenado localmente.
2. No caso de download, o servidor deve enviar o arquivo solicitado para o cliente.

- O servidor deve verificar se o arquivo existe antes de enviá-lo ao cliente.
- Trate erros, como tentativa de download de arquivos inexistentes ou comandos inválidos.

SUGESTÃO: Crie dois arquivos de texto simples (por exemplo: arquivo1.txt e arquivo2.txt) e escreva alguma informação em 1 linha nesses arquivos para que sejam os arquivos que serão transferidos entre cliente e servidor.

DICA: Use o método open(arquivo.txt) para abrir o arquivo solicitado e o método .read() para ler o seu conteúdo.


### Funcionalidades:
- **Comandos suportados pelo cliente:**
  - `upload nome_do_arquivo`: Envia o arquivo especificado para o servidor.
  - `download nome_do_arquivo`: Solicita o arquivo especificado do servidor.
- **Validação no Servidor:**
  - Verifica se o arquivo solicitado no download existe antes de enviá-lo.
  - Retorna mensagens de erro no caso de comandos inválidos ou arquivos inexistentes.
- **Tratamento de Erros:**
  - Tentativa de download de arquivos inexistentes.
  - Envio de comandos inválidos.

---

## **Tarefa B: Sistema de Mensagens (Bate-Papo)**

Crie uma aplicação utilizando socket UDP na qual o cliente envia mensagens para o servidor e este também possa responder para o cliente.

- O cliente deve digitar um texto e enviar para o servidor.
- O servidor deve receber e também enviar um texto digitado para o cliente.
- Experimente também utilizar múltiplos clientes “conectados” ao servidor ao mesmo tempo.

DICA: Colocar o cliente em loop para que o socket não seja encerrado após o envio das mensagens.
