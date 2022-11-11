# REST-API приложение для получения данных из библиотеки
## установка
```commandline
pip install -r requirements.txt
```
## список запросов
* /books - список всех книг
* * /books/?pages_min={pages_num} - показать книги с количеством страниц больше указанного в pages_num
* * /books/?pages_max=100  - показать книги с количеством страниц меньше указанного в pages_num
* * /books/?pages_equal=100  - показать книги с количеством страниц равно указанному в pages_num
* * /books/?author={author_name}&title={book_title} - показать книги автора author_name с названием book_title
* /authors - список всех авторов
* * /authors/?name={author_name} - показать автора с указанным именем author_name
