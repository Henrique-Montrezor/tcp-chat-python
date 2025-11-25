# TCP Chat Python

Este projeto implementa um sistema simples de comunicação entre **cliente** e **servidor** utilizando **sockets TCP** em Python.

## 📌 Funcionalidades
- Conexão entre cliente e servidor via TCP/IP.
- Troca de mensagens em tempo real.
- Comando `sair` para encerrar a comunicação.

## 🗂 Estrutura do Projeto
```
tcp-chat-python/
├── server.py   # Código do servidor TCP
├── client.py   # Código do cliente TCP
```

## 🚀 Como Executar
### 1. Inicie o servidor:
```bash
python server.py
```

### 2. Em outro terminal, inicie o cliente:
```bash
python client.py
```

### 3. Para múltiplos clientes:
- Abra várias instâncias do terminal e execute `python client.py` em cada uma.
- Todos os clientes se conectarão ao mesmo servidor.

## ⚙️ Requisitos
- Python 3.x

## 🧑 Autor
Henrique Montrezor
