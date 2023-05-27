from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import json
app = QApplication([])
window = QWidget()

movies_names = QListWidget()
movies_text = QTextEdit()
movie_line = QLineEdit()
movie_line.setPlaceholderText('Введите фильм...')
add_movie_button = QPushButton('Добавить фильм')
edit_movie_button = QPushButton('Изменить фильм')
del_movie_button = QPushButton('Удалить фильм')

layout_main = QHBoxLayout()

layout_v = QVBoxLayout()
layout_v.addWidget(movies_text)
layout_v.addwidget(movie_line)

layout_line_buttons = QHBoxLayout()
layout_line_buttons.addWidget(add_movie_button)
layout_line_buttons.addWidget(edit_movie_button)
layout_line_buttons.addWidget(del_movie_button)

layout_v.addLayout(layout_line_buttons)

layout_main.addWidget(movies_names)
layout_main.addLayout(layout_v)

with open('movies.json', 'r', encoding='utf-8') as file:
    movies = json.load(file)
    movies_names.addItems(movies)
def add_movie():
    movie = movie_line.text()
    with open('movies.json', 'r', encoding='utf-8') as file:
        movies = json.load(file)
    movies(movie) = ''
    with open('movies.json', 'w', encoding='utf-8') as file:
        json.dump(movies, file)
    movies_names.clear()
    movies_names.addItems(movies)
def info_movie():
    movie = movies_names.selectedItems()[0].text()
    with open('movie.json', 'r', encoding='utf-8') as file:
        movies = json.load(file)
    movies_text.setText(movies[movie])
def edit_movie():
    if movies_names.selectedItems():
        text_movie = movies_text.toPlainText()
        movie = movies_names.selectedItems()[0].text()
        with open('movies.json', 'r', encoding='ust-8') as file:
            movies = json.load(file)
        movies[movie] = text_country
        with open('movies.json', 'w', encoding='utf-8') as file:
            json.dump(movies, file)
        movies_names.clear()
        movies_text.clear()
        movies_names.addItems(movies)
def del_movie():
    if movies_names.selectedItems():
        movie = movies_names.selectedItems()[0].text()
        with open('movies.json', 'r', encoding='utf-8') as file:
            movies = json.load(file)
        movies[movie] = text_movie
        with open('movies.json', 'w', encoding='utf-8') as file:
            json.dump(movies, file)
        movies_names.clear()
        movies_text.clear()
        movies_names.addItems(movies)
def del_movie():
    if movies_names.selectedItems():
        movie = movies_names.selectedItems()[0].text()
        with open('movies.json', 'r', encoding='utf-8') as file:
            movies = json.load(file)
        del movies[movie]
        with open('movies.json', 'w', encoding='utf-8') as file:
            json.dump(movies, file)
        movies_names.clear()
        movies_text.clear()
        movies_names.addItems(movies)


add_movie_button.clicked.connect(add_movie)
movies_names.itemClicked.connect(info_movie)
edit_movie_button.clicked.connect(del_movie)
del_movie_button.clicked.connect(del_movie)

window.setLayout(layout_main)
window.show()
app.exec()



