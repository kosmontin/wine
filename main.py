from collections import OrderedDict, defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

xls_data = pandas.read_excel('db/wine3.xlsx', na_values=' ', keep_default_na=False)
wine_dict = defaultdict(list)
for wine in xls_data.values:
    wine_dict[wine[0]].append(dict(zip(list(xls_data), wine)))

rendered_page = template.render(
    age = datetime.now().year - 1920,
    wine_dict = OrderedDict(sorted(wine_dict.items()))
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()