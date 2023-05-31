# server
Należy podać polecenia niezbędne do:</br>
a. zbudowania opracowanego obrazu kontenera,</br>
'sudo docker build -t fullstack .' to komenda używana do budowania obrazu kontenera na podstawie pliku 'Dockerfile' w bieżącym katalogu.</br>
![image](https://github.com/pollubNorbert/server/assets/135065827/6465bcdb-3aa1-41a5-871b-d86f184c20ac)</br>
![fullstack2](https://github.com/pollubNorbert/server/assets/135065827/fe7569d0-b50d-4497-b717-fcb4b361f709)</br>
b. uruchomienia kontenera na podstawie zbudowanego obrazu,</br>
Komenda 'sudo docker run --name firstContainer -p 8000:8000 fullstack' służy do uruchomienia kontenera na podstawie obrazu o nazwie 'fullstack' i nadania mu nazwy 'firstContainer'.
![fullstack3](https://github.com/pollubNorbert/server/assets/135065827/79819880-af4b-4381-99df-b275c1a27f0d)</br>
c. sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera</br>
Komenda 'sudo docker logs firstContainer' służy do wyświetlania dziennika (logów) dla kontenera o nazwie 'firstContainer'.</br>
![fullstack4](https://github.com/pollubNorbert/server/assets/135065827/106140ff-e432-444b-8b0d-0541e31f83a4)</br>
d. sprawdzenia, ile warstw posiada zbudowany obraz.</br>
Komenda 'sudo docker history fullstack' służy do wyświetlania historii warstw obrazu</br>
![fullstack5](https://github.com/pollubNorbert/server/assets/135065827/171a9928-1f23-4415-a2ec-e17cb2733cc7)</br>

