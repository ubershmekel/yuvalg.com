#!/usr/bin/python

import jinja2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

copies = [
    {
        'name': 'dropbox',
        'id': 'bcvo',
        'logo': 'dropbox.png',
    },
    {
        'name': 'blizzard',
        'id': 'rohc',
        'logo': 'blizzard.gif',
        'logo_style': 'background-color: black;',
    }
]

html = open('secret_template.html', 'rb').read()
template = jinja2.Template(html)

for info in copies:
    rendered = template.render(**info)
    fname = '%s.html' % info['id']
    with open(fname, 'wb') as f:
        f.write(rendered)


