### Соберите образ из исходных файлов
`docker build --tag python-define-rgb .`
### Запустите ваш контейнер
 `docker run --publish 5000:5000 python-define-rgb`


 * Serving Flask app '/var/rgb/main.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)

____
## Техническое Задание
Необходимо написать REST-сервис для определения доминирующего цвета на RGB-изображении. Факт доминирования цвета определять по количеству пикселей, в которых был найден данный цвет.

Заявленная фукнциональность должна быть доступна через следующий API-метод:
POST /api/determine_dominate_color

Для тестирования необходимо создать html-страницу без оформления с единственной кнопкой input для загрузке изображения на сервер с последующим получением результата. При загрузке можно поставить ограничение на получение только png-изображений. Данная html-страница должна быть доступна по адресу:
GET /test/form/upload_image

В качестве фреймворка необходимо использовать flask, для проекта необходимо использовать git (с количеством коммитов строго более 2-х, допустима публикация решения через публичный github-репозиторий), для анализа изображения желательно использовать numpy, для запуска системы необходимо использовать Docker

Пример кода для загрузки изображений можно посмотреть в примерах (например, здесь https://stackoverflow.com/questions/60372919/python-problem-to-fetch-image-from-html-form), но необходимо перед отправкой кода в репозиторий привести весь код к единому стилю и продемонстрировать практики написания хорошего (чистого) кода

В репозиторий необходимо приложить изображения, на котором происходила проверка

Ориентировочное время на выполнение задания: 3-4 часа







