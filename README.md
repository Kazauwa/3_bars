# 3_bars

Скрипт, который показывает информацию по барам Москвы

## Использование

`python bars.py`

После запуска программа приглашает пользователя ввести путь к .json файлу с барами, взятого с [портала открытых данных Москвы](http://data.mos.ru/opendata/7710881420-bary)
В результате работы, скрипт выводит самый большой и самый маленький бары Москвы.

`python bars.py [longitude latitude]`

Если, при запуске, дополнительными параметрами указать GPS-координаты, программа выведет ближайший к ним бар. Координаты должны разделяться пробелом и иметь точку, в качестве разделителя знаков.

Пример:

`python bars.py 75.800000000 37.50000000`
