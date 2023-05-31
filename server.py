import socket
import datetime

# -- informacje o serwerze -- /nw
author_name = "Norbert Wojcik"
tcp_port = 8000

# -- logowanie informacji -- /nw
current_time = datetime.datetime.now()
log_message = f"Serwer uruchomiony przez: {author_name}\nData uruchomienia: {current_time}\nPort TCP: {tcp_port}"
print(log_message)

# -- utworzenie gniazda serwera -- /nw
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', tcp_port))
server_socket.listen(1)
print("Serwer nasłuchuje na porcie", tcp_port)

def handle_client_connection(client_socket):
    # -- obsługa połączenia z klientem -- /nw
    client_address = client_socket.getpeername()
    print("Połączono z klientem o adresie", client_address)

    try:
        # -- przygotowanie strony -- /nw
        client_ip = client_address[0]
        current_time = datetime.datetime.now()
        response = f"Adres IP klienta: {client_ip}\nData i czas w strefie czasowej klienta: {current_time}"

        # -- wysłanie strony -- /nw
        http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + response
        client_socket.sendall(http_response.encode())
    except Exception as e:
        print("Wystąpił błąd podczas obsługi klienta:", e)

    finally:
        # -- zamknięcie połączenia -- /nw
        client_socket.close()
        print("Połączenie z klientem zakończone")

try:
    while True:
        # -- oczekiwanie na połączenie klienta -- /nw
        client_socket, client_address = server_socket.accept()
        handle_client_connection(client_socket)
except KeyboardInterrupt:
    print("Serwer zatrzymany.")

# zamknięcie gniazda serwera -- /nw
server_socket.close()
