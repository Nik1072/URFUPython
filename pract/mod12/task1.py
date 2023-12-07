import sqlite3


# ЗАДАНИЕ 1

# ПОДКЛЮЧЕНИЕ К БД
# Подключаемся к исходной базе данных
start_db_connection = sqlite3.connect('netflix.sqlite')
start_db_cursor = start_db_connection.cursor()

# Создаем новую базу данных для задачи
task1_conn = sqlite3.connect('task1.sqlite')
task1_cursor = task1_conn.cursor()


# СОЗДАНИЕ ТАБЛИЦ
# Таблица актеры
task1_cursor.execute('''
    CREATE TABLE actors (
        actor_id INTEGER PRIMARY KEY,
        actor_name TEXT UNIQUE
    )
''')
# Добавил UNIQUE в столбец actor_name, что б уже на этом
# этапе исключить повторение актёров

# Создаем таблицу фильмы
task1_cursor.execute('''
    CREATE TABLE movies (
        movie_id INTEGER PRIMARY KEY,
        title TEXT,
        director TEXT,
        cast TEXT,
        country TEXT,
        date_added TEXT,
        release_year INTEGER,
        rating TEXT,
        duration TEXT,
        listed_in TEXT,
        description TEXT
    )
''')
# Т.к. изначальные айди фильмов роли в задании не играют, я, для удобства, от них избавился, заменив на свои

# Создаем таблицу актер-фильм
task1_cursor.execute('''
    CREATE TABLE actor_movie (
        actor_id INTEGER,
        movie_id INTEGER,
        FOREIGN KEY (actor_id) REFERENCES actors (actor_id),
        FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
        PRIMARY KEY (actor_id, movie_id)
    )
''')


# ЗАПОЛНЯЕМ ТАБЛИЦЫ
# Копируем данные из исходной таблицы в новые
start_db_cursor.execute('SELECT * FROM netflix_titles')
for data_of_movie in start_db_cursor.fetchall():

    # Добавляем актеров в таблицу актеры
    cast = data_of_movie[4]  # Столбец 4 - 'cast' в netflix_titles, т.е. таблица со строкой из актёров фильма
    if cast:
        actors = [actor.strip() for actor in cast.split(',')]
        for actor in actors:
            task1_cursor.execute('INSERT OR IGNORE INTO actors (actor_name) VALUES (?)', (actor,))  # IGNORE INTO как раз для избежания повторений актёров

    # Добавляем фильмы в таблицу фильмы
    movie_data = data_of_movie[2:12]  # Индексы со 2 по 11 соответствуют столбцам от title до description
    task1_cursor.execute('INSERT INTO movies VALUES (NULL,?,?,?,?,?,?,?,?,?,?)', movie_data)

    # Добавляем связи актер-фильм
    movie_id = task1_cursor.lastrowid
    for actor in actors:
        actor_id_query = task1_cursor.execute('SELECT actor_id FROM actors WHERE actor_name=?', (actor,))
        actor_id = actor_id_query.fetchone()[0]
        task1_cursor.execute('INSERT OR IGNORE INTO actor_movie VALUES (?, ?)', (actor_id, movie_id))

# Сохраняем изменения и закрываем соединения
task1_conn.commit()
start_db_connection.close()
task1_conn.close()


# ЗАДАНИЕ 2

# Подключение к БД
t1_p2_connection = sqlite3.connect('task1.sqlite')
t1_p2_cursor = t1_p2_connection.cursor()

# Находим наиболее часто встречающуюся пару актеров
query = '''
    SELECT a1.actor_name, a2.actor_name, COUNT(*) as movies_together
    FROM actor_movie am1
    JOIN actor_movie am2 ON am1.movie_id = am2.movie_id AND am1.actor_id < am2.actor_id
    JOIN actors a1 ON am1.actor_id = a1.actor_id
    JOIN actors a2 ON am2.actor_id = a2.actor_id
    GROUP BY a1.actor_name, a2.actor_name
    ORDER BY movies_together DESC
    LIMIT 1
'''

t1_p2_cursor.execute(query)
result = t1_p2_cursor.fetchone()

if result:
    actor1, actor2, movies_together = result
    print(f"Наиболее часто работающая друг с другом пара актеров: {actor1} с {actor2}, что совместно участовали в {movies_together} фильмах.")
else:
    print("Нет данных.")

# Закрываем соединение
t1_p2_connection.close()