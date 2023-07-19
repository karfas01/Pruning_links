

# __Обрезка ссылок с помощью *Bitly*__
___
__Обрезка ссылок с помощью *Bitly*__ - Данный проект поможет вам сокращать ссылки, а также получать обратную связь от этих ссылок в виде колличества переходов по ней.

#
## __Как установить__
___
Чтобы начать пользоваться моей программой вам нужно:
1. Получить ключ/токен от `API` Bitly , для этого переходим на сайт [Bitly](https://bitly.is/3PYvAPr) и регистрируемся в нём. 
Затем следуем по следующему пути: [личный кабинет Bitly](https://bitly.is/3PYvAPr) → settings → Developer settings → API → вводим пароль от личного кабинета и нажимаем Generate token → копируем полученый токен (поже он нам понадобится) → переходим в папку с скаченой программой и создаём файл с названием `.env` без расширения → в созданный фаил вставляем `BITLY_TOKEN=` без пробелов и сразу после `BITLY_TOKEN=` вставляем полученый токен (от API Bitly) без пробелов.
2. [Установить](https://bit.ly/3O1rWkW) илбо запустить Python3 (желательно версии [3.11.4](https://bit.ly/46MvdgG) на этой версии всё работает корректно).
3. Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей, команда для установки зависимостей ниже:
```
    pip install -r requirements.txt
```
### Рекомендуется использовать [virtualenv/venv](https://bit.ly/3XUudTL) для изоляции проекта.

#
## Какпользываться программой
1. Запускаем консоль из папки с программой.
2. вводим:
 ```
     python main.py сокращаемая или сокращённая ссылка
 ``` 
   В первом случие получим сокращенную ссылку, а во втором случие получим количество переходов по сокращённой ссылке.

#
## Цель проекта
___
Создать консоьное приложение для сокращения ссылок и аналитики посищаймости интернет рессурсов ссылки к каторым были сокращены с помощю этой консоьного приложения.

#
### Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://bit.ly/3O12fRN).
