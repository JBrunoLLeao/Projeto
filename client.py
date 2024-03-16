import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 6789))  # Connect to the API server

    while True:
        palpite = input("Digite seu palpite (ou 'exit' para sair): ")
        if palpite.lower() == 'exit':
            break

        # Send guess to the server through the API
        client.send(palpite.encode('utf-8'))

        # Receive response from the API
        resposta = client.recv(1024)
        print(resposta.decode('utf-8'))

    client.close()

if __name__ == "__main__":
    run_client()
