1. Я дізнався про docker-compose
#
2. Я дізнався про Flask
#
3. Я дізнався про формат YAML
#
4. Я створив порожній каталог проекту
#
5. Створив каталоги my_app та тестів для модульних тестів проектів та fot. У проекті використовуються Flask та пакети redis. В модульному тестуванні використовуються pytest та 
пакети запитів.
#
6. Я запустив app.py, перевірив, чи працює проект, і запустив тести. Під час запуску я зіткнувся з деякими невдачами, така проблема з Redis та проблема з папкою журналів. Після 
вирішення веб-сторінки почали працювати добре.
#
7. Видалення Pipfiles-файлів. Створено Dockerfiles та Makefile для додатків, модульних тестів та для розгортання.
#
8. Makefile має деякі правила #app - запустити збірку докера для Dockerfile.app #tests - запустити збірку докера для Dockerfile.tests # test-app - запустити контейнер test-app 
#run - створити мережу для докер-контейнера та запустити redis та контейнери додатків теж. # docker-prune - видаляє та очищає невикористані контейнери, мережі, томи, зображення
#
9. Створення та запуск програми. Веб-сторінки працюють добре:

![image alt](https://github.com/Victor123135/labs/blob/main/Lab5/1.PNG?raw=true)
![image alt](https://github.com/Victor123135/labs/blob/main/Lab5/2.PNG?raw=true)
![image alt](https://github.com/Victor123135/labs/blob/main/Lab5/3.PNG?raw=true)
#
10. Очищаю всі ресурси в проекті make docker-prune
#
11. Створюю штовхаючі зображення до Dockerhub "docker-push:	@docker push $(REPO):app \	&& docker push $(REPO):tests"
#
12. Створено docker-compose.yml
#
13. Запустив docker-compose за допомогою "sudo docker-compose up"
#
14. Веб-сторінка добре працює на порту "localhost:80"
#
15. створив образ docker-compose
#
16. Зупинено docker-compose за допомогою "sudo docker-compose down"
#
17. Я пересунув зображення на DockerHub за допомогою "sudo docker-compose push"
#
18. На мій погляд, docker-compose краще використовувати. Цей спосіб більше стосується контексту docker і виконує більше функцій Docer.
