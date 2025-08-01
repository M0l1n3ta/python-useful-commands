
from tabulate import tabulate

# Lista de diccionarios
data = [
    {'title': 'Python Tutorial', 'url': 'https://python.org'},
    {'title': 'Pandas Guide', 'url': 'https://pandas.pydata.org'},
    {'title': 'Flask Docs', 'url': 'https://flask.palletsprojects.com'}
]

# Convertir a lista de listas para tabulate
table = [[item['title'], item['url']] for item in data]

# Imprimir como tabla
print(tabulate(table, headers=['Title', 'URL'], tablefmt='grid'))
