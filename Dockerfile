# -- etap 1 - budowanie aplikacji -- /nw
FROM python:3.9 as builder

# -- aktualizacja listy pakietów systemowych -- /nw
RUN apt-get update

# -- ustawienie katalogu roboczego na /app -- /nw
WORKDIR /app

# -- skopiowanie plików zależności do katalogu roboczego -- /nw
COPY requirements.txt .

# -- instalacja zależności -- /nw
RUN pip install --no-cache-dir -r requirements.txt

# -- skopiowanie plików źródłowych -- / nw
COPY server.py .

# -- etap 2 - tworzenie obrazu kontenera -- /nw
FROM python:3.9-slim

# -- Ustawienie katalogu roboczego na /app -- /nw
WORKDIR /app

# -- skopiowanie plików z poprzedniego etapu -- /nw
COPY --from=builder /app .

# -- informacje o autorze pliku -- /nw
LABEL author="Norbert Wojcik"

# -- ustawienie zmiennej środowiskowej z portem -- /nw
ENV TCP_PORT=8000

# -- otwarcie portu -- /nw
EXPOSE $TCP_PORT

# -- uruchomienie serwera -- /nw
CMD ["python", "server.py"]

