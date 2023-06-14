# server
Zad2: </br>
![zad2](https://github.com/pollubNorbert/server/assets/135065827/319284f3-81d9-4d64-85a0-9cfe5d7f82a5)</br>
Zad1: Należy podać polecenia niezbędne do:</br>
a. zbudowania opracowanego obrazu kontenera,</br>
'sudo docker build -t image .' to komenda używana do budowania obrazu kontenera na podstawie pliku 'Dockerfile' w bieżącym katalogu.</br>
![poprawa1](https://github.com/pollubNorbert/server/assets/135065827/cdea0cdb-4405-4da2-9a87-6a16980939e8)</br>
![poprawa2](https://github.com/pollubNorbert/server/assets/135065827/08bd5254-e9f6-4d1c-98be-686fd5639fc0)</br>
b. uruchomienia kontenera na podstawie zbudowanego obrazu,</br>
Komenda 'sudo docker run --name container -p 8088:8088 image' służy do uruchomienia kontenera na podstawie obrazu o nazwie 'image' i nadania mu nazwy 'container'.</br>
![poprawa3](https://github.com/pollubNorbert/server/assets/135065827/6f6f097e-90bd-4283-9990-3a093a27db38)</br>
c. sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera</br>
Komenda 'sudo docker logs container' służy do wyświetlania dziennika (logów) dla kontenera o nazwie 'firstContainer'.</br>
<![poprawa4](https://github.com/pollubNorbert/server/assets/135065827/2d637889-8c1e-400d-ae08-e2ab9812aac8)</br>
d. sprawdzenia, ile warstw posiada zbudowany obraz.</br>
Komenda 'sudo docker history image' służy do wyświetlania historii warstw obrazu</br>
<![poprawa5](https://github.com/pollubNorbert/server/assets/135065827/5de2eab3-b904-4eb6-9334-3f54aba2916a)</br>
