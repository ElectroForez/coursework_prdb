# Курсовая работа (ПРДБ)


## Install
```
$ pip install PyQt5 psycopg2-binary
```

## Restore database
```
$ psql your_database < res/backup.sql
```
In docker-compose container
```
$  docker-compose exec postgres /bin/bash -c "psql -U admin -d coursework < /res/backup.sql"
```

## Run
```
$ python3 app/main.py
```
