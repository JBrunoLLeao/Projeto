import socket
import threading
import random

def handle_client(client_socket):
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        # Receive guess from the client through the API
        palpite = client_socket.recv(1024).decode('utf-8')

        if not palpite:
            break

        try:
            palpite = int(palpite)
            tentativas += 1

            if palpite == numero_secreto:
                mensagem = f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas."
                client_socket.send(mensagem.encode('utf-8'))
                break
            elif palpite < numero_secreto:
                client_socket.send("Tente um número maior.".encode('utf-8'))
            else:
                client_socket.send("Tente um número menor.".encode('utf-8'))

        except ValueError:
            client_socket.send("Por favor, insira um número válido.".encode('utf-8'))

    client_socket.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('127.0.0.1', 12345))
        server.listen(5)
        print("[Servidor] Aguardando conexões...")

        while True:
            client_socket, addr = server.accept()
            print(f"[Servidor] Conexão estabelecida com {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    run_server()
