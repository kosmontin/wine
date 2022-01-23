import argparse
from collections import OrderedDict, defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

parser = argparse.ArgumentParser(
    description='''Local web-server and site about wine. 
    After run, open in browser http://127.0.0.1:8000/''')
parser.add_argument('--file', type=str, default='db/data.xlsx', help='excel file for load data on site from it')
args = parser.parse_args()

FILE_PATH = args.file

if os.path.isfile(FILE_PATH):
    products_from_xls = pandas.read_excel(FILE_PATH, na_values=' ', keep_default_na=False)
    wines = defaultdict(list)
    for wine in products_from_xls.values:
        wines[wine[0]].append(dict(zip(list(products_from_xls), wine)))

    rendered_page = template.render(
        age=datetime.now().year - 1920,
        wines=OrderedDict(sorted(wines.items()))
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
else:
    print(f'File {FILE_PATH} not found. Please, check path and try again.')