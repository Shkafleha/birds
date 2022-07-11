# Исследование миграций белолобого гуся

## Стадии обработки данных

Исходный датасет [здесь](https://drive.google.com/drive/folders/1guGE45Y1ZSvonVU7D4wPum5_Yb8i2r6T?usp=sharing).
Ноутбуки в этом репо делают обработку по следующим стадиям:

- **01_format** убраны ненужные колонки, данные и имена колонок приведены в питоно-пригодный формат
- **02_clean** удалены записи с некорректными координатами
    - широта или долгота равна NaN
    - широта и долгота одновременно околонулевые
    - резкие одиночные скачки в сторону от трека
- **03_region** всем записям сопоставлена страна, а также область и район, если точка в России
- **04_hunting** всем записям сопоставлен статус "охота"
    - `True` - в это время в этом месте была разрешена охота на гусей
    - `False` - не была разрешена охота

Ноутбуки сохраняют промежуточные данные в формате `parquet`, это удобней для проведения многочисленных экспериментов во время рисёча и отладки, т.к. он быстро загружается-сохраняется, и в нём сохраняются форматы данных (тогда как в случае с `csv` нужно к примеру каждый раз при загрузке файла указывать, что колонку `timestamp` нужно парсить как дату-время).

Для сохранения данных в `csv` можно воспользоваться ноутбуком `parquet2csv.ipynb`.

Итоговые данные в `csv` можно найти [здесь](https://drive.google.com/drive/folders/1C7VBbgeNygpLdrvURz8KcDHcRmLY3GuL?usp=sharing).

## Как запускать
Все ноутбуки для своей работы монтируют папку на `google drive`. В этой папке должны быть следующие подпапки:

- `datasets` - папка (или линк на папку) с исходными датасетами
- `code` - папка `code` из данного репо
- `results` - папка для хранения промежуточных результатов в формате parquet, в ней должны быть подпапки, соответствующие стадиям обработки данных (см. выше)
