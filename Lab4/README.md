# Lab4

1. Ознайомившись з документацією я з'ясував що таке Docker а потім завантажив його на віртуальну машину перенаправив вивід у файл my_work.log
#
2. Зареєструвався і створив репозиторій на Docker Hub - Viсtor/Lab4/
#
3. Запустив веб-сервер за допомогою команди sudo docker run -it --name=django --rm -p 8000:8000 Viсtor/Lab4:django
#
4. Створив Dockerfile.site
#
5. Виконав білд (build) Docker імеджа та завантажив його до репозиторію за допомогою команд sudo docker build -t Viсtor/Lab4:monitoring . --file Dockerfile.site sudo docker 
images sudo docker push Viсtor/Lab4:monitoring
#
6. Щоб отримати логи виконав команди: sudo docker run -it --name=django --rm -p 8000:8000 Viсtor/Lab4:django sudo docker run -it --rm --net=host -v 
$(pwd)/server.log:/app/server.log Viсtor/Lab4:monitoring
