# ТЗ на позицию DevOps_SRE

### 1 Вывести предпоследнюю строчку текстового файла file.txt можно командой:

```bash
tail -2 file.txt | head -1
```

### 2 HTTP-код ответа вебсервера  на GET-запрос ресурса <https://example.com/getUsers> можно получить нижеприведенной командой:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com/getUsers
```

### 3 VIRT и RES в выводе команды top:

VIRT - общее количество памяти, которое требуется процессу с учетом подкачки, библиотек, кода, данных.

RES, напротив, отображает реальное потребление памяти процессом в текущий момент времени.

### 4 Общее между продуктами Logstash, Apache Flume, Filebeat:

Все эти продукты служат для сбора, парсинга, трансформации, агрегирования и доставки больших объемов данных лог файлов.

### 5 InfluxDB и Prometheus:

Prometheus - это система мониторинга, которая отвечает за сбор и хранение данных во встроенной БД временных рядов, построение графиков, а так же оповещение о событиях. InfluxDB представляет из себя только БД временных рядов.

Prometheus использует модель извлечения данных, InfluxDB, наоборот, находится в пассивном состоянии, т.е. ожидает, когда приложения сами отправят данные.

Prometheus ориентирован на хранение предварительно агрегированных метрик. InfluxDB больше подходит для регистрации событий.

И Promtheus и InfluxDB отлично подходят для хранения данных временных рядов. Выбор зависит от критериев, которые выдвигает приложение.
