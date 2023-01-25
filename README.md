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
$ docker-compose exec -T postgres psql -d coursework -U app < res/backup.sql
```

## Run
```
$ python3 app/main.py
```
