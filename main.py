from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import pandas


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

xls_data = pandas.read_excel('db/wine.xlsx', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

rendered_page = template.render(
    age = datetime.now().year - 1920,
    cards = xls_data.to_dict(orient='records')
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()