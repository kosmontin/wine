# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Запустите сайт командой 
```
python3 main.py [--file=db/data.xlsx]
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Подготовка файла данных

Для корректной работы сайта понадобится excel-файл, в котором необходимо расместить данные.
Ниже пример таблицы:

| Категория	| Название | Сорт | Цена |	Картинка |	Акция |
| --- | --- | --- | --- | --- | --- |
| Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
| Напитки | Коньяк классический | | 350 |	konyak_klassicheskyi.png	
| Белые вина | Ркацители |	Ркацители |	499 |	rkaciteli.png	
| Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png	
| Красные вина | Хванчкара | Александраули | 550 | hvanchkara.png	
| Белые вина | Кокур | Кокур | 450 | kokur.png	
| Красные вина | Киндзмараули | Саперави | 550 | kindzmarauli.png	
| Напитки | Чача | | 299 | chacha.png |	Выгодное предложение
| Напитки | Коньяк кизиловый | | 350 | konyak_kizilovyi.png	

## Комментарии к таблице:
- **Шапка таблицы должна соответствовать примеру выше**

- Допускается отсутствие данных в столбце "Сорт"

- Если в столбце "Акция" присутствует любой текст, то на сайте, в верхнем углу картинки этого товара появится дополнительно логотип "Выгодное предложение"

- В столбце "Картинка" указывается название файла, который необходимо поместить в папку images

- Готовый файл необходимо поместить в папку db

В качестве примера готового файла, в папке db расположен файл wine.xlsx

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
