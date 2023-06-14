from flask import Flask, request
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

# -- dane autora serwera -- /nw
author_name = "Norbert"
author_surname = "Wojcik"

@app.route('/')
def index():
    # -- pobranie adresu IP klienta -- /nw
    client_ip = request.remote_addr

    # -- pobranie bieżącej daty i godziny -- /nw
    client_timezone = timezone(request.headers.get('X-Appengine-User-Timezone', 'UTC'))
    client_time = datetime.now(client_timezone)

    # -- tworzenie treści strony -- /nw
    page_content = f"<h1>Informacje o kliencie</h1>" \
                   f"<p>Adres IP klienta: {client_ip}</p>" \
                   f"<p>Data i godzina w strefie czasowej klienta: {client_time}</p>"

    return page_content

if __name__ == '__main__':
    #-- pobranie bieżącej daty i godziny uruchomienia serwera -- /nw
    server_start_time = datetime.now()

    # -- pobranie numeru portu -- /nw
    port = 8088

    # -- wyświetlenie informacji o uruchomieniu serwera -- /nw
    print(f"Serwer uruchomiony. Data uruchomienia: {server_start_time}")
    print(f"Autor serwera: {author_name} {author_surname}")
    print(f"Serwer nasłuchuje na porcie: {port}")

    # -- uruchomienie serwera Flask -- /nw
    app.run(port=port)
