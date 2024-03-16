import socket
import threading

def handle_client(client_socket, server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((server_address, server_port))

        while True:
            # Receive guess from the client
            palpite = client_socket.recv(1024)
            if not palpite:
                break

            # Forward guess to the server
            server_socket.send(palpite)

            # Receive response from the server
            resposta = server_socket.recv(1024)

            # Send response to the client
            client_socket.send(resposta)

    client_socket.close()

def run_api():
    server_address = '127.0.0.1'
    server_port = 12345

    api_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    api_server.bind(('127.0.0.1', 6789))
    api_server.listen(5)
    print("[API] Aguardando conexões...")

    while True:
        client_socket, addr = api_server.accept()
        print(f"[API] Conexão estabelecida com {addr}")
        api_handler = threading.Thread(target=handle_client, args=(client_socket, server_address, server_port))
        api_handler.start()

if __name__ == "__main__":
    run_api()
