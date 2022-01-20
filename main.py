from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from collections import defaultdict
import pandas


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

xls_data = pandas.read_excel('db/wine2.xlsx')
wine_dict = defaultdict(list)
for wine in xls_data.values:
    wine_dict[wine[0]].append(dict(zip(list(xls_data), wine)))

rendered_page = template.render(
    age = datetime.now().year - 1920,
    wine_dict = wine_dict
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()